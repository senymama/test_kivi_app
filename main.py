from kivy.app import App

from kivy.uix.button import Button
from kivy.uix.label import Label

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget

from kivy.config import Config

Config.set('graphics', 'resizable', 0)
Config.set('graphics', 'width', 400)
Config.set('graphics', 'height', 500)

buttons = ['7', '8', '9', 'X',
           '4', '5', '6', '-',
           '1', '2', '3', '+',
           None, '0', '.', '=']


class MyCalculator(App):
    def update_lbl(self):
        self.lbl.text = self.text

    def but_processing(self, instance):
        if self.text == '0':
            self.text = ''
        if instance.text == '=':
            if self.text != '':
                try:
                    self.text = str(eval(self.text.replace('X', '*')))
                    self.update_lbl()
                    self.text = '0'
                except SyntaxError:
                    self.update_lbl()
        else:
            self.text += str(instance.text)
            self.update_lbl()

    def build(self):
        self.text = '0'

        bl = BoxLayout(orientation='vertical', padding=20)
        gl = GridLayout(cols=4, spacing=5, size_hint=(1, .7))

        self.lbl = Label(text='0', font_size=40, halign='right', size_hint=(1, .3), text_size=(400 - 40, 500 * .3 - 40))

        bl.add_widget(self.lbl)
        bl.add_widget(gl)

        for but in buttons:
            if not but is None:
                gl.add_widget(Button(text=but, on_press=self.but_processing))
            else:
                gl.add_widget(Widget())

        return bl


if __name__ == '__main__':
    MyCalculator().run()
