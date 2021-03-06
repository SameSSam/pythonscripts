"""
canvas of toga
"""
import toga
from toga.style import Pack
from toga.colors import WHITE, rgb
from toga.fonts import SANS_SERIF
import math 

class CanvasDemo(toga.App):

    def startup(self):
        """
        Construct and show the Toga application.

        Usually, you would add your application to a main content box.
        We then create a main window (with a name matching the app), and
        show the main window.
        """
        self.main_window = toga.MainWindow(title=self.name, size=(148,250))
        self.canvas=toga.Canvas(style=Pack(flex=1))

        main_box = toga.Box(children=[self.canvas])
               
        self.main_window.content = main_box
        self.draw_tiberius()
        self.main_window.show()
    
    def fill_head(self):
        with self.canvas.fill(color=rgb(149,119,73)) as head_filler:
            head_filler.move_to(112,103)
            head_filler.line_to(112,113)
            head_filler.ellipse(73,114,39,47,0,0,math.pi)
            head_filler.line_to(35,84)
            head_filler.arc(65,84,30,math.pi,3*math.pi/2)
            head_filler.arc(82,84,30,3*math.pi/2,2*math.pi)

    def stroke_head(self):
        with self.canvas.stroke(line_width=4.0) as head_stroker:
            with head_stroker.closed_path(112, 103) as closed_head:
                closed_head.line_to(112, 113)
                closed_head.ellipse(73, 114, 39, 47, 0, 0, math.pi)
                closed_head.line_to(35, 84)
                closed_head.arc(65, 84, 30, math.pi, 3 * math.pi / 2)
                closed_head.arc(82, 84, 30, 3 * math.pi / 2, 2 * math.pi)

    def draw_eyes(self):
        with self.canvas.fill(color=WHITE) as eye_whites:
            eye_whites.arc(58, 92, 15)
            eye_whites.arc(88, 92, 15, math.pi, 3 * math.pi)
        with self.canvas.stroke(line_width=4.0) as eye_outline:
            eye_outline.arc(58, 92, 15)
            eye_outline.arc(88, 92, 15, math.pi, 3 * math.pi)
        with self.canvas.fill() as eye_pupils:
            eye_pupils.arc(58, 97, 3)
            eye_pupils.arc(88, 97, 3)

    def draw_horns(self):
        with self.canvas.context() as r_horn:
            with r_horn.fill(color=rgb(212, 212, 212)) as r_horn_filler:
                r_horn_filler.move_to(112, 99)
                r_horn_filler.quadratic_curve_to(145, 65, 139, 36)
                r_horn_filler.quadratic_curve_to(130, 60, 109, 75)
            with r_horn.stroke(line_width=4.0) as r_horn_stroker:
                r_horn_stroker.move_to(112, 99)
                r_horn_stroker.quadratic_curve_to(145, 65, 139, 36)
                r_horn_stroker.quadratic_curve_to(130, 60, 109, 75)
        with self.canvas.context() as l_horn:
            with l_horn.fill(color=rgb(212, 212, 212)) as l_horn_filler:
                l_horn_filler.move_to(35, 99)
                l_horn_filler.quadratic_curve_to(2, 65, 6, 36)
                l_horn_filler.quadratic_curve_to(17, 60, 37, 75)
            with l_horn.stroke(line_width=4.0) as l_horn_stroker:
                l_horn_stroker.move_to(35, 99)
                l_horn_stroker.quadratic_curve_to(2, 65, 6, 36)
                l_horn_stroker.quadratic_curve_to(17, 60, 37, 75)

    def draw_nostrils(self):
        with self.canvas.fill(color=rgb(212, 212, 212)) as nose_filler:
            nose_filler.move_to(45, 145)
            nose_filler.bezier_curve_to(51, 123, 96, 123, 102, 145)
            nose_filler.ellipse(73, 114, 39, 47, 0, math.pi / 4, 3 * math.pi / 4)
        with self.canvas.fill() as nostril_filler:
            nostril_filler.arc(63, 140, 3)
            nostril_filler.arc(83, 140, 3)
        with self.canvas.stroke(line_width=4.0) as nose_stroker:
            nose_stroker.move_to(45, 145)
            nose_stroker.bezier_curve_to(51, 123, 96, 123, 102, 145)

    def draw_text(self):
        x = 32
        y = 185
        font = toga.Font(family=SANS_SERIF, size=20)
        width, height = self.canvas.measure_text('Tiberius', font, tight=True)
        with self.canvas.stroke(line_width=4.0) as rect_stroker:
            rect_stroker.rect(x - 2, y - height + 2, width, height + 2)
        with self.canvas.fill(color=rgb(149, 119, 73)) as text_filler:
            text_filler.write_text('Tiberius', x, y, font)

    def draw_tiberius(self):
        self.fill_head()
        self.draw_eyes()
        self.draw_horns()
        self.draw_nostrils()
        self.stroke_head()
        self.draw_text()


def main():
    return CanvasDemo()
