from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen,ScreenManager
from kivy.lang import Builder
from kivymd.uix.imagelist import SmartTileWithStar

class MyTile(SmartTileWithStar):
    pass

strt_String = '''
ScreenManager:
    FirstScr:
    

<FirstScr>:
    name: 'First'
    ScrollView:
        MDGridLayout:
            cols:2
            padding: dp(5),dp(5)
            spacing: dp(10)
            
            MyTile:
                stars:5
                source: 'https://www.pxfuel.com/en/desktop-wallpaper-olzer'   
                
            MyTile: 
                stars:4
                source: 'https://www.pxfuel.com/en/desktop-wallpaper-olzer' 
'''


class FirstScr (Screen):
    pass


SManager = ScreenManager()
SManager.add_widget(FirstScr(name = 'First'))


class Main_app(MDApp):
    def build(self):
        scr = Screen()
        self.load_file = Builder.load_string(strt_String)
        scr.add_widget(self.load_file)
        return scr


Main_app().run()