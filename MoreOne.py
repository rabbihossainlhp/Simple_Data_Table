from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.lang import Builder
#from kivymd.uix.snackbar import Snackbar

Start_string = '''
ScreenManager:
    FirstScreen:


<FirstScreen>:
    MDProgressBar:
        value: 50
        pos_hint: {'center_y': 0.5}
'''


class FirstScreen(Screen):
    pass


class App(MDApp):
    def build(self):
        screen = Screen()
        self.loader_str = Builder.load_string(Start_string)
        screen.add_widget(self.loader_str)
        return screen



App().run()
