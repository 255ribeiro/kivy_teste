from kivy.app import App
from kivy.metrics import dp
from kivy.properties import StringProperty, BooleanProperty
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.widget import Widget


class WidgetsExample(GridLayout):
    my_text = StringProperty('0')
    text_input_str = StringProperty('Foo')
    count = 0
    slider_value_txt = StringProperty('Value')
    count_enable = BooleanProperty(False)

    def on_button_click(self):
        if self.count_enable:
            self.count += 1
            self.my_text = (str(self.count))
            print('clicked!')
        else:
            pass

    def on_tog_but_state(self, widget):
        print('state: ' + widget.state )

        if widget.state == 'normal':
            widget.text = 'OFF'
            self.count_enable = False
        if widget.state == 'down':
            self.count_enable = True
            widget.text = 'ON'
    def on_switch_active(self, widget):
        print('switch: '+ str(widget.active))

        """ 
    def on_slider_value(self, widget):
        print("Slider: " + str(widget.value))
        self.slider_value_txt = str(round(widget.value,2)) 
        
        """


    def on_text_validate(self, widget):
        self.text_input_str = widget.text


    

class TheLabApp(App):
    pass


TheLabApp().run()
