from datasets import load_dataset


ds = load_dataset("ecnu-icalk/educhat-sft-002-data-osm", cache_dir='data')
ds_train = ds['train']

for i, data in enumerate(ds_train):
    print(data.keys())
    d, p = data['data'], data['system_prompt']
