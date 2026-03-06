import os
import sys
import traceback
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout

# Создаём папку для логов, если её нет
log_dir = '/storage/emulated/0/пайтон'
if not os.path.exists(log_dir):
    try:
        os.makedirs(log_dir)
    except:
        log_dir = '/sdcard/пайтон'  # запасной путь
        if not os.path.exists(log_dir):
            try:
                os.makedirs(log_dir)
            except:
                log_dir = None

log_file = os.path.join(log_dir, 'log.txt') if log_dir else '/sdcard/log.txt'

def log_error(error_text):
    """Записывает ошибку в файл"""
    try:
        with open(log_file, 'w', encoding='utf-8') as f:
            f.write(f"Ошибка: {error_text}\n")
            f.write("Полный traceback:\n")
            traceback.print_exc(file=f)
    except Exception as e:
        # Если не можем записать в файл, хотя бы в stderr
        print(f"Не удалось записать лог: {e}", file=sys.stderr)

class MyApp(App):
    def build(self):
        try:
            # Твой код здесь
            layout = BoxLayout(orientation='vertical')
            label = Label(text='TEST IS GOOD!', color="red")
            layout.add_widget(label)
            return layout
        except Exception as e:
            # Ловим ошибку и пишем в файл
            log_error(str(e))
            # Показываем пользователю, что пошло не так
            return Label(text=f"Ошибка: {e}\nЛог сохранён в {log_file}")

if __name__ == '__main__':
    try:
        MyApp().run()
    except Exception as e:
        log_error(str(e))
        print(f"Критическая ошибка: {e}", file=sys.stderr)
