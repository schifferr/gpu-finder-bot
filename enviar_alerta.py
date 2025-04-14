import telebot

TOKEN = "7925110772:AAGWJIpCsDWBt8rsHz4M_W8HKBERAJgvlqc"
CHANNEL_ID = "-100595595499"

bot = telebot.TeleBot(TOKEN)

def enviar_alerta_placa(modelo, preco, loja, link):
    mensagem = f"**[ALERTA] {modelo} por R$ {preco} na {loja}!**\n{link}"
    bot.send_message(CHANNEL_ID, mensagem, parse_mode="Markdown")

if __name__ == "__main__":
    enviar_alerta_placa("RTX 3080", "3.999", "Pichau", "https://www.pichau.com.br/rtx3080")
