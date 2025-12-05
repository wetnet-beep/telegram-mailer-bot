#!/usr/bin/env python3
# -*- coding: utf-8 -*-

print("="*60)
print("        TELEGRAM MAILER BOT v5.0")
print("        Автор: @wetnet-beep")
print("="*60)
print("\nЗагрузка...")

import os
import sys
import json
import time
import asyncio
from telethon import TelegramClient
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty

class SimpleTelegramBot:
    def __init__(self):
        self.client = None
        self.me = None
        self.chats = []
    
    async def setup(self):
        print("\n" + "="*60)
        print("НАСТРОЙКА АККАУНТА")
        print("="*60)
        print("\n1. Получите API на https://my.telegram.org")
        print("2. Создайте приложение")
        print("3. Скопируйте API ID и Hash\n")
        
        api_id = input("Введите API ID: ")
        api_hash = input("Введите API Hash: ")
        phone = input("Введите номер телефона (+79991234567): ")
        
        self.client = TelegramClient("user_session", int(api_id), api_hash)
        
        try:
            await self.client.connect()
            
            if not await self.client.is_user_authorized():
                print("\n📲 Отправка кода на Telegram...")
                await self.client.send_code_request(phone)
                code = input("Введите код из Telegram: ")
                await self.client.sign_in(phone, code)
            
            self.me = await self.client.get_me()
            print(f"\n✅ УСПЕШНЫЙ ВХОД!")
            print(f"👤 Имя: {self.me.first_name}")
            if self.me.username:
                print(f"📱 Username: @{self.me.username}")
            
            return True
            
        except Exception as e:
            print(f"\n❌ Ошибка: {e}")
            return False
    
    async def load_chats(self):
        print("\n📋 Загрузка ваших чатов...")
        try:
            result = await self.client(GetDialogsRequest(
                offset_date=None,
                offset_id=0,
                offset_peer=InputPeerEmpty(),
                limit=100,
                hash=0
            ))
            
            self.chats = []
            for chat in result.chats:
                self.chats.append({
                    "id": chat.id,
                    "title": getattr(chat, 'title', ''),
                    "username": getattr(chat, 'username', '')
                })
            
            print(f"✅ Загружено: {len(self.chats)} чатов")
            
        except Exception as e:
            print(f"❌ Ошибка загрузки: {e}")
    
    def show_menu(self):
        print("\n" + "="*60)
        print("ГЛАВНОЕ МЕНЮ")
        print("="*60)
        print("[1] 📋 Показать мои чаты")
        print("[2] 📤 Отправить сообщение")
        print("[3] 🚀 Начать рассылку")
        print("[4] 📊 Статистика")
        print("[5] ⚙️ Настройки")
        print("[x] 🚪 Выход")
        print("="*60)
    
    async def show_chats(self):
        if not self.chats:
            await self.load_chats()
        
        print(f"\n📱 ВАШИ ЧАТЫ ({len(self.chats)}):")
        for i, chat in enumerate(self.chats[:20], 1):
            name = chat["title"] or chat["username"] or f"Чат {chat['id']}"
            print(f"{i}. {name[:40]}")
        
        if len(self.chats) > 20:
            print(f"... и еще {len(self.chats) - 20} чатов")
    
    async def send_message(self):
        await self.show_chats()
        
        try:
            num = int(input("\nВыберите номер чата: "))
            if 1 <= num <= len(self.chats):
                chat = self.chats[num-1]
                message = input("Введите текст сообщения: ")
                
                print(f"Отправка в {chat['title']}...")
                await self.client.send_message(chat["id"], message)
                print("✅ Сообщение отправлено!")
            else:
                print("❌ Неверный номер")
        except:
            print("❌ Ошибка ввода")
    
    async def start_mailing(self):
        await self.show_chats()
        
        print("\n🎯 НАСТРОЙКА РАССЫЛКИ")
        chats_input = input("Введите номера чатов через запятую (1,2,3): ")
        message = input("Текст для рассылки: ")
        delay = float(input("Задержка между сообщениями (секунд): "))
        
        try:
            chat_nums = [int(n.strip()) for n in chats_input.split(',')]
            
            print(f"\n⚠️  Начинаю рассылку в {len(chat_nums)} чатов...")
            
            for num in chat_nums:
                if 1 <= num <= len(self.chats):
                    chat = self.chats[num-1]
                    try:
                        await self.client.send_message(chat["id"], message)
                        print(f"✅ Отправлено в {chat['title']}")
                        await asyncio.sleep(delay)
                    except Exception as e:
                        print(f"❌ Ошибка в {chat['title']}: {e}")
            
            print("\n✅ Рассылка завершена!")
            
        except:
            print("❌ Ошибка ввода")
    
    async def run(self):
        print("\n" + "⭐"*60)
        print("TELEGRAM MAILER BOT v5.0")
        print("Быстрая рассылка сообщений")
        print("⭐"*60)
        
        if not await self.setup():
            return
        
        while True:
            self.show_menu()
            choice = input("\nВыберите действие: ").lower()
            
            if choice == "1":
                await self.show_chats()
            elif choice == "2":
                await self.send_message()
            elif choice == "3":
                await self.start_mailing()
            elif choice == "4":
                print("\n📊 Статистика:")
                print(f"• Чатов загружено: {len(self.chats)}")
                print(f"• Аккаунт: {self.me.first_name}")
            elif choice == "5":
                print("\n⚙️ Настройки в разработке...")
            elif choice == "x":
                print("\n👋 До свидания!")
                break
            
            input("\nНажмите Enter чтобы продолжить...")

async def main():
    bot = SimpleTelegramBot()
    await bot.run()

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n\n👋 Программа завершена")
