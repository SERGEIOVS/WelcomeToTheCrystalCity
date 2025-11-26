import pyttsx3

my_text = [

"В современном мире информация распространяется с невероятной скоростью.",
"Каждое новое открытие, каждый технологический прогресс меняют привычный уклад жизни и влияют на то, как люди взаимодействуют друг с другом.",
"Интернет стал основным источником знаний и коммуникации, объединяя миллионы пользователей по всему миру и создавая глобальное сообщество."]

selected_voice = 2
voice_volume   = 1.0
voice_rate     = 200

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
engine.setProperty('voice', voices[selected_voice].id)  # проверь индекс по выводу

# Настройка громкости (0.0 — 1.0)
engine.setProperty('volume', 1.0)

# Настройка скорости речи
engine.setProperty('rate', 200)

# Текст для озвучки
engine.say(my_text[0])

# Запуск
engine.runAndWait()
