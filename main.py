import telebot
import requests

BOT_TOKEN = "8621315025:AAGFgcN-4j8EceBuvvuCNdogEbv5qGPoRWw"
GEMINI_API_KEY = "AQ.Ab8RN6Kau4-kVZ-Wblzagiwc28uGiHUxg07qa7M1QflZIbqUuA"

bot = telebot.TeleBot(BOT_TOKEN)

def ask_gemini(text):
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={GEMINI_API_KEY}"
    data = {"contents": [{"parts": [{"text": text}]}]}
    response = requests.post(url, json=data)
    result = response.json()
    if "candidates" in result:
        return result["candidates"][0]["content"]["parts"][0]["text"]
    else:
        return str(result)

@bot.message_handler(func=lambda msg: True)
def handle(msg):
    try:
        reply = ask_gemini(msg.text)
        bot.reply_to(msg, reply)
    except Exception as e:
        bot.reply_to(msg, f"خطا: {str(e)}")

bot.infinity_polling()
