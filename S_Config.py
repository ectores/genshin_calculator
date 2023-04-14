from tkinter import *
from tkinter import messagebox as MessageBox
from tkinter.ttk import Combobox, Notebook
from tkinter import filedialog
from PIL import ImageTk, Image
import os
import pandas as pd
import Languages as LG
import Number_format as Nf
import Error_fix as Ef


class Sheet_Config():
    def __init__(self, Multiple_Page):
        self.Page = Frame(Multiple_Page)

        self.dict_actual = LG.create_language(language=LG.language_actual())
        self.dict_main = LG.create_language()

        self.dict_lg = LG.create_language("-", 2)

        self.List_Language_var = StringVar()
        self.List_Language = Combobox(self.Page,values= [], textvariable=self.List_Language_var, state="readonly", width=10, postcommand= self.Load_List_Language)
        self.List_Language_var.set(LG.translate(self.dict_lg, self.dict_lg, LG.language_actual()))
        self.List_Language.bind("<<ComboboxSelected>>", self.Change_Language)
        self.Text_Language_var = StringVar()
        self.Text_Language = Label(self.Page, text=LG.translate(self.dict_main, self.dict_actual, "text_59"))

        Arch_config = pd.read_json("config.json")
        version = Arch_config["Information"]["version"]
        
        self.Text_Version1 = Label(self.Page, text=LG.translate(self.dict_main, self.dict_actual, "text_60"))
        self.Text_Version2 = Label(self.Page, text=version)

        self.Text_Ty1 = Label(self.Page, justify=LEFT, text=LG.translate(self.dict_main, self.dict_actual, "text_61"))
        self.Text_Ty2 = Label(self.Page, justify=LEFT, text=LG.translate(self.dict_main, self.dict_actual, "text_62a") + "\n" + LG.translate(self.dict_main, self.dict_actual, "text_62b"))
        self.Text_Ty3 = Label(self.Page, justify=LEFT, text=LG.translate(self.dict_main, self.dict_actual, "text_63a") + "\n" + LG.translate(self.dict_main, self.dict_actual, "text_63b"))
        self.Text_Ty4 = Label(self.Page, justify=LEFT, text=LG.translate(self.dict_main, self.dict_actual, "text_64a") + "\n" + LG.translate(self.dict_main, self.dict_actual, "text_64b"))

        self.Load_List_Language()

        self.List_Language.place(x=100, y=30, anchor=W)
        self.Text_Language.place(x=100, y=30, anchor=E)
        self.Text_Version1.place(x=100, y=60, anchor=E)
        self.Text_Version2.place(x=100, y=60, anchor=W)

        self.Text_Ty1.place(x=20, y=400)
        self.Text_Ty2.place(x=20, y=420)
        self.Text_Ty3.place(x=20, y=460)
        self.Text_Ty4.place(x=20, y=500)

    
    def Load_List_Language(self):
        directorio = os.listdir(os.getcwd() + "\Languages")
        language = []
        for element in directorio:
            if len(element) == 9:
                language.append(LG.translate(self.dict_lg, self.dict_lg, element[3:5]))
        self.List_Language.config(values= language)

    def Change_Language(self, event):
        new_language = LG.translate_inv(self.List_Language_var.get(), 2)
        Arch_config = pd.read_json("config.json")
        Arch_config["Information"]["language"] = new_language

        q1 = MessageBox.askokcancel(LG.translate(self.dict_main, self.dict_actual, "message_18"), LG.translate(self.dict_main, self.dict_actual, "message_19") + LG.translate(self.dict_lg, self.dict_lg ,LG.language_actual()) + LG.translate(self.dict_main, self.dict_actual, "message_20") + LG.translate(self.dict_lg, self.dict_lg ,new_language))
        
        if q1:
            Arch_config.to_json("config.json")
            MessageBox.showinfo(LG.translate(self.dict_main, self.dict_actual, "message_21"), LG.translate(self.dict_main, self.dict_actual, "message_22"))
        else:
            self.List_Language_var.set(LG.translate(self.dict_lg, self.dict_lg, LG.language_actual()))
    




