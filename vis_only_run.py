"""
Adapted from: https://github.com/Vision-CAIR/MiniGPT-4/blob/main/demo.py
"""
import argparse
import os
import argparse
import random
import json
from tqdm import tqdm


import numpy as np
import torch
import torch.backends.cudnn as cudnn
import gradio as gr

from video_llama.common.config import Config
from video_llama.common.dist_utils import get_rank
from video_llama.common.registry import registry
from video_llama.conversation.conversation_video import Chat, Conversation, default_conversation,SeparatorStyle,conv_llava_llama_2
import decord
decord.bridge.set_bridge('torch')

#%%
# imports modules for registration
from video_llama.datasets.builders import *
from video_llama.models import *
from video_llama.processors import *
from video_llama.runners import *
from video_llama.tasks import *

#%%
def parse_args():
    parser = argparse.ArgumentParser(description="Demo")

    # Add the --start and --end arguments with optional help messages and default values
    # idea is to run this file 5 times in different slurm files in hprc to fasten the process
    parser.add_argument("--start", type=int, help="The start value", default=0)
    parser.add_argument("--end", type=int, help="The end value", default=10)
    parser.add_argument("--text", type=int, help="The text prompt no. (1 or 2 )", default=1)

    parser.add_argument("--cfg-path", default='eval_configs/video_llama_eval_withaudio.yaml', help="path to configuration file.")
    parser.add_argument("--gpu-id", type=int, default=0, help="specify the gpu to load the model.")
    parser.add_argument("--model_type", type=str, default='vicuna', help="The type of LLM")
    parser.add_argument(
        "--options",
        nargs="+",
        help="override some settings in the used config, the key-value pair "
        "in xxx=yyy format will be merged into config file (deprecate), "
        "change to --cfg-options instead.",
    )
    args = parser.parse_args()
    return args


def setup_seeds(config):
    seed = config.run_cfg.seed + get_rank()

    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)

    cudnn.benchmark = False
    cudnn.deterministic = True


# # ========================================
# #             Model Initialization
# # ========================================

print('Initializing Chat')
args = parse_args()
cfg = Config(args)
 
model_config = cfg.model_cfg
model_config.device_8bit = args.gpu_id
print(args.gpu_id)

model_cls = registry.get_model_class(model_config.arch)

model = model_cls.from_config(model_config).to('cuda:{}'.format(args.gpu_id))
model.eval()

vis_processor_cfg = cfg.datasets_cfg.webvid.vis_processor.train
vis_processor = registry.get_processor_class(vis_processor_cfg.name).from_config(vis_processor_cfg)
chat = Chat(model, vis_processor, device='cuda:{}'.format(args.gpu_id))
print('Initialization Finished')



def reset(chat_state, img_list):
    if chat_state is not None:
        chat_state.messages = []
    if img_list is not None:
        img_list = []
    return  chat_state, img_list
#-----------------------------------------------
def upload_video(gr_video, chat_state,audio_flag):
    if args.model_type == 'vicuna':
        chat_state = default_conversation.copy()
    else:
        chat_state = conv_llava_llama_2.copy()
    
    if gr_video is not None:
        print(gr_video)
        chat_state.system =  ""
        img_list = []
        if audio_flag:
            llm_message = chat.upload_video(gr_video, chat_state, img_list)
        else:
            llm_message = chat.upload_video_without_audio(gr_video, chat_state, img_list)
        return  chat_state, img_list
    #---------------------------------------------


#-------------------------------
def gradio_ask(user_message,chat_state):
    if len(user_message) == 0:
        return 'Input should not be empty!'
    chat.ask(user_message, chat_state)
    return chat_state
#--------------------------------

def gradio_answer( chat_state, img_list, num_beams, temperature):
    llm_message = chat.answer(conv=chat_state,
                              img_list=img_list,
                              num_beams=num_beams,
                              temperature=temperature,
                              max_new_tokens=300,
                              max_length=2000)[0]
    # print(f"chat_state.get_prompt(): {chat_state.get_prompt()}")
    # print(f"chat_state: {chat_state}")
    # print(f"llm message: {llm_message}")
    return chat_state, img_list, llm_message

def write_json(output_file_name,data):
    with open(output_file_name,'w') as f:
        json.dump(data,f,indent =4)

def open_json(file_name):
    with open(file_name,'r') as f:
        data = json.load(f)
    return data
# #TODO show examples below


def videollama_output_generation(video_path,text_input):
    num_beams = 1
    temperature = 1

    audio_flag = 0
    chat_state = default_conversation.copy()
    # def upload_video(gr_video, chat_state,audio_flag):
    chat_state,image_list = upload_video(video_path,chat_state,audio_flag)
    # asking question to llm
    chat_state = gradio_ask (text_input, chat_state)
    # extracting asnwer from llm
    chat_state,image_list, llm_message = gradio_answer(chat_state,image_list,num_beams,temperature)

    # print(f"llm message: {llm_message}")

    chat_state, image_list = reset(chat_state,image_list)
    return llm_message

def load(path): 
    with open(path, 'r') as f: 
        return json.load(f)

    






def main():

    data_path ="./data/anomaly_watchdog_data/_anomaly_watchdog_data.json" #filtered validation videos (val_filtered.txt): 4711
    results_dir = "./results" # results will be saved 
  

    
    # print(all_videos[args.start: args.end])
    # loading the anomaly data--> videopath, failure: 1/0
    data = load(data_path)
    # converting it to a list
    dataset_list = [value for value in data.values()]
    #splitting the dataset according to the arguments provided
    dataset_list=dataset_list[args.start: args.end]
    # print(dataset_list)
    
    if args.text ==1: # first baseline text input
        text_input = "Does this video contain any unusual activities? Please reply Yes or No only."
    else:  # second baseline text input
        text_input = "Let's look at this video frame by frame. Does this video contain any unusual activities? Please reply Yes or No only."

    results ={}
    key_idx = args.start
    with tqdm(total = args.end-args.start) as pbar:
        for video in dataset_list:
            print(video)
            video_path ="./"+video['path']
            llm_message = videollama_output_generation(video_path,text_input)
            # llm_message = "No, the video contains an unusual activity. At 2.6 seconds, a man walks past a house at night with a camera in his hand, and at 4.7 seconds, a man and a dog are walking across a wooden deck at night. This implies that the man in the video is taking photos of people and their surroundings."

            if "yes" in llm_message[:3].lower():
                pred_failure = 1
            elif "no" in llm_message[:2].lower():
                pred_failure = 0
            else: 
                pred_failure = 'na'


            _res = {
                'video_path': video_path,
                'prompt': text_input,
                'videollama_ouput':llm_message,
                'gt_failure': video['failure'],
                'pred_failure' :pred_failure
            }
            
            results[key_idx] = _res
            key_idx+=1
            # print(res)
            

            pbar.update(1)
    # print(results)
    output_file_name = f"{results_dir}/Ablate_vis_only/prompt_1/{args.start}_{args.end}_results.json"
    write_json(output_file_name, results)







# IN TOTAL validation oops videos (filtered): 
if __name__ == "__main__":
    main()

# %%



