#simple chat controller
import pygame as pg
import sys
from pathlib import Path



# путь к Scripts/Python
sys.path.append(str(Path(__file__).resolve().parent))

from  Controllers.Units import Enemies_list, players_list  # теперь можно импортировать напрямую



chat_triggers = {
 
"bad_words" : ["нахер","придурок", "жопа","дебил","даун","сука","кретин","наркотик"],

"spam"      : {"переходи", "ссылка:", "подпишись","подпишись на канал и поставь лайк"},

"threats"   : {
            
              "phisical" : ["умри!","чтоб ты сдох,сука!", "Убью нахер!","умри,блядь!"] ,
              "digital"  : ["Я тебя взломаю!", "я знаю твой пароль!", "украду пароль!","по айпи вычислю!"]
            
            }
            
            }



msgs = {}



def chat_moderation(player,msg):
    for player,sections in msgs.items():
        for msg in sections["chat_msgs"]:

                for word in chat_triggers["bad_words"]:
                    if word in msg:
                        print(f"{player} : зафиксировано ругательство!'{word}'")
            
                for spam in chat_triggers["spam"]:
                    if spam in msg:
                        print(f"{player} : зафиксирован спам!'{spam}'")

                for threat in chat_triggers["threats"]["phisical"]:
                    if threat in msg:
                        print(f"{player} : зафиксирована угроза!'{threat}'")
                
                for threat in chat_triggers["threats"]["digital"]:
                    if threat in msg:
                        print(f"{player} : зафиксирована угроза!'{threat}'")



def login():
        
        #отправитель
        sender    = input("Enter your nickname: ")
        
        #получатель
        recipient = input("Enter the  nickname: ")
   
        #если есть - отправляем сообщение игрока
        if sender in msgs:
            msg = input("Enter your message: ")
            msgs[sender]["chat_msgs"].append(msg)
            chat_moderation(sender,msg)
    
        #если нет - информируем об отсутствии игрока
        if sender not in msgs:
            print("Такого игрока нет.")
            return
        
        #если нет - информируем об отсутствии игрока
        if recipient not in msgs:
            print("Такого игрока нет.")
            return


def register():
        
        #отправитель
        for i in range(players_list):
            player = input("Enter your nickname: ")

            #если есть - отправляем сообщение игрока
            if player not in msgs:
                
                msg = input("Enter your message: ")
                msgs[player] = {

                "support_msgs" : [],
                "chat_msgs"    : [],
                "private_msgs" : [],

                }

def menu():
    register = "регистрация"
    login    = "авторизация"
    support  = "техподдержка"
    if action == "регистрация" : register()
    if action == "авторизация" : login()
    if action == "техподдержка" : support()    

    print("регистрация")
    print("авторизация")
    print("техподдержка")
    
    action = input("меню:")