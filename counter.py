import kivy
kivy.require('2.3.0') # replace with your current kivy version !

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

class MyApp(App):

    def build(self):
        mainLayout = BoxLayout(padding=10)
        mainLayout.orientation = 'vertical'

        self.count = 0
        self.label = Label(text='Count: 0', font_size='20sp')
        mainLayout.add_widget(self.label)

        buttonsLayout = BoxLayout(padding=10)
        mainLayout.add_widget(buttonsLayout)

        plusButton = Button(text='Increase (+)')
        buttonsLayout.add_widget(plusButton)
        plusButton.bind(on_press=self.increaseCount)

        minusButton = Button(text='Decrease (-)')
        buttonsLayout.add_widget(minusButton)
        minusButton.bind(on_press=self.decreaseCount)

        return mainLayout

    def decreaseCount(self, value):
        self.count = self.count - 1
        self.label.text = 'Count: ' + str(self.count)

    def increaseCount(self, value):
        self.count = self.count + 1
        self.label.text = 'Count: ' + str(self.count)

if __name__ == '__main__':
    MyApp().run()

