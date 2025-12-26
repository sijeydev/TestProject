from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout

class MyApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        label = Label(text='TEST IS GOOD!', color="red")
        layout.add_widget(label)
        return layout

if __name__ == '__main__':
    MyApp().run()