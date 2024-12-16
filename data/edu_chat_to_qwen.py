from datasets import load_dataset
import json
import os

ds = load_dataset("ecnu-icalk/educhat-sft-002-data-osm", cache_dir='data')
ds_train = ds['train']
ds_ls = []

for i, data in enumerate(ds_train):
    data_row = {}   
    d, p = data['data'], data['system_prompt']
    data_row['id'] = f'identity_{i}'
    data_row['conversations'] = [{'from': "user", "value": d[0]}, {"from":"assistant", 'value':d[1]}]
    ds_ls.append(data_row)
    if i == 10000:
        break

if not os.path.exists("data/edu_to_qwen/data.json"):
    os.makedirs('data/edu_to_qwen')

with open("data/edu_to_qwen/data.json", "w", encoding="utf-8") as json_file:
    json.dump(ds_ls, json_file, ensure_ascii=False, indent=4)

print("数据已写入 data.json 文件")
    