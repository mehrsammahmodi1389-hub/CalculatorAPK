from kivy.app import App
from kivy.config import Config
Config.set('graphics', 'orientation', 'portrait')
from kivy.metrics import dp
from kivy.clock import Clock
from kivy.animation import Animation
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.graphics import Color, RoundedRectangle
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
import math
import pygame


from kivy.config import Config

Config.set('input', 'mouse', 'mouse,disable_multitouch')


class RoundButton(Button):
    def __init__(self, button_color=(0.18,0.18,0.22,1), **kwargs):
        super().__init__(**kwargs)

        self.background_normal = ""
        self.background_down = ""
        self.background_color = (0,0,0,0)

        with self.canvas.before:
            Color(0, 0, 0, 0.4)
            self.shadow = RoundedRectangle(
                pos=(self.x + 3, self.y - 3),
                size=self.size,
                radius=[30]
    )
            self.bg_color = Color(*button_color)
            self.round = RoundedRectangle(
                pos=self.pos,
                size=self.size,
                radius=[30]
    )

        self.bind(pos=self.update_round, size=self.update_round)

    def update_round(self, *args):
        self.round.pos = self.pos
        self.round.size = self.size

        self.shadow.pos = (self.x + 3, self.y - 3)
        self.shadow.size = self.size

    def on_press(self):
        Animation(
            opacity=0.5,
            duration=0.05
        ).start(self)

    def on_release(self):
        Animation(
            opacity=1,
            duration=0.1
        ).start(self)



class CalculatorApp(App):


    themes = [
        {
            "bg": (0.12,0.12,0.16,1),
            "button": (0.18,0.18,0.22,1)
        },
        {
            "bg": (0.05,0.12,0.25,1),
            "button": (0.1,0.3,0.6,1)
        },
        {
            "bg": (0.18,0.05,0.25,1),
            "button": (0.45,0.15,0.6,1)
        }
    ]

    theme_index = 0


    def resize_ui(self, window, size):
        width, height = size
        if width < 400:
            self.display.font_size = 36
        else:
            self.display.font_size = 48
    
    def play_sound(self):
        try:
            self.click_sound.play()
        except:
            pass


    def change_theme(self):
        self.theme_index += 1
        if self.theme_index >= len(self.themes):
            self.theme_index = 0

        theme = self.themes[self.theme_index]
        self.bg_color.rgba = theme["bg"]

        for button in self.buttons:
            button.bg_color.rgb = theme["button"][:3]

    def display_effect(self):
        anim = Animation(
            font_size=49,
            duration=0.05
    )
        anim += Animation(
            font_size=48,
            duration=0.15
    )
        anim.start(self.display)


    def update_display_bg(self, instance, value):
        self.display_bg.pos = instance.pos
        self.display_bg.size = instance.size
        
    def clear_error(self, dt):
        if self.display.text == "Error":
            self.display.text = ""

    def button_click(self, value):
        self.play_sound()
        self.display_effect()
        current = self.display.text
        if current == "Error":
            return

        if value == "C":
            self.display.text = ""
        elif value == "⌫":
            self.display.text = current[:-1]
        elif value == "=":
            if not current or current[-1] in "+-*/":
                return
            try:
                self.display.text = str(eval(current))
            except:
                self.display.text = "Error"
                Clock.schedule_once(self.clear_error, 2)
        elif value == "%":
            try:
                self.display.text = str(float(current)/100)
            except:
                self.display.text = "Error"
                Clock.schedule_once(self.clear_error, 2)
        elif value == "√":
            try:
                self.display.text = str(math.sqrt(float(current)))
            except:
                self.display.text = "Error"
                Clock.schedule_once(self.clear_error, 2)
        elif value == "±":
            if current:
                self.display.text = current[1:] if current.startswith("-") else "-" + current
        elif value == ".":
            last = current
            for op in "+-*/":
                last = last.split(op)[-1]
            if "." in last:
                return
            if current == "" or current[-1] in "+-*/":
                self.display.text += "0."
            else:
                self.display.text += "."
        elif value in "+-*/":
            if current == "":
                if value == "-":
                    self.display.text = "-"
                return
            if current[-1] in "+-*/":
                current = current[:-1]
            self.display.text = current + value
        else:
            if value == "0" and current == "0":
                return
            self.display.text += value

    def build(self):
        try:
            pygame.mixer.init()
            self.click_sound = pygame.mixer.Sound("click.wav")
        except:
            self.click_sound = None
        root = BoxLayout(orientation="vertical", padding=10, spacing=8)
        Window.bind(size=self.resize_ui)
        from kivy.graphics import Color, Rectangle

        with root.canvas.before:
            self.bg_color = Color(0.12, 0.12, 0.16, 1)
            self.bg = Rectangle(
                pos=root.pos,
                size=root.size
    )

        root.bind(pos=self.update_bg, size=self.update_bg)

        self.display = TextInput(
            readonly=True,
            multiline=False,
            halign="right",
            font_size=48,
            size_hint_y=None,
            height=dp(80),
            foreground_color=(1,1,1,1),
            background_color=(0,0,0,0)
        )
        self.display.cursor_color = (1,1,1,1)  
        with self.display.canvas:
            Color(0.02, 0.02, 0.02, 1)
            self.display_bg = RoundedRectangle(
                pos=self.display.pos,
                size=self.display.size,
                radius=[20]
            )

        self.display.bind(
            pos=self.update_display_bg,
            size=self.update_display_bg
        )
        root.add_widget(self.display)

        grid = GridLayout(
            cols=4,
            spacing=dp(8),
            size_hint_y=None,
            height=dp(380)
)
        buttons = [
    ["⌫","C","%","√"],
    ["7","8","9","/"],
    ["4","5","6","*"],
    ["1","2","3","-"],
    ["±","0",".","+"]
]
        self.buttons = []
        for row in buttons:
            for t in row:
                if t == "=":
                    color = (0.1, 0.7, 0.3, 1)       # سبز

                elif t in "+-*/":
                    color = (1, 0.5, 0.1, 1)        # نارنجی

                elif t in ["C", "⌫"]:
                    color = (0.8, 0.1, 0.1, 1)      # قرمز

                else:
                    color = (0.18, 0.18, 0.22, 1)   # خاکستری
                

                b = RoundButton(
                    text=t,
                    font_size=24,
                    size_hint_y=None,
                    height=dp(65),
                    button_color=color
)

                self.buttons.append(b)
                b.bind(on_press=lambda inst, x=t: self.button_click(x))
                grid.add_widget(b)

        theme_box = BoxLayout(
            size_hint_y=None,
            height=dp(40)
)

        theme_button = RoundButton(
            text="T",
            font_size=18,
            button_color=(0.2,0.6,1,1)
        )

        theme_box.add_widget(theme_button)

        theme_button.bind(
            on_press=lambda inst: self.change_theme()
        )

        root.add_widget(theme_box)
        root.add_widget(grid)

        equal_box = BoxLayout(
            size_hint_y=None,
            height=dp(60),
)

        equal = RoundButton(
            text="=",
            font_size=28,
            button_color=(0.1, 0.7, 0.3, 1)
        )

        equal.bind(
            on_press=lambda inst: self.button_click("=")
        )

        equal_box.add_widget(equal)
        root.add_widget(equal_box)

        return root

    def update_bg(self, instance, value):
        self.bg.pos = instance.pos
        self.bg.size = instance.size


if __name__=="__main__":
    CalculatorApp().run()
 