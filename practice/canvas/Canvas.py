from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.metrics import dp 
from kivy.properties import StringProperty, BooleanProperty, Clock
from kivy.graphics.vertex_instructions import Line, Rectangle, Ellipse
from kivy.graphics.context_instructions import Color

#Builder.load_file("pickAFile.kv or .py")



class CanvasApp(App):
    pass 

# class CanvasEx(Widget):
#     def __init__(self, **kwargs):
#         downer().__init__(**kwargs)
#         with self.canvas:
#             Color(1,0,1)
#             Line(points=(0,0,self.width, self.height), width=2)
#             Line(circle=(200,200,100), width=2)
class CanvasEx2(Widget):

    
    

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.ball_size = dp(50)
        self.velX =dp(5)
        self.velY =dp(5)
        with self.canvas:
            Color(1,1,1)
            self.rect = Rectangle(pos=(0,400), size=(100,100))
            self.ball = Ellipse(pos=self.center, size=(self.ball_size,self.ball_size))
        Clock.schedule_interval(self.update, 1/60)
    def on_size(self, *args):
        self.ball.pos = (self.center_x -self.ball_size/2, self.center_y - self.ball_size/2)
    def update(self, dt):

        x,y = self.ball.pos

        x+=self.velX
        y+=self.velY

        if y + self.ball_size >self.height:
            self.velY = -self.velY
        if x + self.ball_size >self.width:
            self.velX = -self.velX
        if y <0:
            self.velY = -self.velY
        if x < 0:
            self.velX = -self.velX
        self.ball.pos = (x, y)

    def right_button_click(self):
        move_dist = dp(100)
        x,y = self.rect.pos
        w,h = self.rect.size
        contain_x = self.width -(x+w)
        if contain_x < move_dist:
            move_dist = contain_x
        x += move_dist
        self.rect.pos= (x, y)
    def up_button_click(self):
        move_dist = dp(100)
        x,y = self.rect.pos
        w,h = self.rect.size
        contain_y = self.height -(y+h)
        if contain_y < move_dist:
            move_dist = contain_y
        y += move_dist
        self.rect.pos= (x, y)
    def down_button_click(self):
        move_dist = dp(100)
        x,y = self.rect.pos
        w,h = self.rect.size
        contain_y = 0
        if contain_y >= y:
            move_dist = contain_y
        y -= move_dist
        self.rect.pos= (x, y)
    def left_button_click(self):
        move_dist = dp(100)
        x,y = self.rect.pos
        w,h = self.rect.size
        contain_x = 0 
        if contain_x >= x:
            move_dist = contain_x
        x -= move_dist
        self.rect.pos= (x, y)
CanvasApp().run()