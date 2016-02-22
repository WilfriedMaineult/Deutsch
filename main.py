# -*- coding: utf-8 -*-

from kivy.app import App
from kivy.uix.widget import Widget


class Assimil(Widget):
    pass


class AssimilApp(App):
    def build(self):
        return Assimil()


if __name__ == '__main__':
    AssimilApp().run()