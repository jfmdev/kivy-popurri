import kivy
kivy.require('2.3.0') # replace with your current kivy version !

from kivy.app import App
from kivy.clock import Clock
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

from datetime import datetime
from datetime import timedelta
from enum import Enum

class Status(Enum):
    STOPPED = 1
    PAUSED = 2
    PLAYING = 3

class MyApp(App):
    def build(self):
        main_layout = BoxLayout(padding=10)
        main_layout.orientation = 'vertical'

        self.start_timestamp = None
        self.pause_timestamp = None
        self.status = Status.STOPPED

        self.label = Label(text='0:00:00.000000', font_size='20sp')
        main_layout.add_widget(self.label)

        buttons_layout = BoxLayout(padding=10)
        main_layout.add_widget(buttons_layout)

        self.stop_button = Button(text='')
        buttons_layout.add_widget(self.stop_button)
        self.stop_button.bind(on_press=self.stop_or_pause)

        self.play_button = Button(text='')
        buttons_layout.add_widget(self.play_button)
        self.play_button.bind(on_press=self.play_or_resume)

        self.update_button_labels()

        self.trigger = Clock.create_trigger(self.on_trigger)

        return main_layout

    def on_trigger(self, *largs):
        if self.status == Status.PLAYING:
            self.label.text = str(datetime.now() - self.start_timestamp)
            self.trigger()

    def play_or_resume(self, value):
        if self.status != Status.PLAYING:
            if self.status == Status.STOPPED:
                self.start_timestamp = datetime.now()
            elif self.status == Status.PAUSED:
                self.start_timestamp = datetime.now() - (self.pause_timestamp - self.start_timestamp)

            self.status = Status.PLAYING
            self.update_button_labels()
            self.trigger()


    def stop_or_pause(self, value):
        if self.status == Status.PLAYING:
            self.status = Status.PAUSED
            self.pause_timestamp = datetime.now()
        elif self.status == Status.PAUSED:
            self.status = Status.STOPPED
            self.pause_timestamp = None
            self.start_timestamp = None
            self.label.text = '0:00:00.000000'

        self.update_button_labels()

    def update_button_labels(self):
        self.stop_button.text = 'Pause' if self.status == Status.PLAYING else 'Stop'
        self.play_button.text = 'Resume' if self.status == Status.PAUSED else 'Play'

if __name__ == '__main__':
    MyApp().run()
