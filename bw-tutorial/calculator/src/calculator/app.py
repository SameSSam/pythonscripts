"""
One example of beeware
"""
import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW
from functools import partial


class Calculator(toga.App):

    def startup(self):
        """
        Construct and show the Toga application.

        Usually, you would add your application to a main content box.
        We then create a main window (with a name matching the app), and
        show the main window.
        """
        main_box = toga.Box(style=Pack(direction=COLUMN))
        #create 6 boxes
        box1 = toga.Box()
        box2 = toga.Box()
        box3 = toga.Box()
        box4 = toga.Box()
        box5 = toga.Box()
        box6 = toga.Box()
        #create inputtext 
        self.inputtext = toga.TextInput(style=Pack(width=300))

        #create buttons for the caculator
        button7 = toga.Button('7',on_press = partial(self.enterdata,number='7'),style=Pack(padding_top=30))
        button8 = toga.Button('8',on_press = partial(self.enterdata,number='8'),style=Pack(padding_top=30))
        button9 = toga.Button('9',on_press = partial(self.enterdata,number='9'),style=Pack(padding_top=30))
        buttonplus = toga.Button('+',on_press = partial(self.enterdata,number='+'),style=Pack(padding_top=30))

        button4 = toga.Button('4',on_press = partial(self.enterdata,number='4'),style=Pack(padding_top=30))
        button5 = toga.Button('5',on_press = partial(self.enterdata,number='5'),style=Pack(padding_top=30))
        button6 = toga.Button('6',on_press = partial(self.enterdata,number='6'),style=Pack(padding_top=30))
        buttonminus = toga.Button('-',on_press = partial(self.enterdata,number='-'),style=Pack(padding_top=30))

        button1 = toga.Button('1',on_press = partial(self.enterdata,number='1'),style=Pack(padding_top=30))
        button2 = toga.Button('2',on_press = partial(self.enterdata,number='2'),style=Pack(padding_top=30))
        button3 = toga.Button('3',on_press = partial(self.enterdata,number='3'),style=Pack(padding_top=30))
        buttonmultiply = toga.Button('*',on_press = partial(self.enterdata,number='*'),style=Pack(padding_top=30))

        buttondot = toga.Button('.',on_press = partial(self.enterdata,number='.'),style=Pack(padding_top=30))
        button0 = toga.Button('0',on_press = partial(self.enterdata,number='0'),style=Pack(padding_top=30))
        buttonclear = toga.Button('C',on_press = partial(self.enterdata,number='C'),style=Pack(padding_top=30))
        buttondivide = toga.Button('/',on_press = partial(self.enterdata,number='/'),style=Pack(padding_top=30))

        calculate = toga.Button('Calculate',on_press = self.calculate, style=Pack(padding_top=50,width=300))

        #add buttons to the boxes
        box1.add(self.inputtext)

        box2.add(button7)
        box2.add(button8)
        box2.add(button9)
        box2.add(buttonplus)

        box3.add(button4)
        box3.add(button5)
        box3.add(button6)
        box3.add(buttonminus)

        box4.add(button1)
        box4.add(button2)
        box4.add(button3)
        box4.add(buttonmultiply)


        box5.add(buttondot)
        box5.add(button0)
        box5.add(buttonclear)
        box5.add(buttondivide)

        box6.add(calculate)

        main_box.add(box1)
        main_box.add(box2)
        main_box.add(box3)
        main_box.add(box4)
        main_box.add(box5)
        main_box.add(box6)
 
        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()
    def enterdata(self,widget,number):
        if (number == 'C'):
            self.inputtext.value = ''
        else:
            self.inputtext.value = self.inputtext.value + number
    def calculate(self,widget):
        output = eval(self.inputtext.value)
        self.main_window.info_dialog('Result:',str(output))

def main():
    return Calculator()
