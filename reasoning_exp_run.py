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

# from video_llama.common.config import Config
# from video_llama.common.dist_utils import get_rank
# from video_llama.common.registry import registry
# from video_llama.conversation.conversation_video import Chat, Conversation, default_conversation,SeparatorStyle,conv_llava_llama_2
# import decord
# decord.bridge.set_bridge('torch')

# #%%
# # imports modules for registration
# from video_llama.datasets.builders import *
# from video_llama.models import *
# from video_llama.processors import *
# from video_llama.runners import *
# from video_llama.tasks import *

# #%%
# def parse_args():

#     parser = argparse.ArgumentParser(description="Demo")

#     # Add the --start and --end arguments with optional help messages and default values
#     # idea is to run this file 5 times in different slurm files in hprc to fasten the process
#     parser.add_argument("--start", type=int, help="The start value", default=0)
#     parser.add_argument("--end", type=int, help="The end value", default=10)
#     parser.add_argument("--text", type=int, help="The text prompt no. (1 or 2 )", default=1)

#     parser.add_argument("--cfg-path", default='eval_configs/video_llama_eval_withaudio.yaml', help="path to configuration file.")
#     parser.add_argument("--gpu-id", type=int, default=0, help="specify the gpu to load the model.")
#     parser.add_argument("--model_type", type=str, default='vicuna', help="The type of LLM")
#     parser.add_argument(
#         "--options",
#         nargs="+",
#         help="override some settings in the used config, the key-value pair "
#         "in xxx=yyy format will be merged into config file (deprecate), "
#         "change to --cfg-options instead.",
#     )
#     args = parser.parse_args()
#     return args


# def setup_seeds(config):
#     seed = config.run_cfg.seed + get_rank()

#     random.seed(seed)
#     np.random.seed(seed)
#     torch.manual_seed(seed)

#     cudnn.benchmark = False
#     cudnn.deterministic = True


# # # ========================================
# # #             Model Initialization
# # # ========================================

# print('Initializing Chat')
# args = parse_args()
# cfg = Config(args)
 
# model_config = cfg.model_cfg
# model_config.device_8bit = args.gpu_id
# print(args.gpu_id)

# model_cls = registry.get_model_class(model_config.arch)

# model = model_cls.from_config(model_config).to('cuda:{}'.format(args.gpu_id))
# model.eval()

# vis_processor_cfg = cfg.datasets_cfg.webvid.vis_processor.train
# vis_processor = registry.get_processor_class(vis_processor_cfg.name).from_config(vis_processor_cfg)
# chat = Chat(model, vis_processor, device='cuda:{}'.format(args.gpu_id))
# print('Initialization Finished')

def load(path):
    with open(path, 'r') as f:
        return json.load(f)

def write_json(path,data):
    with open(path,'w') as f:
        json.dump(data,f,indent =4)
    
# def reset(chat_state, img_list):
#     if chat_state is not None:
#         chat_state.messages = []
#     if img_list is not None:
#         img_list = []
#     return  chat_state, img_list

# def upload_video(gr_video, chat_state,audio_flag):
#     if args.model_type == 'vicuna':
#         chat_state = default_conversation.copy()
#     else:
#         chat_state = conv_llava_llama_2.copy()
    
#     if gr_video is not None:
#         print(gr_video)
#         chat_state.system =  ""
#         img_list = []
#         if audio_flag:
#             llm_message = chat.upload_video(gr_video, chat_state, img_list)
#         else:
#             llm_message = chat.upload_video_without_audio(gr_video, chat_state, img_list)
#         return  chat_state, img_list

# def gradio_ask(user_message,chat_state):
#     if len(user_message) == 0:
#         return 'Input should not be empty!'
#     chat.ask(user_message, chat_state)
#     return chat_state

# def gradio_answer( chat_state, img_list, num_beams, temperature):
#     llm_message = chat.answer(conv=chat_state,
#                               img_list=img_list,
#                               num_beams=num_beams,
#                               temperature=temperature,
#                               max_new_tokens=300,
#                               max_length=2000)[0]
#     # print(f"chat_state.get_prompt(): {chat_state.get_prompt()}")
#     # print(f"chat_state: {chat_state}")
#     # print(f"llm message: {llm_message}")
#     return chat_state, img_list, llm_message

# def videollama_output_generation(video_path,text_input):
#     num_beams = 1
#     temperature = 1

#     audio_flag = 1
#     chat_state = default_conversation.copy()
#     # def upload_video(gr_video, chat_state,audio_flag):
#     chat_state,image_list = upload_video(video_path,chat_state,audio_flag)
#     # asking question to llm
#     chat_state = gradio_ask (text_input, chat_state)
#     # extracting asnwer from llm
#     chat_state,image_list, llm_message = gradio_answer(chat_state,image_list,num_beams,temperature)

#     # print(f"llm message: {llm_message}")

#     chat_state, image_list = reset(chat_state,image_list)
#     return llm_message

def main():

    data_path ="../data/anomaly_watchdog_data/_anomaly_watchdog_data.json" #filtered validation videos (val_filtered.txt): 4711
    results_dir = "./results" # results will be saved  

    prmt_1_merged_res_path = "./results/prompt1/merged_results_0_4711.json"
    prmpt_1_merged_res_data = load(prmt_1_merged_res_path)

    dataset_list = []
    for k,v in prmpt_1_merged_res_data.items():
        # print(k,v)
        if v['gt_failure'] ==1 and v['pred_failure']==1:
            dataset_list.append(k)
        
    print(len(dataset_list))
    print(dataset_list[0:2])
if __name__ == "__main__":
    main()



        

