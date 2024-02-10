from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.lang.builder import Builder

# KV string defining the screen structure
NewStr = '''
ScreenManager:
    firstscreen:

<firstscreen>:
    name: 'first'
    MDLabel:
        text: 'Assalamu alikum'
        halign: 'center'
        font_style: 'H1'
'''

# Define the app class
class NEWAPP(MDApp):
    def build(self):
        # Load the KV string and return the ScreenManager instance
        return Builder.load_string(NewStr)

# Run the app
NEWAPP().run()
