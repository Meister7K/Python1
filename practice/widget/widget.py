from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.metrics import dp 
from kivy.properties import StringProperty

class ButtonClickEx(GridLayout):
    
    my_text=StringProperty("0")
    count = 1
    def on_button_click(self):
        print("clicked")
        self.my_text = str(self.count)
        self.count += 1
    def on_reset_click(self):
        print("reset")
        self.my_text = str(0)
        self.count = 1


class WidgetApp(App):
    pass 

WidgetApp().run()