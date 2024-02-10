from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen,ScreenManager
from kivy.lang import Builder
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton

#String_forStructure
Stcr = '''
ScreenManager:
    First_Screen:
    Second_Screen:
    
<First_Screen>:
    name: 'Fisrt'
    MDLabel:
        text: 'Welcom to Our community'
        halign: 'center' 
        theme_text_color: 'Custom'
        text_color: 70, 237, 52, 0.8
        font_size: 55
        pos_hint: {'center_x':0.5, 'center_y':0.87}
        
    MDFloatingActionButton:
        icon: 'android'
        pos_hint: {'center_x':0.5, 'center_y':0.67}
        theme_text_color: 'Custom'
        user_font_size: '200sp'
        md_bg_color: 54, 0, 142, 0.8
        on_release:
            root.manager.current = 'Second'
            root.manager.transition.direction = 'left'
            
    MDRectangleFlatIconButton: 
        text: 'Click to theme'
        pos_hint: {'center_x':0.9, 'center_y':0.9}
        on_release:
            app.theme_Changer()

        
        
##Another Screen this is 
<Second_Screen>:
    id: new_text
    name:'Second'
    MDLabel:
        text: 'You Have to Customize your app from here'
        halign: 'center' 
        theme_text_color: 'Custom'
        text_color: 70, 237, 52, 0.8
        font_size: 30
        font_style: 'H5'
        pos_hint: {'center_x':0.5, 'center_y':0.7}
        
    MDFloatingActionButton:
        icon: 'android'
        pos_hint: {'center_x':0.5, 'center_y':0.6}
        theme_text_color: 'Custom'
        user_font_size: '200sp'
        md_bg_color: 54, 0, 142, 0.8
        on_release:
            root.manager.current = 'Fisrt' 
            root.manager.transition.direction = 'right'
        
    MDRectangleFlatIconButton: 
        text: 'Click to theme'
        pos_hint: {'center_x':0.9, 'center_y':0.9}
        on_release:
            app.theme_Changer()
            
    MDTextField: 
        hint_text: 'Enter Username'
        color_mode: 'Custom'
        line_focus_color: 47, 0, 81, 0.8
        line_color_normal: app.theme_cls.primary_color
        pos_hint: {'center_x':0.5, 'center_y':0.48}
        size_hint: {0.73,0.1}
        icon_right: 'star'
        icon_right_color: 47, 218, 81, 0.8
        helper_text_mode: 'on_error'
        mode: 'rectangle'
        requires: True
        
    MDIconButton:
        icon: 'star'
        pos_hint: {'center_x': 0.15, 'center_y':0.38}
        on_release: app.User_checker() 
        
        
'''



class First_Screen(Screen):
    pass
class Second_Screen(Screen):
    pass


SM = ScreenManager()
SM.add_widget(First_Screen(name="Fisrt"))
SM.add_widget(Second_Screen(name='Second'))

class Main_App(MDApp):
    def build(self):
        screen = Screen()
        self.makeVari = Builder.load_string(Stcr)
        screen.add_widget(self.makeVari)
        return screen

    def theme_Changer(self):
        if self.theme_cls.theme_style == 'Light':
            self.theme_cls.theme_style = 'Dark'
        else:
            self.theme_cls.theme_style = 'Light'

    def User_checker(self):
        user_check_false = True
        user_text_data = self.makeVari.get_screen('Second').ids.new_text.text

        try:
            int(user_text_data)
        except:
            user_check_false = False

        if user_check_false or user_text_data.split()==[]:
            clear_button = MDFlatButton(text='Retry', on_release = self.close_D)
            self.user_dialog = MDDialog(title = 'Incorrect Username',text = 'Enter correct username',size_hint = (0.5,0.2),buttons = [clear_button])
            self.user_dialog.open()

    def close_D(self,obj):
        self.user_dialog.dismiss()
Main_App().run()