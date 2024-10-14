# pip install openvino-genai huggingface_hub

import huggingface_hub as hf_hub

model_id = "OpenVINO/mistral-7b-instrcut-v0.1-int8-ov"
model_path = "mistral-7b-instrcut-v0.1-int8-ov"

hf_hub.snapshot_download(model_id, local_dir=model_path)

import openvino_genai as ov_genai

device = "CPU"
pipe = ov_genai.LLMPipeline(model_path, device)
print(pipe.generate("What is OpenVINO?", max_length=200))
