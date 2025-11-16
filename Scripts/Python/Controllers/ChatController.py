#simple chat controller
import pygame as pg

chat_triggers = {
 
"bad_words" : ["нахер","придурок", "жопа","дебил","даун","сука","кретин","наркотик"],

"spam"      : ["переходи", "ссылка:", "подпишись","подпишись на канал и поставь лайк"],

"threats"   :{
            
              "phisical" : ["умри!","чтоб ты сдох,сука!", "Убью нахер!","умри,блядь!"] ,
              "digital"  : ["Я тебя взломаю!", "я знаю твой пароль!", "украду пароль!","по айпи вычислю!"]
            
            }

}



msgs = {

"player1": {
            
            "support_msgs":[
            
            "у меня не работает учетка", "меня оскорбил игрок", "мой аккаунт взломали", "у меня украли предмет", "меня не пускают в мой дом с приватом"
            
            ],

            "chat_msgs":[
            
            "у меня не работает учетка", "меня оскорбил игрок", "мой аккаунт взломали", "у меня украли предмет", "меня не пускают в мой дом с приватом"
            
            ],

            "private_msgs":[
            
            "у меня не работает учетка", "меня оскорбил игрок", "мой аккаунт взломали", "у меня украли предмет", "меня не пускают в мой дом с приватом"
            
            ]
            
            },

"player2": {
            
            "support_msgs":[
            
            "у меня не работает учетка", "меня оскорбил игрок", "мой аккаунт взломали", "у меня украли предмет", "меня не пускают в мой дом с приватом"
            
            ],

            "chat_msgs":[
            
            "у меня не работает учетка", "меня оскорбил игрок", "мой аккаунт взломали", "у меня украли предмет", "меня не пускают в мой дом с приватом"
            
            ],

            "private_msgs":[
            
            "у меня не работает учетка", "меня оскорбил игрок", "мой аккаунт взломали", "у меня украли предмет", "меня не пускают в мой дом с приватом"
            
            ]
            
            }

}



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
    

    print("регистрация")
    print("авторизация")
    print("техподдержка")
    
    action = input("меню:")
    
    if action == "регистрация" : register()
    if action == "авторизация" : login()
    if action == "техподдержка" : support()





#функция вызывается при проверке чата на запрещенку
