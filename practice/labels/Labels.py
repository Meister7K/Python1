from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.metrics import dp 
from kivy.properties import StringProperty

class LabelEx(GridLayout):

    my_text=StringProperty("0")
    count = 0
    button_enabled = False
    def on_button_click(self):
        print("clicked")
        if self.button_enabled == True:
            self.count += 1
            self.my_text = str(self.count)
        
    def on_reset_click(self):
        print("reset")
        self.my_text = str(0)
        self.count = 0
    def on_toggle_state(self,widget):
        print("toggled to"+widget.state)
        if widget.state == "down":
            widget.text= "ON"
            self.button_enabled = True
        else:
            widget.text= "OFF"
            self.button_enabled = False
           

        

class LabelsApp(App):
    pass 

LabelsApp().run()
#the title and App component must be identical