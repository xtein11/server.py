from flask import Flask, request
import telegram

# === ТВОЙ ТОКЕН ===
TOKEN = "7960236842:AAHh8VL9Q9cUVa_H1rlDqWHRtoDE2iCsC2Q"

# создаём бота
bot = telegram.Bot(token=TOKEN)

# создаём Flask сервер
app = Flask(__name__)

# проверка, что сервер работает
@app.route('/')
def home():
    return "Бот работает 🚀"

# обработчик сообщений от Telegram
@app.route(f'/{TOKEN}', methods=['POST'])
def webhook():
    update = telegram.Update.de_json(request.get_json(force=True), bot)

    # получаем чат и текст
    chat_id = update.message.chat.id
    text = update.message.text

    # ответ пользователю
    bot.sendMessage(chat_id=chat_id, text=f"Ты написал: {text}")

    return "ok"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

