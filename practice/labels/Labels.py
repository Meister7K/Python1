from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.metrics import dp 
from kivy.properties import StringProperty, BooleanProperty


class LabelEx(GridLayout):

    my_text=StringProperty("0")
    count = 0
    button_disabled = BooleanProperty(True)
    slider_value = StringProperty("50")
    slide_dis = BooleanProperty(True)

    def on_button_click(self):
        print("clicked")
        if self.button_disabled == False:
            self.count += 1
            self.my_text = str(self.count)
         
        
    def on_reset_click(self):
        print("reset")
        if self.button_disabled == False:
            self.my_text = str(0)
            self.count = 0
           
    def on_toggle_state(self,widget):
        print("toggled to"+widget.state)
        if widget.state == "down":
            widget.text= "ON"
            self.button_disabled = False
     
        else:
            widget.text= "OFF"
            self.button_disabled = True

    def on_active(self,widget):
       if widget.active == True:
           self.slide_dis = False
       else: 
           self.slide_dis = True
           

    def on_slide(self,widget):
        if self.slide_dis == False:
            print("s"+ str(int(widget.value)))
            self.slider_value = str(int(widget.value))

        
     
           

        

class LabelsApp(App):
    pass 

LabelsApp().run()
#the title and App component must be identical