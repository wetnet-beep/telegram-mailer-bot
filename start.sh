#!/bin/bash

cd "$(dirname "$0")"

echo "Запуск Telegram Mailer Bot..."
echo "Версия: 5.0"
echo "Автор: @wetnet-beep"
echo ""

# Проверка Python
if ! command -v python3 &> /dev/null; then
    echo "❌ Python3 не установлен"
    echo "Установите: pkg install python"
    exit 1
fi

# Проверка зависимостей
if ! python3 -c "import telethon" 2>/dev/null; then
    echo "📦 Установка библиотек..."
    pip install telethon colorama
fi

# Запуск бота
python3 bot.py
