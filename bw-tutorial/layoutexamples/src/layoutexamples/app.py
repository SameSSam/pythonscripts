"""
for showing how is the layouts working
"""
import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW
import os


class LayoutExamples(toga.App):

    def startup(self):
        """
        Construct and show the Toga application.

        Usually, you would add your application to a main content box.
        We then create a main window (with a name matching the app), and
        show the main window.
        """
        brutus_icon = "./icons/brutus"
        cricket_icon = "./icons/cricket-72.png"

        data = [('root%s' %i, 'Value %s' %i) for i in range(1,100)]

        left_container = toga.Table(headings=["hello" , "World"], data = data)
        right_content = toga.Box(style=Pack(direction=COLUMN, padding_top=50))

        for b in range(0,10):
            right_content.add(toga.Button('Hello world %s' %b, on_press=self.button_handler,style=Pack(width=200,padding=20)))
        
        right_container = toga.ScrollContainer(horizontal=False)
        right_container.content = right_content
        
        split = toga.SplitContainer()
        split.content = [(left_container,1),(right_container,2)]

        #create things group
        things = toga.Group('Things')
        cmd0 = toga.Command(self.action0, label='Action 0',tooltip='Perform action 0',icon=brutus_icon,group=things)
        cmd1 = toga.Command(self.action1, label='Action 1',tooltip='Perform action 1',icon=brutus_icon,group=things)
        cmd2 = toga.Command(self.action2, label='Action 2',tooltip='Perform action 2',icon=toga.Icon.TOGA_ICON,group=things)
        #commands wiself.thout an group
        self.cmd3 = toga.Command(self.action3, label='Action 3',tooltip='Perform action 3',shortcut=toga.Key.MOD_1 + 'k',icon=cricket_icon,order=3)
        #submenu
        sub_menu = toga.Group('Sub Menu',parent=toga.Group.COMMANDS,order=2)

        cmd5 = toga.Command(self.action5,label='Action 5',tooltip='Perform action 5',order=2,group=sub_menu)
        cmd6 = toga.Command(self.action6,label="Action 6",tooltip='Perform action 6',order=1,group=sub_menu)

        cmd4 =toga.Command(self.action4,label='Action 4',tooltip='Perform action 4',icon=brutus_icon,order=1)
                

        self.commands.add(cmd1,cmd0,cmd6,cmd4,cmd5,self.cmd3)
        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.toolbar.add(cmd1,self.cmd3,cmd2,cmd4)
        self.main_window.content = split
        self.main_window.show()

    def button_handler(self,widget):
        print('button handler')
        for i in range(0,10):
            print('hello', i)
            yield
        print('Done',i)

    def action4(self,widget):
        print("Calling Action 4")
        self.cmd3.enabled = not self.cmd3.enabled


    def action0(self,widget):
        print('action 0')

    def action1(self,widget):
        print('action 1')

    def action2(self,widget):
        print('action 2')

    def action3(self,widget):
        print('action 3')

    def action5(self,widget):
        print('action 5')

    def action6(self,widget):
        print('action 6')  

def main():
    return LayoutExamples()
