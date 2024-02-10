import kivy
from kivy.app import App
from kivy.uix.button import Button


class FirstapK(App):
    def build(self):
        def Name(instance,value):
            print("Welcome our plannet")
        btno=Button(text="HAW maww khaw")
        btno.bind(state=Name)
        return btno

if __name__=="__main__":
    FirstapK().run()

    