from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

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