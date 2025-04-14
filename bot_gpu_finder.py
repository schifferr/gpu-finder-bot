
import telebot
from fastapi import FastAPI, Request
import uvicorn

TOKEN = "7925110772:AAGWJIpCsDWBt8rsHz4M_W8HKBERAJgvlqc"
bot = telebot.TeleBot(TOKEN)
app = FastAPI()

@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id, "Bem-vindo ao GPU Finder! Use /buscar para procurar GPUs.")

@bot.message_handler(commands=["buscar"])
def buscar(message):
    bot.send_message(message.chat.id, "Buscando as melhores ofertas de placas de vídeo...")

@app.get("/")
async def root():
    return {{"message": "GPU Finder Bot"}}

@app.post("/webhook/" + TOKEN)
async def webhook(request: Request):
    json_str = await request.body()
    update = telebot.types.Update.de_json(json_str.decode("utf-8"))
    bot.process_new_updates([update])
    return {{"ok": True}}

if __name__ == "__main__":
    uvicorn.run("bot_gpu_finder:app", host="0.0.0.0", port=10000)
