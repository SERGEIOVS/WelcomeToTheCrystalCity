import pyttsx3

# Инициализация движка
engine = pyttsx3.init()

# Получаем доступные голоса
voices = engine.getProperty('voices')
for i, voice in enumerate(voices):
    print(f"Voice {i}:")
    print(f"  ID: {voice.id}")
    print(f"  Name: {voice.name}")
    print(f"  Languages: {voice.languages}")
    print(f"  Gender: {voice.gender}")
    print("-----------")


# Выбираем голос
engine.setProperty('voice', voices[0].id)  # проверь индекс по выводу

# Настройка громкости (0.0 — 1.0)
engine.setProperty('volume', 1.0)

# Настройка скорости речи
engine.setProperty('rate', 200)

# Текст для озвучки
engine.say("This is my first language speaking test using the Python lang.")

# Запуск
engine.runAndWait()
