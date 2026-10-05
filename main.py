from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.graphics import Color, Rectangle


class MassihCalculatorApp(App):

    def build(self):

        layout = BoxLayout(
            orientation="vertical",
            padding=15,
            spacing=10
        )

        with layout.canvas.before:
            Color(0.05, 0.05, 0.08, 1)
            self.background = Rectangle(
                pos=layout.pos,
                size=layout.size
            )

        layout.bind(
            pos=self.update_background,
            size=self.update_background
        )

        title = Label(
            text="MASSIH CALCULATOR",
            font_size=25,
            color=(1, 1, 1, 1),
            size_hint_y=0.10
        )

        layout.add_widget(title)

        self.display = Label(
            text="0",
            font_size=55,
            color=(1, 1, 1, 1),
            size_hint_y=0.25
        )

        layout.add_widget(self.display)

        buttons = [
            ["C", "DEL", "%", "/"],
            ["7", "8", "9", "*"],
            ["4", "5", "6", "-"],
            ["1", "2", "3", "+"],
            ["0", ".", "="]
        ]

        for row in buttons:

            row_layout = BoxLayout(
                spacing=10
            )

            for text in row:

                button = Button(
                    text=text,
                    font_size=35,
                    background_normal="",
                    background_color=(0.1, 0.5, 0.9, 1)
                )

                button.bind(
                    on_press=self.button_pressed
                )

                row_layout.add_widget(button)

            layout.add_widget(row_layout)

        return layout

    def update_background(self, instance, value):
        self.background.pos = instance.pos
        self.background.size = instance.size

    def button_pressed(self, button):

        value = button.text

        if value == "C":
            self.display.text = "0"

        elif value == "DEL":

            if len(self.display.text) > 1:
                self.display.text = self.display.text[:-1]
            else:
                self.display.text = "0"

        elif value == "=":

            try:
                expression = self.display.text
                self.display.text = str(eval(expression))

            except:
                self.display.text = "Error"

        elif value == "%":

            try:
                self.display.text = str(
                    float(self.display.text) / 100
                )

            except:
                self.display.text = "Error"

        else:

            if self.display.text == "0":
                self.display.text = value
            else:
                self.display.text += value


MassihCalculatorApp().run()


