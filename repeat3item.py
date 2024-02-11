from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen,ScreenManager
from kivymd.uix.button import MDRoundFlatButton


helper_string = '''
ScreenManager:
    First:
    Second:
    
<First>:
    name: 'first'
    MDFloatingActionButton:
        id: left_float_btn
        icon: 'arrow-left'
        md_bg_color: 1,0,0,1
        pos_hint: {'center_x': 0.4, 'center_y': 0.5}
        # on_release: root.manager.current = 'second'
        
##ACTUALLY IN HERE USED THE DIFFERENT WAY TO SHOWING ANOTHER SCREEN BY PRESSING THAT ARROW KEY
        
        on_release:app.screen_changer()
        
    MDFloatingActionButton:
        icon: 'arrow-right'
        md_bg_color: 0,1,0,1
        pos_hint: {'center_x': 0.6, 'center_y': 0.5}
        # on_press: app.color_changer()
        
<Second>:
    name: 'second'
    MDLabel:
        text: 'Assalamu alaikum'
        font_style: 'H3'
        pos_hint: {'center_x':0.7, 'center_y': 0.6}      
'''
class First(Screen):
    pass
class Second(Screen):
    pass

SM = ScreenManager()
SM.add_widget(First(name = 'first'))
SM.add_widget(Second(name = 'second'))


class DemoApp(MDApp):
    def build(self):
        screen = Screen()
        self.loader = Builder.load_string(helper_string)
        screen.add_widget(self.loader)
        new_btn = MDRoundFlatButton(
            icon = 'language-python',
            pos_hint = {'center_x':0.6, 'center_y':0.14},
        )
        self.loader.get_screen('second').add_widget(new_btn)
        return screen

    def color_changer(self):
        if self.loader.get_screen('first').ids.left_arrow_btn.md_bg_color == self.theme_cls.primary_color:
            self.loader.get_screen('first').ids.left_arrow_btn.md_bg_color(0,1,0,1)
        else:
            self.loader.get_screen('first').ids.left_arrow_btn.md_bg_color = self.theme_cls.primary_color

    def screen_changer(self):
        self.loader.get_screen('second').manager.current = 'second'
DemoApp().run()