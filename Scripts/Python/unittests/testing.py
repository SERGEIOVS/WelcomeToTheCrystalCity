from openai import OpenAI
client = OpenAI(
  api_key="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"
)

user_input = input("Введи свой запрос: ")
user_store = input("Сохранить ответ ИИ ? (да - 1 или 0): ")
if user_store == "1":
  store=True
else:user_store = False

response = client.responses.create(
model="gpt-5-nano",
input=user_input,
store = user_store

)

print(response.output_text)
if user_store ==1:
  print("Ответ сохранен!")
else:print("Ответ не сохранен!")