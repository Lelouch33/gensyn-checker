# 📊 Gensyn "Total Wins" Tracker Bot

Отслеживание ваших ID с автоматической отправкой уведомлений в Telegram 💬

Track your IDs with auto Telegram updates 💬

## 🚀 Возможности | Features

🔍 Проверка ID из файла peer_id.txt

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
pip install eth-abi eth-utils requests
```
```bash
nano peer_id.txt
```
вставьте Node ID (указано рядом с именем в квадратных скобках и начинается на "Qm"), каждый с новой строки

Создайте бота через ```@BotFather``` затем зайдите в него и нажмите start

Получите TOKEN бота

Получите ваш CHAT_ID через ```@userinfobot```

Отредактируйте переменные в начале скрипта:

```
BOT_TOKEN = "ВАШ_ТОКЕН"

CHAT_ID = "ВАШ_CHAT_ID"

SEND_INTERVAL_SECONDS = 3000  # интервал в секундах
```
## ▶️ Запуск
```bash
python3 gensyn-perserID.py
```
будут отображаться последние 10 символов Node ID для комфортного восприятия

![image](https://github.com/user-attachments/assets/7a9c28a4-86f2-4502-b78b-77c3d7eb6027)










