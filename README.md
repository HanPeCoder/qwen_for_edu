# Exploration of Fine-Tuning Educational Large Models

Fine-tuning with the Qwen Pretrained Model
Using SFT, with a recommendation to use LoRA for fine-tuning

---
Fine-tuning Dataset: [educhat-sft-002-data-osm](https://huggingface.co/datasets/ecnu-icalk/educhat-sft-002-data-osm)  
Each entry contains a list of dialogues and a corresponding system prompt. The list stores dialogues in a Q&A order. The dataset comes from open-source data, cleaned and deduplicated using the CleanTool.  
Dataset download:  
1. Install datasets
   ```bash
   pip install datasets
   ```
2. Run `data/data_download.py` to download the dataset, which will be saved in the data folder. You can modify the cache path using the `cache_dir`.
   ```bash
   python data/data_download.py
   ```
Dataset processing:
Qwen requires data in JSON format.
```json
[
  {
    "id": "identity_0",
    "conversations": [
      {
        "from": "user",
        "value": "Hello"
      },
      {
        "from": "assistant",
        "value": "I am a language model, and my name is Tongyi Qianwen."
      }
    ]
  }
]
```
Running data/edu_chat_to_qwen.py will process the educhat-sft-002-data-osm dataset as required.
Note that we only use the conversation data provided by educhat-sft-002-data-osm and do not use the provided `system_prompt`.

---
Qwen Fine-Tuning  
```bash
git clone git@github.com:QwenLM/Qwen.git
```
For detailed fine-tuning instructions, refer to [Qwen](https://github.com/QwenLM/Qwen)

---
Disclaimer: This project is for educational purposes only and does not involve any commercial activities.
