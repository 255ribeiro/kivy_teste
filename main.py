from kivy.app import App
from kivy.metrics import dp
from kivy.properties import StringProperty, BooleanProperty, IntegerProperty
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.widget import Widget


class WidgetsExample(GridLayout):
    my_text = StringProperty('<-- clique no botão')
    count = 0
    font_size = IntegerProperty(100)
    def on_button_click(self):
        self.count += 1
        self.my_text = (str(self.count))
        print('clicked!')
    

class TheLabApp(App):
    pass


TheLabApp().run()
