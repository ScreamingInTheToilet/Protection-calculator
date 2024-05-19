
#Importing tkinter

'''
Tkinter has both classic and themed widgets. There are more themed than classic widgets. Themed Tk is known as ttk.
Below is a list of all ttk widgets (themed Tkinter)
Button, Checkbutton, Entry, Frame, Label, LabelFrame, Menubutton, PanedWindow, Radiobutton, Scale, Scrollbar, Spinbox,
Combobox, Notebook, Progressbar,Separator,Sizegrip,Treeview


Components in Tkinter programs/applications are called Widgets, the standard syntax is:
widget = WidgetName(master, **options)
The pack() method is required to display the widgets, you can also use the grid() method to edit your position of the diplayed widget.
'''
import tkinter as tk
from tkinter import ttk
from Damage import Armor

# root.resizable(False, False)
'''stop the user from resizing the app'''

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        #Window
        self.geometry('500x400')
        self.resizable(False, False)
        #storing data
        self.armor = tk.StringVar()
        self.enchantment = tk.StringVar()
        self.toughness = tk.StringVar()
        self.damage = tk.StringVar()

        #text input by User
        self.textbox_armor_points = ttk.Entry(self, textvariable=self.armor).place(x=120, y=50)
        self.textbox_enchantment = ttk.Entry(self, textvariable=self.enchantment).place(x=120, y=80)
        self.textbox_toughness = ttk.Entry(self, textvariable=self.toughness).place(x=120,y=110)
        self.textbox_damage = ttk.Entry(self, textvariable=self.damage).place(x=120,y=140)

        #Labels
        self.Label_1 = ttk.Label(self, text="Armor points:").place(x=10, y=50)
        self.Label_2 = ttk.Label(self, text="Enchantment level:").place(x=10,y=80)
        self.Label_2 = ttk.Label(self, text="Armor toughness:").place(x=10,y=110)
        self.Label_2 = ttk.Label(self, text="Damage inflicted:").place(x=10,y=140)

        #button
        self.Button = ttk.Button(self,text="Enter data",command=self.show_result).place(x=120,y=170)

    def show_result(self):
        armor = float(self.armor.get())
        enchantment = float(self.enchantment.get()) * 0.16
        toughness = float(self.toughness.get()) 
        damage = float(self.damage.get())

        result = Armor(armor, enchantment, toughness,damage)

        Label_result_1 = ttk.Label(self,text=f"Remaining vulnerability based on infliction: {round(result.leaked_damage(),1)}")
        Label_result_2 = ttk.Label(self, text=f"Damage reduction based on infliction: {round(result.damage_reduction(),2)*100}")


        Label_result_1.place(x=120,y=210)
        Label_result_2.place(x=120,y=240)
        
      
        


if __name__ == "__main__":
    app = App()
    app.mainloop()


