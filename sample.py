import kivy
kivy.require('1.11.1')
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout

class SimpleApp(App):
    def build(self):
        layout = GridLayout(cols=1)

        button1 = Button(text="Push to Record", size_hint_y=None, height=50)
        layout.add_widget(button1)

        button2 = Button(text="Upload File", size_hint_y=None, height=50)
        layout.add_widget(button2)

        button3 = Button(text="Upload Audio", size_hint_y=None, height=50)
        layout.add_widget(button3)

        button4 = Button(text="Library", size_hint_y=None, height=50)
        layout.add_widget(button4)

        return layout

if __name__ == '__main__':
    SimpleApp().run()
