from openai import OpenAI
import os,requests
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

user_input = input("Введи свой запрос: ")
user_store = input("Сохранить ответ ИИ ? (да - 1 или 0): ")

if user_store == 1:
  store=True
else:
   store = False

response = client.responses.create(
model="gpt-5-nano",
input=user_input,
store = store  

)
print(response.output_text)
print()
print()
print()
print()

# Получаем список организаций, связанных с ключом
#----------------------------------------------------

#---------------------------------
    
#files = client.files.list()
#if len(files.data) == 0 : print(f"ФАЙЛОВ НЕТ! {len(files.data)}")

#else:
#   for f in files.data:
#        print(f.id, f.filename, f.purpose)

if user_store ==1:
  print("Ответ сохранен!")
else:print("Ответ не сохранен!")
