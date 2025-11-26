"""

from openai import OpenAI
import os,requests
player1 = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
player2 = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

player1_input = input("Введи свой запрос: ")
player1_store = input("Сохранить ответ ИИ ? (да - 1 или 0): ")

if player1_store == 1:
  store=True
else:
   store = False

response =player1.responses.create(
model="gpt-5-nano",
input=player1_input,
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
    
#files = player1.files.list()
#if len(files.data) == 0 : print(f"ФАЙЛОВ НЕТ! {len(files.data)}")

#else:
#   for f in files.data:
#        print(f.id, f.filename, f.purpose)

if player1_store ==1:
  print("Ответ сохранен!")
else:print("Ответ не сохранен!")


"""




import base64
from openai import OpenAI
client = OpenAI()

img = client.images.generate(
    model="gpt-image-1",
    prompt="A cute baby sea otter",
    n=1,
    size="1024x1024"
)

image_bytes = base64.b64decode(img.data[0].b64_json)
with open("output.png", "wb") as f:
    f.write(image_bytes)