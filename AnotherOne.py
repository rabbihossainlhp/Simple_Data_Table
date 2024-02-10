from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.lang import Builder

strings = '''
ScreenManager:
    HelloScr:

<HelloScr>:
    name: 'HelS'
    MDLabel:
        text: 'HEloo fello'
        font_style: 'H2'
        halign: 'center'
        pos_hint: {'center_y': 0.85, 'center_x': 0.5}
'''


class HelloScr(Screen):
    pass


helsm = ScreenManager()
helsm.add_widget(HelloScr(name='Hels'))


class Mainapp(MDApp):
    def build(self):
        scre = Screen()
        loaderS = Builder.load_string(strings)
        scre.add_widget(loaderS)
        return scre


Mainapp().run()