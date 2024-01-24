# Moondream Telegram Bot

This bot utilizes the Moondream model to generate text responses to questions based on images sent to it. 

## Usage  

1. `pip install -r requirements.txt`  
2. Add your Telegram bot API token to `bot.py`
3. `python bot.py`  
4. Send an image to the bot and ask a question

## Requirements

requirements.txt:
```
telebot==0.1.5

moondream==0.1.0
transformers==4.25.1
huggingface-hub==0.11.1

pillow==9.3.0

torch==1.13.1
```


The core requirements are:  

- `telebot` - Telegram Bot API wrapper  
- `moondream` - Main model for text generation  
- Image and model libraries like PyTorch, Transformers, etc  

Feel free to tweak the versions as needed.
