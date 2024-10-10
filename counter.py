import kivy
kivy.require('2.3.0') # replace with your current kivy version !

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

class MyApp(App):
    def build(self):
        main_layout = BoxLayout(padding=10)
        main_layout.orientation = 'vertical'

        self.count = 0
        self.label = Label(text='Count: 0', font_size='20sp')
        main_layout.add_widget(self.label)

        buttons_layout = BoxLayout(padding=10)
        main_layout.add_widget(buttons_layout)

        plus_button = Button(text='Increase (+)')
        buttons_layout.add_widget(plus_button)
        plus_button.bind(on_press=self.increase_count)

        minus_button = Button(text='Decrease (-)')
        buttons_layout.add_widget(minus_button)
        minus_button.bind(on_press=self.decrease_count)

        return main_layout

    def decrease_count(self, value):
        self.count = self.count - 1
        self.label.text = 'Count: ' + str(self.count)

    def increase_count(self, value):
        self.count = self.count + 1
        self.label.text = 'Count: ' + str(self.count)

if __name__ == '__main__':
    MyApp().run()
