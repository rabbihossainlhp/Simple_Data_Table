from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen,ScreenManager
from kivy.lang import Builder
from kivymd.uix.list import MDList,OneLineListItem,TwoLineListItem

Start_string = '''
ScreenManager:
    FirstScreen:
    
    
<FirstScreen>:
    name: 'First'
    ScrollView:
        MDList:
            id:List 
'''



class FirstScreen(Screen):
    pass

Screen_Manager = ScreenManager()
Screen_Manager.add_widget(FirstScreen(name = 'First'))

class App(MDApp):
    def build(self):
        screen=Screen()
        self.loader_str = Builder.load_string(Start_string)
        screen.add_widget(self.loader_str)
        self.start_list()
        return screen

    def start_list(self):
        for i in range(30):
            self.loader_str.get_screen('First').ids.List.add_widget(
                OneLineListItem(text = f"Item{i}")
            )
            self.loader_str.get_screen('First').ids.List.add_widget(
                TwoLineListItem(text = f'this is another list no {i}', secondary_text = f'sub list this is{i}')
            )
App().run()
