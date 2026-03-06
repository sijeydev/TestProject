import os
import sys
import traceback
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout

# Пробуем разные пути
possible_paths = [
    '/sdcard/log.txt',
    '/storage/emulated/0/log.txt',
    '/storage/emulated/0/пайтон/log.txt',
    '/data/data/org.example.myapp/files/log.txt'  # внутреннее хранилище приложения
]

log_file = None
for path in possible_paths:
    try:
        # Проверяем, можем ли писать
        with open(path, 'w') as f:
            f.write('Тест записи\n')
        log_file = path
        break
    except:
        continue

def log_error(error_text):
    if not log_file:
        return
    try:
        with open(log_file, 'a', encoding='utf-8') as f:
            f.write(f"\n=== {error_text} ===\n")
            traceback.print_exc(file=f)
    except:
        pass

# Пишем сразу при запуске
if log_file:
    with open(log_file, 'a') as f:
        f.write("Приложение запущено\n")

class MyApp(App):
    def build(self):
        if log_file:
            with open(log_file, 'a') as f:
                f.write("build() вызван\n")
        try:
            layout = BoxLayout(orientation='vertical')
            label = Label(text='TEST IS GOOD!', color="red")
            layout.add_widget(label)
            return layout
        except Exception as e:
            log_error(str(e))
            return Label(text="Ошибка")

if __name__ == '__main__':
    if log_file:
        with open(log_file, 'a') as f:
            f.write("__main__ запущен\n")
    try:
        MyApp().run()
    except Exception as e:
        log_error(str(e))
