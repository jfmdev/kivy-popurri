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
        mainLayout = BoxLayout(padding=10)
        mainLayout.orientation = 'vertical'

        self.startTimestamp = None
        self.pauseTimestamp = None
        self.status = Status.STOPPED

        self.label = Label(text='0:00:00.000000', font_size='20sp')
        mainLayout.add_widget(self.label)

        buttonsLayout = BoxLayout(padding=10)
        mainLayout.add_widget(buttonsLayout)

        self.stopButton = Button(text='')
        buttonsLayout.add_widget(self.stopButton)
        self.stopButton.bind(on_press=self.stopOrPause)

        self.playButton = Button(text='')
        buttonsLayout.add_widget(self.playButton)
        self.playButton.bind(on_press=self.playOrResume)

        self.updateButtonLabels()

        self.trigger = Clock.create_trigger(self.onTrigger)

        return mainLayout

    def onTrigger(self, *largs):
        if self.status == Status.PLAYING:
            self.label.text = str(datetime.now() - self.startTimestamp)
            self.trigger()

    def playOrResume(self, value):
        if self.status != Status.PLAYING:
            if self.status == Status.STOPPED:
                self.startTimestamp = datetime.now()
            elif self.status == Status.PAUSED:
                self.startTimestamp = datetime.now() - (self.pauseTimestamp - self.startTimestamp)

            self.status = Status.PLAYING
            self.updateButtonLabels()
            self.trigger()


    def stopOrPause(self, value):
        if self.status == Status.PLAYING:
            self.status = Status.PAUSED
            self.pauseTimestamp = datetime.now()
        elif self.status == Status.PAUSED:
            self.status = Status.STOPPED
            self.pauseTimestamp = None
            self.startTimestamp = None
            self.label.text = '0:00:00.000000'

        self.updateButtonLabels()

    def updateButtonLabels(self):
        self.stopButton.text = 'Pause' if self.status == Status.PLAYING else 'Stop'
        self.playButton.text = 'Resume' if self.status == Status.PAUSED else 'Play'

if __name__ == '__main__':
    MyApp().run()

