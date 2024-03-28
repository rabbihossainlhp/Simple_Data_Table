from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen,ScreenManager
from kivymd.uix.datatables import MDDataTable
from kivy.metrics import dp

newstring = '''
ScreenManager:
    Screen_1:
    
<Screen_1>:
    name: 'New_scr'
    MDLabel:
        text: 'Check this box carefully'
        font_style: 'H4'
        pos_hint: {'center_x':0.78,'center_y':0.91}
'''

class Screen_1(Screen):
    pass

Sm = ScreenManager()
Sm.add_widget(Screen_1(name = 'New_scr'))


class Table_App(MDApp):
    def build(self):
        Sc = Screen()
        For_loaders = Builder.load_string(newstring)

        New_Table = MDDataTable(size_hint = (0.8,0.7), pos_hint = {'center_x':0.5, 'center_y':0.45},
            check = True,

            rows_num = 11,
            column_data = [
                ('No:', dp(30)),
                ('Experience of',dp(30)),
                ('D O F',dp(30)),
                ('Vehicle', dp(30))
            ],

            row_data = [
                ('1', '1 year', '1994', 'Truck'),
                ('2', '2 years', '1995', 'Car'),
                ('3', '3 years', '1996', 'Bus'),
                ('4', '4 years', '1997', 'Bus'),
                ('5', '5 years', '1998', 'Truck'),
                ('6', '6 years', '1999', 'Min-Bus'),
                ('7', '7 years', '2000', 'Bike'),
                ('8', '8 years', '2001', 'Min-Bus'),
                ('9', '9 years', '2002', 'Truck'),
                ('10', '10 years', '2003', 'Bike')

            ]
        )
        New_Table.bind(on_check_press = self.check_press)
        New_Table.bind(on_row_press = self.row_press)
        '''
        ...
        ...
        ...
        ...
        '''
        Sc.add_widget(For_loaders)
        Sc.add_widget(New_Table)
        return Sc

    '''This button for showing the value from user on the terminal((backend))'''
    def check_press(self,instance_table,current_row):
        print(instance_table,current_row)
    def row_press(self,instance_table,current_row):
        print(instance_table,current_row)


Table_App().run()