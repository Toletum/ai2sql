# https://huggingface.co/OpenVINO
# pip install openvino-genai huggingface_hub
import time

import huggingface_hub as hf_hub
import openvino_genai as ov_genai


model_path = "models/mistral-7b-instrcut-v0.1-int8-ov"
model_id = "OpenVINO/mistral-7b-instrcut-v0.1-int8-ov"

#model_id = "OpenVINO/open_llama_3b_v2-int8-ov"
#model_path = "models/open_llama_3b_v2-int8-ov"

#hf_hub.snapshot_download(model_id, local_dir=model_path)

start = time.time()
device = "CPU"
pipe = ov_genai.LLMPipeline(model_path, device)
print(pipe.generate("Ordena el array en python: [2, 1, 5, 8, 23, 9]? muestrame el código", max_length=200))
stop = time.time()

print(f"total: {stop - start}")
