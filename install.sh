#!/bin/bash

echo "╔══════════════════════════════════════════════╗"
echo "║     TELEGRAM MAILER BOT - УСТАНОВКА         ║"
echo "╚══════════════════════════════════════════════╝"

# Цвета для вывода
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
CYAN='\033[0;36m'
NC='\033[0m'

echo -e "${CYAN}[1/5] Обновление Termux...${NC}"
pkg update -y && pkg upgrade -y

echo -e "${CYAN}[2/5] Установка Python и Git...${NC}"
pkg install python git -y

echo -e "${CYAN}[3/5] Установка библиотек...${NC}"
pip install telethon colorama

echo -e "${CYAN}[4/5] Скачивание бота...${NC}"
git clone https://github.com/wetnet-beep/telegram-mailer-bot.git
cd telegram-mailer-bot

echo -e "${CYAN}[5/5] Настройка прав...${NC}"
chmod +x bot.py
chmod +x start.sh

echo -e "${GREEN}✅ УСТАНОВКА ЗАВЕРШЕНА!${NC}"
echo ""
echo -e "${YELLOW}🚀 Для запуска бота:${NC}"
echo -e "   ${CYAN}cd telegram-mailer-bot${NC}"
echo -e "   ${CYAN}python bot.py${NC}"
echo ""
echo -e "${YELLOW}📱 Или используйте:${NC}"
echo -e "   ${CYAN}./start.sh${NC}"
echo ""
echo -e "${YELLOW}🔧 При первом запуске понадобится:${NC}"
echo "   1. API ID и Hash с my.telegram.org"
echo "   2. Ваш номер телефона Telegram"
echo "   3. Код из приложения Telegram"
echo ""

read -p "Запустить бота сейчас? (y/n): " -n 1 -r
echo
if [[ $REPLY =~ ^[Yy]$ ]]; then
    python bot.py
fi
