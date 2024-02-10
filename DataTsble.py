from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.lang import Builder
from kivymd.uix.datatables import MDDataTable
from kivy.metrics import dp

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

        Table = MDDataTable(size_hint = (0.9,0.6),pos_hint ={'center_x':0.5,'center_y':0.5},
                            check = True,

                            rows_num = 11,
                            column_data = [
                                ('NO', dp(30)),
                                ('food',dp(30)),
                                ('calloris',dp(30))
                            ],
                            row_data = [
                                ('1','pizzzza','300'),
                                ('2','burger','499'),
                                ('3', 'burger', '499'),
                                ('4', 'burger', '499'),
                                ('5','burger','499'),
                                ('6','burger','499'),
                                ('7','burger','499'),
                                ('8', 'burger', '499'),
                                ('9', 'burger', '499'),
                                ('9', 'burger', '499'),
                                ('10', 'burger', '499')
                            ]
                            )
        Table.bind(on_check_press = self.check_press)
        Table.bind(on_row_press=self.row_press)
        scre.add_widget(Table)
        return scre
    def check_press(self,instance_tale,current_row):
        print(instance_tale,current_row)
    def row_press(self,instance_tale,current_row):
        print(instance_tale,current_row)
Mainapp().run()