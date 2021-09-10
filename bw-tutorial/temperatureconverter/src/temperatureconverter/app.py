"""
a Fahrenheit to Celsius converter
"""
import toga
# from toga.style import Pack
from toga.style.pack import COLUMN, ROW, RIGHT,LEFT,Pack 


class TemperatureConverter(toga.App):

    def startup(self):
        """
        Construct and show the Toga application.

        Usually, you would add your application to a main content box.
        We then create a main window (with a name matching the app), and
        show the main window.
        """
        main_box = toga.Box(style=Pack(direction=COLUMN,padding_top=10))
        c_box = toga.Box()
        f_box = toga.Box()

        self.c_input =toga.TextInput(readonly=True)
        self.f_input = toga.TextInput()

        c_label = toga.Label('Celcius',style=Pack(text_align=LEFT))
        f_label = toga.Label('Fahrenheit',style=Pack(text_align=LEFT))

        join_label = toga.Label('is equivalent to',style=Pack(text_align=RIGHT))

        button = toga.Button('Calculate',on_press=self.calculate)

        f_box.add(self.f_input)
        f_box.add(f_label)

        c_box.add(join_label)
        c_box.add(self.c_input)
        c_box.add(c_label)

        main_box.add(f_box)
        main_box.add(c_box)
        main_box.add(button)

        f_box.style.update(direction=ROW,padding=5)
        c_box.style.update(direction=ROW,padding=5)

        self.c_input.style.update(flex=1)

        self.f_input.style.update(flex=1,padding_left=360)
        c_label.style.update(width=100,padding_left=10)
        f_label.style.update(width=100,padding_left=10)
        join_label.style.update(width=150,padding_right=10)
        button.style.update(padding=15,flex=1)


        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()
    def calculate(self,widget):
        try:
            self.c_input.value = (float(self.f_input.value) - 32.0) *5.0/9.0
        except ValueError:
            self.c_input.value = '???'

def main():
    return TemperatureConverter()
