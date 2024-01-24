import telebot
import moondream
from PIL import Image
from threading import Thread 

bot = telebot.TeleBot("<api_token>")

vision_encoder = moondream.VisionEncoder(model_path)  
text_model = moondream.TextModel(model_path)

@bot.message_handler(content_types=['photo'])
def handle_image(message):

    file_id = message.photo[-1].file_id
    file_path = bot.get_file(file_id).file_path
    
    image = Image.open(bot.download_file(file_path))
    image_embeds = vision_encoder(image)
    
    streamer = moondream.TextIteratorStreamer(text_model.tokenizer)

    @bot.message_handler(func=lambda m: True)
    def handle_question(message):

        question = message.text

        def generate():
            return text_model.answer_question(
                image_embeds, question, streamer=streamer)

        thread = Thread(target=generate)
        thread.start()

        for text in streamer:
            bot.send_message(message.chat.id, text)

bot.polling()
