__author__ = 'Adroso'

from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window


class currencyConverterApp(App):

    def build(self):
        Window.size = 350, 700
        self.title = "Foreign Exchange Calculator"
        self.root = Builder.load_file('gui.kv')
        return self.root


if __name__ == '__main__':
    currencyConverterApp().run()

