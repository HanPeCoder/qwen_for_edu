# 教育大模型微调探究  

应用Qwen预训练模型微调  
使用SFT，建议使用LoRA进行微调  

---
微调数据集[educhat-sft-002-data-osm](https://huggingface.co/datasets/ecnu-icalk/educhat-sft-002-data-osm)  
每条数据由一个存放对话的list和与数据对应的system_prompt组成。list中按照Q，A顺序存放对话。 数据来源为开源数据，使用CleanTool数据清理工具去重。  
数据集下载： 
1. 安装datasets
   ```
   pip install datasets
   ```
2. 运行`data/data_download.py`
   ```shell
   python data/data_download.py
   ```
数据集处理：
  Qwen要求使用json格式的数据
```json
[
  {
    "id": "identity_0",
    "conversations": [
      {
        "from": "user",
        "value": "你好"
      },
      {
        "from": "assistant",
        "value": "我是一个语言模型，我叫通义千问。"
      }
    ]
  }
]
```

运行`data/edu_chat_to_qwen.py`会将educhat-sft-002-data-osm数据按要求处理。  
注意，我们仅使用了educhat-sft-002-data-osm所提供的对话数据，并未使用其所提供的system_prompt。

---  

Qwen微调
参考[Qwen/README_CN](Qwen/README_CN.md)
