#Tkinter is a library for GUI
#PIL allows use images in the GUI
#os allows know if a archive exists
#pandas allows use csv archives in a easy way
#Languages, Number_Format and Error_fix are a own library
from tkinter import *
from tkinter.ttk import Notebook
import Languages as LG
#Now I import every page :D
import S_CharactersList
import S_MyCharacter
import S_InvCal
import S_Config
import S_SummaryMenu

class Interfaz():
    def __init__(self):
        self.Main_Menu = Tk()
        self.Main_Menu.title("Ectores Impact")
        self.Main_Menu.resizable(0,0) 
        self.Main_Menu.config(bg="gray")
        self.Main_Menu.iconphoto(False, PhotoImage(file='icon_paimon.png'))
        self.Main_Menu.geometry("860x600") 
        self.Multiple_Page = Notebook(self.Main_Menu)

    def Initialize(self):
        self.Multiple_Page.pack(expand=1, fill="both")
        self.Main_Menu.mainloop()

    def Add_Page(self, page, name):
         self.Multiple_Page.add(page, text=name)

if __name__ == "__main__":
    Ectores_Impact = Interfaz()

    dict_actual = LG.create_language(language=LG.language_actual())
    dict_main = LG.create_language()
    
    Config = S_Config.Sheet_Config(Ectores_Impact.Main_Menu)

    InvCal = S_InvCal.Sheet_InvCal(Ectores_Impact.Main_Menu)
    Summary_Menu = S_SummaryMenu.Sheet_SummaryMenu(Ectores_Impact.Main_Menu, InvCal)
    My_Character = S_MyCharacter.Sheet_MyCharacter(Ectores_Impact.Main_Menu, Summary_Menu, InvCal)
    Characters_List = S_CharactersList.Sheet_CharactersList(Ectores_Impact.Main_Menu, My_Character, Summary_Menu, InvCal)



    #Here i decide if a page is shown
    Ectores_Impact.Add_Page(Characters_List.Page, LG.translate(dict_main, dict_actual,"menu_1"))
    Ectores_Impact.Add_Page(My_Character.Page, LG.translate(dict_main, dict_actual,"menu_2"))
    Ectores_Impact.Add_Page(Summary_Menu.Page, LG.translate(dict_main, dict_actual,"menu_3"))
    Ectores_Impact.Add_Page(InvCal.Page, LG.translate(dict_main, dict_actual,"menu_4"))
    Ectores_Impact.Add_Page(Config.Page, LG.translate(dict_main, dict_actual,"menu_5"))
    Ectores_Impact.Initialize()



    #Quitar element_cristal de element_es y dejarlo permanentemente en mat_Es
    #Cambiar todo o al menos la mayoria de usos de listas a DataFrame (Aguante Ramon)
    #Añadir ascension objetivo para agilizar cálculos