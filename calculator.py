from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen,ScreenManager
from kivy.lang import Builder
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton

#Builder str>>>
helpr_St= '''
ScreenManager:
    Hello:
    anotherscreen:
    
<Hello>:
    name: 'hello'
    MDLabel:
        id:text_change
        text: 'Hello Duniya'
        halign: 'center'
        theme_text_color: 'Custom'
        text_color: 148/255,0,211/255,1
        font_style: "H1"    
        
    MDFloatingActionButton:
        icon:"android"
        user_font_size: '200sp'
        pos_hint: {'center_x':0.5, 'center_y':0.3}
        on_release:
            root.manager.current = 'new'
            root.manager.transition.direction = 'left'

    MDRectangleFlatIconButton:
        text: 'Theme'
        pos_hint: {'center_x':0.5, 'center_y':0.7}
        on_release:
            app.theme_changer()
        
    MDRectangleFlatIconButton:
        text: 'Proparty'
        pos_hint: {'center_x':0.5, 'center_y':0.8}
        on_release:app.Property()
            
<anotherscreen>:
    name: 'new'
    MDLabel:
        text: 'kaiso hoon'
        halign: 'center'
        font_style: 'H2'
        theme_text_color: 'Custom'
        text_color: 0,1,0,1
        
    MDFloatingActionButton:
        icon: 'android'
        pos_hint: {'center_x':0.5, 'center_y':0.6}
        on_release:
            root.manager.current = 'hello'
            root.manager.transition.direction = 'right' 
            
            
    MDIconButton:
        icon: 'android'
        on_release: app.user_checker()
        
    MDTextField:
        id: user_text
        hint_text: 'Username'
        color_mode: 'Custom'
        line_color_normal: app.theme_cls.primary_color
        line_color_focus: 0,1,0,1
        helper_text: 'Required'
        helper_text_mode: 'on_error'
        mode: 'rectangle'
        icon_right: 'android'
        icon_right_color: 1,0,0,1
        pos_hint: {'center_x':0.5, 'center_y':0.3}
        requires: True
        size_hint: (0.7,0.1)
        
        
'''

class Hello(Screen):
    pass
class anotherscreen(Screen):
    pass

sm=ScreenManager()
sm.add_widget(Hello(name= 'hello'))
sm.add_widget(anotherscreen(name= 'new'))

class demo(MDApp):
    def build( self):
        self.theme_cls.theme_style = 'Light'
        screen = Screen()
        self.help_s = Builder.load_string(helpr_St)
        screen.add_widget(self.help_s)
        return screen

    def theme_changer(self):
        if self.theme_cls.theme_style == 'Light':
            self.theme_cls.theme_style = 'Dark'
        else:
            self.theme_cls.theme_style = 'Light'

    def Property(self):
        if self.help_s.get_screen('hello').ids.text_change.text == 'Hello Duniya':
            self.help_s.get_screen('hello').ids.text_change.text = 'Welcom'
        else:
            self.help_s.get_screen('hello').ids.text_change.text = 'Hello Duniya'

    def user_checker(self):
        user_check_false = True
        user_text_data = self.help_s.get_screen('new').ids.user_text.text
        try:
            int(user_text_data)
        except:
            user_check_false = False

        if user_check_false or user_text_data.split()==[]:
            cancel = MDFlatButton(text = 'Retry', on_release = self.close_dialog)
            self.username_dialog = MDDialog(title = 'Invalid User',text = 'Please Enter correct username', size_hint = (0.5,0.2),buttons = [cancel])
            self.username_dialog.open()
    def close_dialog(self,obj):
        self.username_dialog.dismiss()

demo().run()