# 📊 Gensyn Leaderboard Tracker Bot

Отслеживание ваших ID и никнеймов в лидерборде Gensyn с автоматической отправкой уведомлений в Telegram 💬

Track your IDs and nicknames in the Gensyn leaderboard with auto Telegram updates 💬

## 🚀 Возможности | Features

🔍 Проверка ID и nickname'ов из файла id.txt

⏱ Автоматические запросы с интервалом в секундах из настроек

📩 Уведомления в Telegram

## ⚙ Настройка

```bash
git clone https://github.com/noderguru/gensyn-cheker.git
cd gensyn-cheker
```
```bash
tmux new -s gensyn-cheker
```

```bash
python3 -m venv venv
source venv/bin/activate
```
```bash
pip install requests
```
```bash
nano id.txt
```
вставьте имя вашего воркера (три слова при старте ноды) ```или``` id ноды (указано рядом с именем в квадратных скобках и начинается на "Qm"), каждый с новой строки

### Если надо получать уведомления в Телеграм:

Создайте бота через ```@BotFather``` затем зайдите в него и нажмите start

Получите TOKEN бота

Получите ваш CHAT_ID через ```@userinfobot```

Отредактируйте переменные в начале скрипта:

```
SEND_TELEGRAM = True/False

TELEGRAM_BOT_TOKEN = "ВАШ_ТОКЕН"

TELEGRAM_CHAT_ID = "ВАШ_CHAT_ID"

SEND_INTERVAL_SECONDS = 300  # интервал в секундах
```
## ▶️ Запуск
```bash
python3 gensyn-perserID_leaderboard.py
```
![image](https://github.com/user-attachments/assets/556d8ff8-b5d2-4881-afa5-0406f7f07b12)

## Если телега не используется то результат будет выводится в консоль
![image](https://github.com/user-attachments/assets/8a478783-0256-4a40-9c39-e9c04bad7c67)










