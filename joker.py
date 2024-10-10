import kivy
kivy.require('2.3.0') # replace with your current kivy version !

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

import requests
import threading

class MyApp(App):
    def build(self):
        main_layout = BoxLayout(padding=10)
        main_layout.orientation = 'vertical'

        self.label = Label(text='Press the button to get a joke', font_size='20sp')
        main_layout.add_widget(self.label)

        self.fetch_button = Button(text='Tell me a joke')
        self.fetch_button.bind(on_press=self.fetch_joke)
        main_layout.add_widget(self.fetch_button)

        return main_layout

    def fetch_joke(self, value):
        self.fetch_button.text = 'Getting joke...'
        self.fetch_button.disabled = True

        threading.Thread(target=self.joke_request).start()

    def joke_request(self):
        result = requests.get('https://v2.jokeapi.dev/joke/Any?type=single')
        json_data = result.json()
        print(json_data)
        self.label.text = json_data['joke']

        self.fetch_button.text = 'Tell me another joke'
        self.fetch_button.disabled = False

if __name__ == '__main__':
    MyApp().run()
