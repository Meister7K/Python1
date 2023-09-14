from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.stacklayout import StackLayout
from kivy.metrics import dp 


class StackLayoutEx(StackLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # init comes first kv file comes second
        self.orientation= "lr-tb"
        for i  in range(0,100):
            #newSize = dp(100) + i*10
            newSize = dp(100)
            b=Button(text=str(i+1), size_hint=(None,None), size=(newSize, newSize))
            self.add_widget(b)

#class GridLayoutEx(GridLayout):
    #pass

class AnchorLayoutEx(AnchorLayout):
    pass

class BoxLayoutEx(BoxLayout):
    pass
    """   def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation="vertical"
        b1 = Button(text="1")
        b2 = Button(text = "2")
        b3 = Button(text = "3")
        self.add_widget(b1)
        self.add_widget(b2)
        self.add_widget(b3)
    """

class MainWidget(Widget):
    pass

class PracticeApp(App):
    pass

PracticeApp().run()