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

Метрика ```total votes``` показывает сколько раз конкретный EOA (адрес пользователя) проголосовал за кого-либо в рамках всех прошедших раундов.

![image](https://github.com/user-attachments/assets/bdbd96a7-b14b-4c0d-aee9-89c977036363)











