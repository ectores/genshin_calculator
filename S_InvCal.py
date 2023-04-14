from tkinter import *
from tkinter import messagebox as MessageBox
import os
import sqlite3
import Languages as LG
import Error_fix as Ef


class Sheet_InvCal():
    def __init__(self, Multiple_Page):
        self.Page = Frame(Multiple_Page)

        self.dict_actual = LG.create_language(language=LG.language_actual())
        self.dict_main = LG.create_language()

        self.Page_Inv = 1
        self.Var_Group_3 = 0
        self.Page_Category = 0
        self.Image_var = ""
        size_text_button = 11

        self.inv_list_1 = []
        self.inv_list_2 = []
        self.inv_list_3 = []
        self.inv_list_4 = []
        self.inv_list_5 = []
        self.inv_list_6 = []
        self.inv_list_7 = []
        self.inv_list_8 = []

        self.Text_Description = Label(self.Page, relief="groove", text=LG.button_text(self.dict_main, self.dict_actual, "text_42", "text_43"), width=70, height= 3)
        self.Text_Description.place(x=430, y=40, anchor=CENTER)

        self.Button_Category_1 = Button(self.Page, command=lambda: self.Change_Category(1), text=LG.button_text(self.dict_main, self.dict_actual, "button_4_part1", "button_4_part2", "button_4_part3"), font= ("TkDefaultFont",size_text_button), width=10, height=2)
        self.Button_Category_1.place(x=70 , y=110, anchor=CENTER)
        self.Button_Category_2 = Button(self.Page, command=lambda: self.Change_Category(2), text=LG.button_text(self.dict_main, self.dict_actual, "button_5_part1", "button_5_part2", "button_5_part3"), font= ("TkDefaultFont",size_text_button), width=10, height=2)
        self.Button_Category_2.place(x=173, y=110, anchor=CENTER)
        self.Button_Category_3 = Button(self.Page, command=lambda: self.Change_Category(3), text=LG.button_text(self.dict_main, self.dict_actual, "button_6_part1", "button_6_part2", "button_6_part3"), font= ("TkDefaultFont",size_text_button), width=10, height=2)
        self.Button_Category_3.place(x=276, y=110, anchor=CENTER)
        self.Button_Category_4 = Button(self.Page, command=lambda: self.Change_Category(4), text=LG.button_text(self.dict_main, self.dict_actual, "button_7_part1", "button_7_part2", "button_7_part3"), font= ("TkDefaultFont",size_text_button), width=10, height=2)
        self.Button_Category_4.place(x=380, y=110, anchor=CENTER)
        self.Button_Category_5 = Button(self.Page, command=lambda: self.Change_Category(5), text=LG.button_text(self.dict_main, self.dict_actual, "button_8_part1", "button_8_part2", "button_8_part3"), font= ("TkDefaultFont",size_text_button), width=10, height=2)
        self.Button_Category_5.place(x=483, y=110, anchor=CENTER)
        self.Button_Category_6 = Button(self.Page, command=lambda: self.Change_Category(6), text=LG.button_text(self.dict_main, self.dict_actual, "button_9_part1", "button_9_part2", "button_9_part3"), font= ("TkDefaultFont",size_text_button), width=10, height=2)
        self.Button_Category_6.place(x=586, y=110, anchor=CENTER)
        self.Button_Category_7 = Button(self.Page, command=lambda: self.Change_Category(7), text=LG.button_text(self.dict_main, self.dict_actual, "button_10_part1", "button_10_part2", "button_10_part3"), font= ("TkDefaultFont",size_text_button), width=10, height=2)
        self.Button_Category_7.place(x=688, y=110, anchor=CENTER)
        self.Button_Category_8 = Button(self.Page, command=lambda: self.Change_Category(8), text=LG.button_text(self.dict_main, self.dict_actual, "button_11_part1", "button_11_part2", "button_11_part3"), font= ("TkDefaultFont",size_text_button), width=10, height=2)
        self.Button_Category_8.place(x=790, y=110, anchor=CENTER)

        self.Marco1 = Label(self.Page)
        self.Marco1.config(relief="groove", width=32, height= 23)
        self.Marco2 = Label(self.Page)
        self.Marco2.config(relief="groove", width=32, height= 23)
        self.Marco3 = Label(self.Page)
        self.Marco3.config(relief="groove", width=32, height= 23)

        self.Text_Name_1 = Label(self.Page, text=LG.translate(self.dict_main, self.dict_actual,"test_1"))
        self.Text_Name_2 = Label(self.Page, text=LG.translate(self.dict_main, self.dict_actual,"test_2"))
        self.Text_Name_3 = Label(self.Page, text=LG.translate(self.dict_main, self.dict_actual,"test_3"))

        self.Image_1 = Label(self.Page)
        self.Image_1.place(x=165, y=180, anchor=N)
        self.Image_2 = Label(self.Page)
        self.Image_2.place(x=430, y=180, anchor=N)
        self.Image_3 = Label(self.Page)
        self.Image_3.place(x=695, y=180, anchor=N)

        self.Text_Day1 = Label(self.Page)
        self.Text_Day1.place(x=165, y=250, anchor=N)
        self.Text_Day2 = Label(self.Page)
        self.Text_Day2.place(x=430, y=250, anchor=N)
        self.Text_Day3 = Label(self.Page)
        self.Text_Day3.place(x=695, y=250, anchor=N)

        self.Text_Title1_1 = Label(self.Page, text=LG.translate(self.dict_main, self.dict_actual,"text_45"))
        self.Text_Title1_2 = Label(self.Page, text=LG.translate(self.dict_main, self.dict_actual,"text_45"))
        self.Text_Title1_3 = Label(self.Page, text=LG.translate(self.dict_main, self.dict_actual,"text_45"))


        self.Text1_Slot1_T1 = Label(self.Page, text=LG.translate(self.dict_main, self.dict_actual,"text_47") + "1")
        self.Text1_Slot1_T2 = Label(self.Page, text=LG.translate(self.dict_main, self.dict_actual,"text_47") + "2")
        self.Text1_Slot1_T3 = Label(self.Page, text=LG.translate(self.dict_main, self.dict_actual,"text_47") + "3")
        self.Text1_Slot1_T4 = Label(self.Page, text=LG.translate(self.dict_main, self.dict_actual,"text_47") + "4")
        self.Text1_Slot1_T5 = Label(self.Page, text=LG.translate(self.dict_main, self.dict_actual,"text_47") + "5")
        self.Text1_Slot1_T = Label(self.Page, text=LG.translate(self.dict_main, self.dict_actual,"text_46"))

        self.Entry_Slot1_T1_var = IntVar()
        self.Entry_Slot1_T1 = Entry(self.Page, width=5, textvariable= self.Entry_Slot1_T1_var)
        self.Entry_Slot1_T2_var = IntVar()
        self.Entry_Slot1_T2 = Entry(self.Page, width=5, textvariable= self.Entry_Slot1_T2_var)
        self.Entry_Slot1_T3_var = IntVar()
        self.Entry_Slot1_T3 = Entry(self.Page, width=5, textvariable= self.Entry_Slot1_T3_var)
        self.Entry_Slot1_T4_var = IntVar()
        self.Entry_Slot1_T4 = Entry(self.Page, width=5, textvariable= self.Entry_Slot1_T4_var)
        self.Entry_Slot1_T5_var = IntVar()
        self.Entry_Slot1_T5 = Entry(self.Page, width=5, textvariable= self.Entry_Slot1_T5_var)
        self.Entry_Slot1_T_var = IntVar()
        self.Entry_Slot1_T = Entry(self.Page, width=5, textvariable= self.Entry_Slot1_T_var)

        self.Text2_Slot1_T1_var = StringVar()
        self.Text2_Slot1_T1 = Label(self.Page, textvariable=self.Text2_Slot1_T1_var)
        self.Text2_Slot1_T2_var = StringVar()
        self.Text2_Slot1_T2 = Label(self.Page, textvariable=self.Text2_Slot1_T2_var)
        self.Text2_Slot1_T3_var = StringVar()
        self.Text2_Slot1_T3 = Label(self.Page, textvariable=self.Text2_Slot1_T3_var)
        self.Text2_Slot1_T4_var = StringVar()
        self.Text2_Slot1_T4 = Label(self.Page, textvariable=self.Text2_Slot1_T4_var)
        self.Text2_Slot1_T5_var = StringVar()
        self.Text2_Slot1_T5 = Label(self.Page, textvariable=self.Text2_Slot1_T5_var)
        self.Text2_Slot1_T_var = StringVar()
        self.Text2_Slot1_T = Label(self.Page, textvariable=self.Text2_Slot1_T_var)

        self.Text3_Slot1_var = StringVar()
        self.Text3_Slot1 = Label(self.Page, textvariable=self.Text3_Slot1_var)


        self.Text1_Slot2_T1 = Label(self.Page, text=LG.translate(self.dict_main, self.dict_actual,"text_47") + "1")
        self.Text1_Slot2_T2 = Label(self.Page, text=LG.translate(self.dict_main, self.dict_actual,"text_47") + "2")
        self.Text1_Slot2_T3 = Label(self.Page, text=LG.translate(self.dict_main, self.dict_actual,"text_47") + "3")
        self.Text1_Slot2_T4 = Label(self.Page, text=LG.translate(self.dict_main, self.dict_actual,"text_47") + "4")
        self.Text1_Slot2_T5 = Label(self.Page, text=LG.translate(self.dict_main, self.dict_actual,"text_47") + "5")
        self.Text1_Slot2_T = Label(self.Page, text=LG.translate(self.dict_main, self.dict_actual,"text_46"))

        self.Entry_Slot2_T1_var = IntVar()
        self.Entry_Slot2_T1 = Entry(self.Page, width=5, textvariable= self.Entry_Slot2_T1_var)
        self.Entry_Slot2_T2_var = IntVar()
        self.Entry_Slot2_T2 = Entry(self.Page, width=5, textvariable= self.Entry_Slot2_T2_var)
        self.Entry_Slot2_T3_var = IntVar()
        self.Entry_Slot2_T3 = Entry(self.Page, width=5, textvariable= self.Entry_Slot2_T3_var)
        self.Entry_Slot2_T4_var = IntVar()
        self.Entry_Slot2_T4 = Entry(self.Page, width=5, textvariable= self.Entry_Slot2_T4_var)
        self.Entry_Slot2_T5_var = IntVar()
        self.Entry_Slot2_T5 = Entry(self.Page, width=5, textvariable= self.Entry_Slot2_T5_var)
        self.Entry_Slot2_T_var = IntVar()
        self.Entry_Slot2_T = Entry(self.Page, width=5, textvariable= self.Entry_Slot2_T_var)

        self.Text2_Slot2_T1_var = StringVar()
        self.Text2_Slot2_T1 = Label(self.Page, textvariable=self.Text2_Slot2_T1_var)
        self.Text2_Slot2_T2_var = StringVar()
        self.Text2_Slot2_T2 = Label(self.Page, textvariable=self.Text2_Slot2_T2_var)
        self.Text2_Slot2_T3_var = StringVar()
        self.Text2_Slot2_T3 = Label(self.Page, textvariable=self.Text2_Slot2_T3_var)
        self.Text2_Slot2_T4_var = StringVar()
        self.Text2_Slot2_T4 = Label(self.Page, textvariable=self.Text2_Slot2_T4_var)
        self.Text2_Slot2_T5_var = StringVar()
        self.Text2_Slot2_T5 = Label(self.Page, textvariable=self.Text2_Slot2_T5_var)
        self.Text2_Slot2_T_var = StringVar()
        self.Text2_Slot2_T = Label(self.Page, textvariable=self.Text2_Slot2_T_var)

        self.Text3_Slot2_var = StringVar()
        self.Text3_Slot2 = Label(self.Page, textvariable=self.Text3_Slot2_var)


        self.Text1_Slot3_T1 = Label(self.Page, text=LG.translate(self.dict_main, self.dict_actual,"text_47") + "1")
        self.Text1_Slot3_T2 = Label(self.Page, text=LG.translate(self.dict_main, self.dict_actual,"text_47") + "2")
        self.Text1_Slot3_T3 = Label(self.Page, text=LG.translate(self.dict_main, self.dict_actual,"text_47") + "3")
        self.Text1_Slot3_T4 = Label(self.Page, text=LG.translate(self.dict_main, self.dict_actual,"text_47") + "4")
        self.Text1_Slot3_T5 = Label(self.Page, text=LG.translate(self.dict_main, self.dict_actual,"text_47") + "5")
        self.Text1_Slot3_T = Label(self.Page, text=LG.translate(self.dict_main, self.dict_actual,"text_46"))

        self.Entry_Slot3_T1_var = IntVar()
        self.Entry_Slot3_T1 = Entry(self.Page, width=5, textvariable= self.Entry_Slot3_T1_var)
        self.Entry_Slot3_T2_var = IntVar()
        self.Entry_Slot3_T2 = Entry(self.Page, width=5, textvariable= self.Entry_Slot3_T2_var)
        self.Entry_Slot3_T3_var = IntVar()
        self.Entry_Slot3_T3 = Entry(self.Page, width=5, textvariable= self.Entry_Slot3_T3_var)
        self.Entry_Slot3_T4_var = IntVar()
        self.Entry_Slot3_T4 = Entry(self.Page, width=5, textvariable= self.Entry_Slot3_T4_var)
        self.Entry_Slot3_T5_var = IntVar()
        self.Entry_Slot3_T5 = Entry(self.Page, width=5, textvariable= self.Entry_Slot3_T5_var)
        self.Entry_Slot3_T_var = IntVar()
        self.Entry_Slot3_T = Entry(self.Page, width=5, textvariable= self.Entry_Slot3_T_var)

        self.Text2_Slot3_T1_var = StringVar()
        self.Text2_Slot3_T1 = Label(self.Page, textvariable=self.Text2_Slot3_T1_var)
        self.Text2_Slot3_T2_var = StringVar()
        self.Text2_Slot3_T2 = Label(self.Page, textvariable=self.Text2_Slot3_T2_var)
        self.Text2_Slot3_T3_var = StringVar()
        self.Text2_Slot3_T3 = Label(self.Page, textvariable=self.Text2_Slot3_T3_var)
        self.Text2_Slot3_T4_var = StringVar()
        self.Text2_Slot3_T4 = Label(self.Page, textvariable=self.Text2_Slot3_T4_var)
        self.Text2_Slot3_T5_var = StringVar()
        self.Text2_Slot3_T5 = Label(self.Page, textvariable=self.Text2_Slot3_T5_var)
        self.Text2_Slot3_T_var = StringVar()
        self.Text2_Slot3_T = Label(self.Page, textvariable=self.Text2_Slot3_T_var)

        self.Text3_Slot3_var = StringVar()
        self.Text3_Slot3 = Label(self.Page, textvariable=self.Text3_Slot3_var)


        self.Text_Number_Page = Label(self.Page, text=LG.translate(self.dict_main, self.dict_actual,"button_3") + str(self.Page_Inv))

        self.Button_Previous = Button(self.Page, command=lambda: self.Change_Page(-1), text=LG.translate(self.dict_main, self.dict_actual,"button_3a"))
        self.Button_Next = Button(self.Page, command=lambda: self.Change_Page(1), text=LG.translate(self.dict_main, self.dict_actual,"button_3b"))


        self.image_cancel = LG.fastimport_imagech("undo", "others", 4)
        self.image_save = LG.fastimport_imagech("save", "others", 4)

        self.ButtonCancelChange = Button(self.Page, image=self.image_cancel,state=NORMAL,command=lambda: self.Save_Data(False))
        
        self.ButtonSaveChange = Button(self.Page, image=self.image_save,state=NORMAL,command=lambda: self.Save_Data(True))

        self.Reload_Data()



    def Change_Category(self, Page_Category):
        self.Move_Entries()

        self.Page_Category = Page_Category
        conexion1 = sqlite3.connect("DB SQL/genshin_db.db")

        query1 = conexion1.execute(f"select * from user_inv where Category={self.Page_Category} ORDER by order1, order2")

        self.N_per_category = len(query1.fetchall())

        self.Inv_Per_category = query1.fetchall()

        self.Page_Inv = 1
        self.Max_Pages = 1

        if self.N_per_category % 3 == 0:
            self.Max_Pages = self.N_per_category // 3
        else:
            self.Max_Pages = self.N_per_category // 3 + 1
        self.Change_Page(0)



    def Config_Entries(self):   
        self.Button_Category_1.config(state=NORMAL)
        self.Button_Category_2.config(state=NORMAL)
        self.Button_Category_3.config(state=NORMAL)
        self.Button_Category_4.config(state=NORMAL)
        self.Button_Category_5.config(state=NORMAL)
        self.Button_Category_6.config(state=NORMAL)
        self.Button_Category_7.config(state=NORMAL)
        self.Button_Category_8.config(state=NORMAL)

        self.Entry_Slot1_T1.config(state=NORMAL)
        self.Entry_Slot1_T2.config(state=NORMAL)
        self.Entry_Slot1_T3.config(state=NORMAL)
        self.Entry_Slot1_T4.config(state=NORMAL)
        self.Entry_Slot1_T5.config(state=NORMAL)

        self.Entry_Slot2_T1.config(state=NORMAL)
        self.Entry_Slot2_T2.config(state=NORMAL)
        self.Entry_Slot2_T3.config(state=NORMAL)
        self.Entry_Slot2_T4.config(state=NORMAL)
        self.Entry_Slot2_T5.config(state=NORMAL)

        self.Entry_Slot3_T1.config(state=NORMAL)
        self.Entry_Slot3_T2.config(state=NORMAL)
        self.Entry_Slot3_T3.config(state=NORMAL)
        self.Entry_Slot3_T4.config(state=NORMAL)
        self.Entry_Slot3_T5.config(state=NORMAL)

        self.Entry_Slot1_T.config(state=DISABLED)
        self.Entry_Slot2_T.config(state=DISABLED)
        self.Entry_Slot3_T.config(state=DISABLED)


        if self.Page_Category == 1:
            self.Button_Category_1.config(state=DISABLED)
            self.Var_Group_3 = 0
            self.Image_var = "cristal"
            self.Entry_Slot1_T1.config(state=DISABLED)
            self.Entry_Slot2_T1.config(state=DISABLED)
            self.Entry_Slot3_T1.config(state=DISABLED)
        elif self.Page_Category == 2:
            self.Button_Category_2.config(state=DISABLED)
            self.Var_Group_3 = 1
            self.Image_var = "talent"
            self.Entry_Slot1_T1.config(state=DISABLED)
            self.Entry_Slot1_T5.config(state=DISABLED)

            self.Entry_Slot2_T1.config(state=DISABLED)
            self.Entry_Slot2_T5.config(state=DISABLED)

            self.Entry_Slot3_T1.config(state=DISABLED)
            self.Entry_Slot3_T5.config(state=DISABLED)
        elif self.Page_Category == 3:
            self.Button_Category_3.config(state=DISABLED)
            self.Var_Group_3 = 1
            self.Image_var = "weapon_asc"
            self.Entry_Slot1_T1.config(state=DISABLED)
            self.Entry_Slot2_T1.config(state=DISABLED)
            self.Entry_Slot3_T1.config(state=DISABLED)
        elif self.Page_Category == 4:
            self.Button_Category_4.config(state=DISABLED)
            self.Var_Group_3 = 0
            self.Image_var = "mat_common"
            self.Entry_Slot1_T1.config(state=DISABLED)
            self.Entry_Slot1_T5.config(state=DISABLED)

            self.Entry_Slot2_T1.config(state=DISABLED)
            self.Entry_Slot2_T5.config(state=DISABLED)
            
            self.Entry_Slot3_T1.config(state=DISABLED)
            self.Entry_Slot3_T5.config(state=DISABLED)
        elif self.Page_Category == 5:
            self.Button_Category_5.config(state=DISABLED)
            self.Var_Group_3 = 0
            self.Image_var = "mat_common"
            self.Entry_Slot1_T4.config(state=DISABLED)
            self.Entry_Slot1_T5.config(state=DISABLED)

            self.Entry_Slot2_T4.config(state=DISABLED)
            self.Entry_Slot2_T5.config(state=DISABLED)
            
            self.Entry_Slot3_T4.config(state=DISABLED)
            self.Entry_Slot3_T5.config(state=DISABLED)
        elif self.Page_Category == 6:
            self.Button_Category_6.config(state=DISABLED)
            self.Var_Group_3 = 0
            self.Image_var = "mat_local"
            self.Entry_Slot1_T2.config(state=DISABLED)
            self.Entry_Slot1_T3.config(state=DISABLED)
            self.Entry_Slot1_T4.config(state=DISABLED)
            self.Entry_Slot1_T5.config(state=DISABLED)

            self.Entry_Slot2_T2.config(state=DISABLED)
            self.Entry_Slot2_T3.config(state=DISABLED)
            self.Entry_Slot2_T4.config(state=DISABLED)
            self.Entry_Slot2_T5.config(state=DISABLED)

            self.Entry_Slot3_T2.config(state=DISABLED)
            self.Entry_Slot3_T3.config(state=DISABLED)
            self.Entry_Slot3_T4.config(state=DISABLED)
            self.Entry_Slot3_T5.config(state=DISABLED)
        elif self.Page_Category == 7:
            self.Button_Category_7.config(state=DISABLED)
            self.Var_Group_3 = 0
            self.Image_var = "ib_normal"
            self.Entry_Slot1_T1.config(state=DISABLED)
            self.Entry_Slot1_T2.config(state=DISABLED)
            self.Entry_Slot1_T3.config(state=DISABLED)
            self.Entry_Slot1_T5.config(state=DISABLED)

            self.Entry_Slot2_T1.config(state=DISABLED)
            self.Entry_Slot2_T2.config(state=DISABLED)
            self.Entry_Slot2_T3.config(state=DISABLED)
            self.Entry_Slot2_T5.config(state=DISABLED)

            self.Entry_Slot3_T1.config(state=DISABLED)
            self.Entry_Slot3_T2.config(state=DISABLED)
            self.Entry_Slot3_T3.config(state=DISABLED)
            self.Entry_Slot3_T5.config(state=DISABLED)
        else:
            self.Button_Category_8.config(state=DISABLED)
            self.Var_Group_3 = 2
            self.Image_var = "ib_weekly"
            self.Entry_Slot1_T1.config(state=DISABLED)
            self.Entry_Slot1_T2.config(state=DISABLED)
            self.Entry_Slot1_T3.config(state=DISABLED)
            self.Entry_Slot1_T4.config(state=DISABLED)

            self.Entry_Slot2_T1.config(state=DISABLED)
            self.Entry_Slot2_T2.config(state=DISABLED)
            self.Entry_Slot2_T3.config(state=DISABLED)
            self.Entry_Slot2_T4.config(state=DISABLED)

            self.Entry_Slot3_T1.config(state=DISABLED)
            self.Entry_Slot3_T2.config(state=DISABLED)
            self.Entry_Slot3_T3.config(state=DISABLED)
            self.Entry_Slot3_T4.config(state=DISABLED)

        

    def Move_Entries(self):
        if self.Page_Category == 0:

            self.Button_Previous.place(x=325, y=530, anchor=CENTER)
            self.Button_Next.place(x=535, y=530, anchor=CENTER)
            self.Text_Number_Page.place(x=430, y=530, anchor=CENTER)

            self.ButtonCancelChange.place(x=130, y=40, anchor=CENTER)
            self.ButtonSaveChange.place(x=730, y=40, anchor=CENTER)

            self.Text_Name_1.place(x=165, y=170, anchor=CENTER)
            self.Text_Name_2.place(x=430, y=170, anchor=CENTER)
            self.Text_Name_3.place(x=695, y=170, anchor=CENTER)

            self.Text_Title1_1.place(x=165, y=280, anchor=CENTER)
            self.Text_Title1_2.place(x=430, y=280, anchor=CENTER)
            self.Text_Title1_3.place(x=695, y=280, anchor=CENTER)


            self.Text1_Slot1_T1.place(x=125, y=310, anchor=E)
            self.Text1_Slot1_T2.place(x=125, y=335, anchor=E)
            self.Text1_Slot1_T3.place(x=125, y=360, anchor=E)
            self.Text1_Slot1_T4.place(x=125, y=385, anchor=E)
            self.Text1_Slot1_T5.place(x=125, y=410, anchor=E)
            self.Text1_Slot1_T.place(x=125, y=445, anchor=E)

            self.Entry_Slot1_T1.place(x=165, y=311, anchor=E)
            self.Entry_Slot1_T2.place(x=165, y=336, anchor=E)
            self.Entry_Slot1_T3.place(x=165, y=361, anchor=E)
            self.Entry_Slot1_T4.place(x=165, y=386, anchor=E)
            self.Entry_Slot1_T5.place(x=165, y=411, anchor=E)
            self.Entry_Slot1_T.place(x=165, y=446, anchor=E)

            self.Text2_Slot1_T1.place(x=170, y=310, anchor=W)
            self.Text2_Slot1_T2.place(x=170, y=335, anchor=W)
            self.Text2_Slot1_T3.place(x=170, y=360, anchor=W)
            self.Text2_Slot1_T4.place(x=170, y=385, anchor=W)
            self.Text2_Slot1_T5.place(x=170, y=410, anchor=W)
            self.Text2_Slot1_T.place(x=170, y=445, anchor=W)

            self.Text3_Slot1.place(x=165, y=480, anchor=CENTER)


            self.Text1_Slot2_T1.place(x=390, y=310, anchor=E)
            self.Text1_Slot2_T2.place(x=390, y=335, anchor=E)
            self.Text1_Slot2_T3.place(x=390, y=360, anchor=E)
            self.Text1_Slot2_T4.place(x=390, y=385, anchor=E)
            self.Text1_Slot2_T5.place(x=390, y=410, anchor=E)
            self.Text1_Slot2_T.place(x=390, y=445, anchor=E)

            self.Entry_Slot2_T1.place(x=430, y=311, anchor=E)
            self.Entry_Slot2_T2.place(x=430, y=336, anchor=E)
            self.Entry_Slot2_T3.place(x=430, y=361, anchor=E)
            self.Entry_Slot2_T4.place(x=430, y=386, anchor=E)
            self.Entry_Slot2_T5.place(x=430, y=411, anchor=E)
            self.Entry_Slot2_T.place(x=430, y=446, anchor=E)

            self.Text2_Slot2_T1.place(x=435, y=310, anchor=W)
            self.Text2_Slot2_T2.place(x=435, y=335, anchor=W)
            self.Text2_Slot2_T3.place(x=435, y=360, anchor=W)
            self.Text2_Slot2_T4.place(x=435, y=385, anchor=W)
            self.Text2_Slot2_T5.place(x=435, y=410, anchor=W)
            self.Text2_Slot2_T.place(x=435, y=445, anchor=W)

            self.Text3_Slot2.place(x=430, y=480, anchor=CENTER)


            self.Text1_Slot3_T1.place(x=655, y=310, anchor=E)
            self.Text1_Slot3_T2.place(x=655, y=335, anchor=E)
            self.Text1_Slot3_T3.place(x=655, y=360, anchor=E)
            self.Text1_Slot3_T4.place(x=655, y=385, anchor=E)
            self.Text1_Slot3_T5.place(x=655, y=410, anchor=E)
            self.Text1_Slot3_T.place(x=655, y=445, anchor=E)

            self.Entry_Slot3_T1.place(x=695, y=311, anchor=E)
            self.Entry_Slot3_T2.place(x=695, y=336, anchor=E)
            self.Entry_Slot3_T3.place(x=695, y=361, anchor=E)
            self.Entry_Slot3_T4.place(x=695, y=386, anchor=E)
            self.Entry_Slot3_T5.place(x=695, y=411, anchor=E)
            self.Entry_Slot3_T.place(x=695, y=446, anchor=E)

            self.Text2_Slot3_T1.place(x=700, y=310, anchor=W)
            self.Text2_Slot3_T2.place(x=700, y=335, anchor=W)
            self.Text2_Slot3_T3.place(x=700, y=360, anchor=W)
            self.Text2_Slot3_T4.place(x=700, y=385, anchor=W)
            self.Text2_Slot3_T5.place(x=700, y=410, anchor=W)
            self.Text2_Slot3_T.place(x=700, y=445, anchor=W)

            self.Text3_Slot3.place(x=695, y=480, anchor=CENTER)
        
            self.Marco1.place(x=165, y=150, anchor=N) #-50
            self.Marco2.place(x=430, y=150, anchor=N)
            self.Marco3.place(x=695, y=150, anchor=N) #+50



    def Reload_Data(self):
    
        conexion2 = sqlite3.connect("DB SQL/genshin_db.db")


        query1a = conexion2.execute("select e.cristal, sum(u.Ascension_Cristal_Tier2) as cristalt2, sum(u.Ascension_Cristal_Tier3) as cristalt3, sum(u.Ascension_Cristal_Tier4) as cristalt4, sum(u.Ascension_Cristal_Tier5) as cristalt5 from user as u join db_base as b on u.Character=b.id join db_element as e on b.element=e.element where b.traveller=0 group by e.cristal")
        query1b = conexion2.execute("select e.cristal, sum(u.Ascension_Cristal_Tier2) as cristalt2, sum(u.Ascension_Cristal_Tier3) as cristalt3, sum(u.Ascension_Cristal_Tier4) as cristalt4, sum(u.Ascension_Cristal_Tier5) as cristalt5 from user as u join db_base as b on u.Character=b.id join db_element as e on b.element=e.element where b.traveller=0 and u.Build = 'status_2' group by e.cristal")
        self.inv_list_1a = query1a.fetchall()
        self.inv_list_1b = query1b.fetchall()


        query2a = conexion2.execute("""select n1, sum(t2), sum(t3), sum(t4) from (select u.Character, b.tal_1_book_1 as n1, u.Tal1_B1_T2 as t2, u.Tal1_B1_T3 as t3, u.Tal1_B1_T4 as t4 from user as u join db_base as b on u.Character = b.id 
                                    union all
                                    select u.Character, b.tal_1_book_2 as n1, u.Tal1_B2_T2 as t2, u.Tal1_B2_T3 as t3, u.Tal1_B2_T4 as t4 from user as u join db_base as b on u.Character = b.id
                                    union all
                                    select u.Character, b.tal_1_book_3 as n1, u.Tal1_B3_T2 as t2, u.Tal1_B3_T3 as t3, u.Tal1_B3_T4 as t4 from user as u join db_base as b on u.Character = b.id
                                    union all
                                    select u.Character, b.tal_2_book_1 as n1, u.Tal2_B1_T2 as t2, u.Tal2_B1_T3 as t3, u.Tal2_B1_T4 as t4 from user as u join db_base as b on u.Character = b.id
                                    union all
                                    select u.Character, b.tal_2_book_2 as n1, u.Tal2_B2_T2 as t2, u.Tal2_B2_T3 as t3, u.Tal2_B2_T4 as t4 from user as u join db_base as b on u.Character = b.id
                                    union all
                                    select u.Character, b.tal_2_book_3 as n1, u.Tal2_B3_T2 as t2, u.Tal2_B3_T3 as t3, u.Tal2_B3_T4 as t4 from user as u join db_base as b on u.Character = b.id
                                    union all
                                    select u.Character, b.tal_3_book_1 as n1, u.Tal3_B1_T2 as t2, u.Tal3_B1_T3 as t3, u.Tal3_B1_T4 as t4 from user as u join db_base as b on u.Character = b.id
                                    union all
                                    select u.Character, b.tal_3_book_2 as n1, u.Tal3_B2_T2 as t2, u.Tal3_B2_T3 as t3, u.Tal3_B2_T4 as t4 from user as u join db_base as b on u.Character = b.id
                                    union all
                                    select u.Character, b.tal_3_book_3 as n1, u.Tal3_B3_T2 as t2, u.Tal3_B3_T3 as t3, u.Tal3_B3_T4 as t4 from user as u join db_base as b on u.Character = b.id)
                                    group by n1
                                    """)
        query2b = conexion2.execute("""select n1, sum(t2), sum(t3), sum(t4) from (select u.Character, b.tal_1_book_1 as n1, u.Tal1_B1_T2 as t2, u.Tal1_B1_T3 as t3, u.Tal1_B1_T4 as t4 from user as u join db_base as b on u.Character = b.id where u.Build = 'status_2'
                                    union all
                                    select u.Character, b.tal_1_book_2 as n1, u.Tal1_B2_T2 as t2, u.Tal1_B2_T3 as t3, u.Tal1_B2_T4 as t4 from user as u join db_base as b on u.Character = b.id where u.Build = 'status_2'
                                    union all
                                    select u.Character, b.tal_1_book_3 as n1, u.Tal1_B3_T2 as t2, u.Tal1_B3_T3 as t3, u.Tal1_B3_T4 as t4 from user as u join db_base as b on u.Character = b.id where u.Build = 'status_2'
                                    union all
                                    select u.Character, b.tal_2_book_1 as n1, u.Tal2_B1_T2 as t2, u.Tal2_B1_T3 as t3, u.Tal2_B1_T4 as t4 from user as u join db_base as b on u.Character = b.id where u.Build = 'status_2'
                                    union all
                                    select u.Character, b.tal_2_book_2 as n1, u.Tal2_B2_T2 as t2, u.Tal2_B2_T3 as t3, u.Tal2_B2_T4 as t4 from user as u join db_base as b on u.Character = b.id where u.Build = 'status_2'
                                    union all
                                    select u.Character, b.tal_2_book_3 as n1, u.Tal2_B3_T2 as t2, u.Tal2_B3_T3 as t3, u.Tal2_B3_T4 as t4 from user as u join db_base as b on u.Character = b.id where u.Build = 'status_2'
                                    union all
                                    select u.Character, b.tal_3_book_1 as n1, u.Tal3_B1_T2 as t2, u.Tal3_B1_T3 as t3, u.Tal3_B1_T4 as t4 from user as u join db_base as b on u.Character = b.id where u.Build = 'status_2'
                                    union all
                                    select u.Character, b.tal_3_book_2 as n1, u.Tal3_B2_T2 as t2, u.Tal3_B2_T3 as t3, u.Tal3_B2_T4 as t4 from user as u join db_base as b on u.Character = b.id where u.Build = 'status_2'
                                    union all
                                    select u.Character, b.tal_3_book_3 as n1, u.Tal3_B3_T2 as t2, u.Tal3_B3_T3 as t3, u.Tal3_B3_T4 as t4 from user as u join db_base as b on u.Character = b.id where u.Build = 'status_2')
                                    group by n1
                                    """)
        self.inv_list_2a = query2a.fetchall()
        self.inv_list_2b = query2b.fetchall()


        query3a = conexion2.execute("select w.mat_domain_weapon, sum(u.Weapon_Material_Domain_Tier2) as matt2, sum(u.Weapon_Material_Domain_Tier3) as matt3, sum(u.Weapon_Material_Domain_Tier4) as matt4, sum(u.Weapon_Material_Domain_Tier5) as matt5 from user as u join db_weapon as w on u.weapon = w.id group by w.mat_domain_weapon")
        query3b = conexion2.execute("select w.mat_domain_weapon, sum(u.Weapon_Material_Domain_Tier2) as matt2, sum(u.Weapon_Material_Domain_Tier3) as matt3, sum(u.Weapon_Material_Domain_Tier4) as matt4, sum(u.Weapon_Material_Domain_Tier5) as matt5 from user as u join db_weapon as w on u.weapon = w.id where u.Build = 'status_2' group by w.mat_domain_weapon")
        self.inv_list_3a = query3a.fetchall()
        self.inv_list_3b = query3b.fetchall()


        query4a = conexion2.execute("select w.mat_com_1, sum(u.Weapon_Material_Common_1_Tier2) as t2, sum(u.Weapon_Material_Common_1_Tier3) as t3, sum(u.Weapon_Material_Common_1_Tier4) as t4 from user as u join db_weapon as w on u.weapon = w.id group by w.mat_com_1")
        query4b = conexion2.execute("select w.mat_com_1, sum(u.Weapon_Material_Common_1_Tier2) as t2, sum(u.Weapon_Material_Common_1_Tier3) as t3, sum(u.Weapon_Material_Common_1_Tier4) as t4 from user as u join db_weapon as w on u.weapon = w.id where u.Build = 'status_2' group by w.mat_com_1")
        self.inv_list_4a = query4a.fetchall()
        self.inv_list_4b = query4b.fetchall()

        query5a = conexion2.execute("""select mat_2, sum(t1), sum(t2), sum(t3) from (select w.mat_com_2 as mat_2, u.Weapon_Material_Common_2_Tier1 as t1, u.Weapon_Material_Common_2_Tier2 as t2, u.Weapon_Material_Common_2_Tier3 as t3 from user as u join db_weapon as w on u.weapon = w.id
                                    union ALL
                                    select b.asc_mat_com_2 as mat_2, u.Ascension_Material_Common_2_Tier1 as t1, u.Ascension_Material_Common_2_Tier2 as t2, u.Ascension_Material_Common_2_Tier3 as t3 from user as u join db_base as b on u.Character = b.id
                                    union ALL
                                    select b.tal_1_mat_com_2 as mat_2, u.Tal1_Com2_T1 as t1, u.Tal1_Com2_T2 as t2, u.Tal1_Com2_T3 as t3 from user as u join db_base as b on u.Character = b.id
                                    union ALL
                                    select b.tal_2_mat_com_2 as mat_2, u.Tal2_Com2_T1 as t1, u.Tal2_Com2_T2 as t2, u.Tal2_Com2_T3 as t3 from user as u join db_base as b on u.Character = b.id
                                    union ALL
                                    select b.tal_3_mat_com_2 as mat_2, u.Tal3_Com2_T1 as t1, u.Tal3_Com2_T2 as t2, u.Tal3_Com2_T3 as t3 from user as u join db_base as b on u.Character = b.id)
                                    group by mat_2
                                    """)
        query5b = conexion2.execute("""select mat_2, sum(t1), sum(t2), sum(t3) from (select w.mat_com_2 as mat_2, u.Weapon_Material_Common_2_Tier1 as t1, u.Weapon_Material_Common_2_Tier2 as t2, u.Weapon_Material_Common_2_Tier3 as t3 from user as u join db_weapon as w on u.weapon = w.id where u.Build = 'status_2'
                                    union ALL
                                    select b.asc_mat_com_2 as mat_2, u.Ascension_Material_Common_2_Tier1 as t1, u.Ascension_Material_Common_2_Tier2 as t2, u.Ascension_Material_Common_2_Tier3 as t3 from user as u join db_base as b on u.Character = b.id where u.Build = 'status_2'
                                    union ALL
                                    select b.tal_1_mat_com_2 as mat_2, u.Tal1_Com2_T1 as t1, u.Tal1_Com2_T2 as t2, u.Tal1_Com2_T3 as t3 from user as u join db_base as b on u.Character = b.id where u.Build = 'status_2'
                                    union ALL
                                    select b.tal_2_mat_com_2 as mat_2, u.Tal2_Com2_T1 as t1, u.Tal2_Com2_T2 as t2, u.Tal2_Com2_T3 as t3 from user as u join db_base as b on u.Character = b.id where u.Build = 'status_2'
                                    union ALL
                                    select b.tal_3_mat_com_2 as mat_2, u.Tal3_Com2_T1 as t1, u.Tal3_Com2_T2 as t2, u.Tal3_Com2_T3 as t3 from user as u join db_base as b on u.Character = b.id where u.Build = 'status_2')
                                    group by mat_2
                                    """)
        self.inv_list_5a = query5a.fetchall()
        self.inv_list_5b = query5b.fetchall()


        query6a = conexion2.execute("select b.mat_local, sum(u.Ascension_Material_Local) from user as u join db_base as b on u.Character=b.id group by b.mat_local")
        query6b = conexion2.execute("select b.mat_local, sum(u.Ascension_Material_Local) from user as u join db_base as b on u.Character=b.id where u.Build = 'status_2' group by b.mat_local")
        self.inv_list_6a = query6a.fetchall()
        self.inv_list_6b = query6b.fetchall()



        query7a = conexion2.execute("select b.mat_boss_daily, sum(u.Ascension_Material_NormalBoss) from user as u join db_base as b on u.Character = b.id group by b.mat_boss_daily")
        query7b = conexion2.execute("select b.mat_boss_daily, sum(u.Ascension_Material_NormalBoss) from user as u join db_base as b on u.Character = b.id where u.Build = 'status_2' group by b.mat_boss_daily")
        self.inv_list_7a = query7a.fetchall()
        self.inv_list_7b = query7b.fetchall()


        query8a = conexion2.execute("""select n1, sum(q1) from (select u.Character, b.tal_1_mat_boss_weekly as n1, u.Tal1_MatBoss as q1 from user as u join db_base as b on u.Character = b.id
                                    union all
                                    select u.Character, b.tal_2_mat_boss_weekly as n1, u.Tal2_MatBoss as q1 from user as u join db_base as b on u.Character = b.id
                                    union all
                                    select u.Character, b.tal_3_mat_boss_weekly as n1, u.Tal3_MatBoss as q1 from user as u join db_base as b on u.Character = b.id)
                                    group by n1
                                    """)
        query8b = conexion2.execute("""select n1, sum(q1) from (select u.Character, b.tal_1_mat_boss_weekly as n1, u.Tal1_MatBoss as q1 from user as u join db_base as b on u.Character = b.id where u.Build = 'status_2'
                                    union all
                                    select u.Character, b.tal_2_mat_boss_weekly as n1, u.Tal2_MatBoss as q1 from user as u join db_base as b on u.Character = b.id where u.Build = 'status_2'
                                    union all
                                    select u.Character, b.tal_3_mat_boss_weekly as n1, u.Tal3_MatBoss as q1 from user as u join db_base as b on u.Character = b.id where u.Build = 'status_2')
                                    group by n1
                                    """)
        self.inv_list_8a = query8a.fetchall()
        self.inv_list_8b = query8b.fetchall()

        conexion2.commit()


    def Show_Data(self):

        #OBJETOS A FARMEAR



        if self.Page_Category == 1:
            self.list_to_use = self.inv_list_1a
            self.list_to_use_bld = self.inv_list_1b
        elif self.Page_Category == 2:
            self.list_to_use = self.inv_list_2a
            self.list_to_use_bld = self.inv_list_2b
        elif self.Page_Category == 3:
            self.list_to_use = self.inv_list_3a
            self.list_to_use_bld = self.inv_list_3b
        elif self.Page_Category == 4:
            self.list_to_use = self.inv_list_4a
            self.list_to_use_bld = self.inv_list_4b
        elif self.Page_Category == 5:
            self.list_to_use = self.inv_list_5a
            self.list_to_use_bld = self.inv_list_5b
        elif self.Page_Category == 6:
            self.list_to_use = self.inv_list_6a
            self.list_to_use_bld = self.inv_list_6b
        elif self.Page_Category == 7:
            self.list_to_use = self.inv_list_7a
            self.list_to_use_bld = self.inv_list_7b
        elif self.Page_Category == 8:
            self.list_to_use = self.inv_list_8a
            self.list_to_use_bld = self.inv_list_8b


        conexion3 = sqlite3.connect("DB SQL/genshin_db.db")

        #OBJETOS EN INV
        query1 = conexion3.execute("select * from user_inv")
        conexion3.commit()

        list_inv = []

        for fila in query1:
            list_inv.append(list(fila))


        List_per_category = []
        for element_inv in list_inv:
            if element_inv[1] == self.Page_Category:
                List_per_category.append([element_inv[0], element_inv[1], element_inv[2], element_inv[3], element_inv[4], element_inv[5], element_inv[6], element_inv[7], element_inv[8], LG.translate(self.dict_main, self.dict_actual,element_inv[0])])
        



        self.var_id_1 = ""
        self.var_id_2 = ""
        self.var_id_3 = ""

        self.var_exist_1 = 0
        self.var_exist_2 = 0
        self.var_exist_3 = 0

        for element_category in List_per_category:
            if self.Var_Group_3 != 0:
                if int(element_category[2]) == self.Page_Inv:    
                    if int(element_category[3]) == 1:
                        self.Text_Name_1.config(text= element_category[9])
                        self.var_id_1 = element_category[0]
                        self.var_exist_1 = 1
                        if os.path.exists("Images/" + self.Image_var + "/" + element_category[0] + ".png"):
                            self.Image_1_var = LG.fastimport_imagech(element_category[0], self.Image_var, 2)
                        else:
                            self.Image_1_var = LG.fastimport_imagech("", self.Image_var, 2)
                    elif int(element_category[3]) == 2:
                        self.Text_Name_2.config(text= element_category[9])
                        self.var_id_2 = element_category[0]
                        self.var_exist_2 = 1
                        if os.path.exists("Images/" + self.Image_var + "/" + element_category[0] + ".png"):
                            self.Image_2_var = LG.fastimport_imagech(element_category[0], self.Image_var, 2)
                        else:
                            self.Image_2_var = LG.fastimport_imagech("", self.Image_var, 2)
                    elif int(element_category[3]) == 3:
                        self.Text_Name_3.config(text= element_category[9])
                        self.var_id_3 = element_category[0]
                        self.var_exist_3 = 1
                        if os.path.exists("Images/" + self.Image_var + "/" + element_category[0] + ".png"):
                            self.Image_3_var = LG.fastimport_imagech(element_category[0], self.Image_var, 2)
                        else:
                            self.Image_3_var = LG.fastimport_imagech("", self.Image_var, 2)
            else:
                List_per_category.sort(key=lambda x: x[9])

                if self.Page_Inv*3-2 <= self.N_per_category:
                    self.Text_Name_1.config(text=List_per_category[self.Page_Inv*3-3][9])
                    self.var_id_1 = List_per_category[self.Page_Inv*3-3][0]
                    self.var_exist_1 = 1
                    if os.path.exists("Images/" + self.Image_var + "/" + List_per_category[self.Page_Inv*3-3][0] + ".png"):
                        self.Image_1_var = LG.fastimport_imagech(List_per_category[self.Page_Inv*3-3][0], self.Image_var, 2)
                    else:
                        self.Image_1_var = LG.fastimport_imagech("", self.Image_var, 2)
                else:
                    self.Text_Name_1.config(text=LG.translate(self.dict_main, self.dict_actual,"text_44"))
                    self.Image_1_var = LG.fastimport_imagech("", self.Image_var, 2)
                    self.var_id_1 = ""
                    self.Entry_Slot1_T1.config(state=DISABLED)
                    self.Entry_Slot1_T2.config(state=DISABLED)
                    self.Entry_Slot1_T3.config(state=DISABLED)
                    self.Entry_Slot1_T4.config(state=DISABLED)
                    self.Entry_Slot1_T5.config(state=DISABLED)

                if self.Page_Inv*3-1 <= self.N_per_category:
                    self.Text_Name_2.config(text=List_per_category[self.Page_Inv*3-2][9])
                    self.var_id_2 = List_per_category[self.Page_Inv*3-2][0]
                    self.var_exist_2 = 1
                    if os.path.exists("Images/" + self.Image_var + "/" + List_per_category[self.Page_Inv*3-2][0] + ".png"):
                        self.Image_2_var = LG.fastimport_imagech(List_per_category[self.Page_Inv*3-2][0], self.Image_var, 2)
                    else:
                        self.Image_2_var = LG.fastimport_imagech("", self.Image_var, 2)
                else:
                    self.Text_Name_2.config(text=LG.translate(self.dict_main, self.dict_actual,"text_44")) 
                    self.Image_2_var = LG.fastimport_imagech("", self.Image_var, 2)  
                    self.var_id_2 = ""
                    self.Entry_Slot2_T1.config(state=DISABLED)
                    self.Entry_Slot2_T2.config(state=DISABLED)
                    self.Entry_Slot2_T3.config(state=DISABLED)
                    self.Entry_Slot2_T4.config(state=DISABLED)
                    self.Entry_Slot2_T5.config(state=DISABLED)
                
                if self.Page_Inv*3-0 <= self.N_per_category:
                    self.Text_Name_3.config(text=List_per_category[self.Page_Inv*3-1][9])
                    self.var_id_3 = List_per_category[self.Page_Inv*3-1][0]
                    self.var_exist_3 = 1
                    if os.path.exists("Images/" + self.Image_var + "/" + List_per_category[self.Page_Inv*3-1][0] + ".png"):
                        self.Image_3_var = LG.fastimport_imagech(List_per_category[self.Page_Inv*3-1][0], self.Image_var, 2)
                    else:
                        self.Image_3_var = LG.fastimport_imagech("", self.Image_var, 2)
                else:
                    self.Text_Name_3.config(text=LG.translate(self.dict_main, self.dict_actual,"text_44"))
                    self.Image_3_var = LG.fastimport_imagech("", self.Image_var, 2)
                    self.var_id_3 = ""
                    self.Entry_Slot3_T1.config(state=DISABLED)
                    self.Entry_Slot3_T2.config(state=DISABLED)
                    self.Entry_Slot3_T3.config(state=DISABLED)
                    self.Entry_Slot3_T4.config(state=DISABLED)
                    self.Entry_Slot3_T5.config(state=DISABLED)

                
                self.Text_Day1.config(text="")
                self.Text_Day2.config(text="")
                self.Text_Day3.config(text="")
        
        if self.Var_Group_3 == 1:
            self.Text_Day1.config(text=LG.translate(self.dict_main, self.dict_actual,"day_1"))
            self.Text_Day2.config(text=LG.translate(self.dict_main, self.dict_actual,"day_2"))
            self.Text_Day3.config(text=LG.translate(self.dict_main, self.dict_actual,"day_3"))
        else:
            self.Text_Day1.config(text="")
            self.Text_Day2.config(text="")
            self.Text_Day3.config(text="")


        self.Image_1.config(image= self.Image_1_var)
        self.Image_2.config(image= self.Image_2_var)
        self.Image_3.config(image= self.Image_3_var)

        text_no_item = "---> 0 (0)" 

        self.Len_List()
        for element_inv in list_inv:
            if self.var_exist_1 == 1:
                if element_inv[0] == self.var_id_1:
                    self.Entry_Slot1_T1_var.set(element_inv[4])
                    self.Entry_Slot1_T2_var.set(element_inv[5])
                    self.Entry_Slot1_T3_var.set(element_inv[6])
                    self.Entry_Slot1_T4_var.set(element_inv[7])
                    self.Entry_Slot1_T5_var.set(element_inv[8])

                    self.Entry_Slot1_T_var.set(self.Calculate_Value(element_inv[self.ini:]))
            else:
                self.Entry_Slot1_T1_var.set(0)
                self.Entry_Slot1_T2_var.set(0)
                self.Entry_Slot1_T3_var.set(0)
                self.Entry_Slot1_T4_var.set(0)
                self.Entry_Slot1_T5_var.set(0)
                self.Entry_Slot1_T_var.set(0)
                
                self.Text2_Slot1_T1.config(text=text_no_item)
                self.Text2_Slot1_T2.config(text=text_no_item)
                self.Text2_Slot1_T3.config(text=text_no_item)
                self.Text2_Slot1_T4.config(text=text_no_item)
                self.Text2_Slot1_T5.config(text=text_no_item)
                self.Text2_Slot1_T.config(text=text_no_item)
            if self.var_exist_2 == 1:
                if element_inv[0] == self.var_id_2:
                    self.Entry_Slot2_T1_var.set(element_inv[4])
                    self.Entry_Slot2_T2_var.set(element_inv[5])
                    self.Entry_Slot2_T3_var.set(element_inv[6])
                    self.Entry_Slot2_T4_var.set(element_inv[7])
                    self.Entry_Slot2_T5_var.set(element_inv[8])
                    self.Entry_Slot2_T_var.set(self.Calculate_Value(element_inv[self.ini:]))

            else:
                self.Entry_Slot2_T1_var.set(0)
                self.Entry_Slot2_T2_var.set(0)
                self.Entry_Slot2_T3_var.set(0)
                self.Entry_Slot2_T4_var.set(0)
                self.Entry_Slot2_T5_var.set(0)
                self.Entry_Slot2_T_var.set(0)
                
                self.Text2_Slot2_T1.config(text=text_no_item)
                self.Text2_Slot2_T2.config(text=text_no_item)
                self.Text2_Slot2_T3.config(text=text_no_item)
                self.Text2_Slot2_T4.config(text=text_no_item)
                self.Text2_Slot2_T5.config(text=text_no_item)
                self.Text2_Slot2_T.config(text=text_no_item)
            if self.var_exist_3 == 1:    
                if element_inv[0] == self.var_id_3:
                    self.Entry_Slot3_T1_var.set(element_inv[4])
                    self.Entry_Slot3_T2_var.set(element_inv[5])
                    self.Entry_Slot3_T3_var.set(element_inv[6])
                    self.Entry_Slot3_T4_var.set(element_inv[7])
                    self.Entry_Slot3_T5_var.set(element_inv[8])
                    self.Entry_Slot3_T_var.set(self.Calculate_Value(element_inv[self.ini:]))

            else:
                self.Entry_Slot3_T1_var.set(0)
                self.Entry_Slot3_T2_var.set(0)
                self.Entry_Slot3_T3_var.set(0)
                self.Entry_Slot3_T4_var.set(0)
                self.Entry_Slot3_T5_var.set(0)
                self.Entry_Slot3_T_var.set(0)

                self.Text2_Slot3_T1.config(text=text_no_item)
                self.Text2_Slot3_T2.config(text=text_no_item)
                self.Text2_Slot3_T3.config(text=text_no_item)
                self.Text2_Slot3_T4.config(text=text_no_item)
                self.Text2_Slot3_T5.config(text=text_no_item)
                self.Text2_Slot3_T.config(text=text_no_item)
        

        self.Show_Text()


    def Format_Text(self, var_tar, var_bld):
        return f"---> {var_tar} ({var_bld})"


    def Len_List(self):
        if self.Page_Category == 1:
            self.ini = 5
            self.times = 4
        elif self.Page_Category == 2:
            self.ini = 5
            self.times = 3
        elif self.Page_Category == 3:
            self.ini = 5
            self.times = 4
        elif self.Page_Category == 4:
            self.ini = 5
            self.times = 3
        elif self.Page_Category == 5:
            self.ini = 4
            self.times = 3
        elif self.Page_Category == 6:
            self.ini = 4
            self.times = 1
        elif self.Page_Category == 7:
            self.ini = 7
            self.times = 1
        elif self.Page_Category == 8:
            self.ini = 8
            self.times = 1

    def Calculate_Value(self, list_number):
        value = 0

        for count,elem in enumerate(list_number):
            value += elem * 3 ** (count)

        return value
    
    
    

    def Reset_Slot_1(self):
        self.s1_t1 = 0
        self.s1_t2 = 0
        self.s1_t3 = 0
        self.s1_t4 = 0
        self.s1_t5 = 0
        self.s1_t = 0

        self.bld_s1_t1 = 0
        self.bld_s1_t2 = 0
        self.bld_s1_t3 = 0
        self.bld_s1_t4 = 0
        self.bld_s1_t5 = 0
        self.bld_s1_t = 0

    def Reset_Slot_2(self):
        self.s2_t1 = 0
        self.s2_t2 = 0
        self.s2_t3 = 0
        self.s2_t4 = 0
        self.s2_t5 = 0
        self.s2_t = 0

        self.bld_s2_t1 = 0
        self.bld_s2_t2 = 0
        self.bld_s2_t3 = 0
        self.bld_s2_t4 = 0
        self.bld_s2_t5 = 0
        self.bld_s2_t = 0

    def Reset_Slot_3(self):
        self.s3_t1 = 0
        self.s3_t2 = 0
        self.s3_t3 = 0
        self.s3_t4 = 0
        self.s3_t5 = 0
        self.s3_t = 0

        self.bld_s3_t1 = 0
        self.bld_s3_t2 = 0
        self.bld_s3_t3 = 0
        self.bld_s3_t4 = 0
        self.bld_s3_t5 = 0
        self.bld_s3_t = 0


    def Show_Text(self):

        self.Reset_Slot_1()
        self.Reset_Slot_2()
        self.Reset_Slot_3()

        if self.Page_Category == 1 or self.Page_Category == 3:
            for elem1 in self.list_to_use:
                if self.var_exist_1 == 1:
                    if elem1[0] == self.var_id_1:
                        self.s1_t1 = 0
                        self.s1_t2 = elem1[1]
                        self.s1_t3 = elem1[2]
                        self.s1_t4 = elem1[3]
                        self.s1_t5 = elem1[4]
                        self.s1_t = self.Calculate_Value(elem1[1:])
                
                if self.var_exist_2 == 1:
                    if elem1[0] == self.var_id_2:
                        self.s2_t1 = 0
                        self.s2_t2 = elem1[1]
                        self.s2_t3 = elem1[2]
                        self.s2_t4 = elem1[3]
                        self.s2_t5 = elem1[4]
                        self.s2_t = self.Calculate_Value(elem1[1:])
                
                if self.var_exist_3 == 1:
                    if elem1[0] == self.var_id_3:
                        self.s3_t1 = 0
                        self.s3_t2 = elem1[1]
                        self.s3_t3 = elem1[2]
                        self.s3_t4 = elem1[3]
                        self.s3_t5 = elem1[4]
                        self.s3_t = self.Calculate_Value(elem1[1:])
            for elem1 in self.list_to_use_bld:
                if self.var_exist_1 == 1:
                    if elem1[0] == self.var_id_1:
                        self.bld_s1_t1 = 0
                        self.bld_s1_t2 = elem1[1]
                        self.bld_s1_t3 = elem1[2]
                        self.bld_s1_t4 = elem1[3]
                        self.bld_s1_t5 = elem1[4]
                        self.bld_s1_t = self.Calculate_Value(elem1[1:])
                
                if self.var_exist_2 == 1:
                    if elem1[0] == self.var_id_2:
                        self.bld_s2_t1 = 0
                        self.bld_s2_t2 = elem1[1]
                        self.bld_s2_t3 = elem1[2]
                        self.bld_s2_t4 = elem1[3]
                        self.bld_s2_t5 = elem1[4]
                        self.bld_s2_t = self.Calculate_Value(elem1[1:])
                
                if self.var_exist_3 == 1:
                    if elem1[0] == self.var_id_3:
                        self.bld_s3_t1 = 0
                        self.bld_s3_t2 = elem1[1]
                        self.bld_s3_t3 = elem1[2]
                        self.bld_s3_t4 = elem1[3]
                        self.bld_s3_t5 = elem1[4]
                        self.bld_s3_t = self.Calculate_Value(elem1[1:])


        if self.Page_Category == 2 or self.Page_Category == 4:
            for elem1 in self.list_to_use:
                if self.var_exist_1 == 1:
                    if elem1[0] == self.var_id_1:
                        self.s1_t1 = 0
                        self.s1_t2 = elem1[1]
                        self.s1_t3 = elem1[2]
                        self.s1_t4 = elem1[3]
                        self.s1_t5 = 0
                        self.s1_t = self.Calculate_Value(elem1[1:])
                
                if self.var_exist_2 == 1:
                    if elem1[0] == self.var_id_2:
                        self.s2_t1 = 0
                        self.s2_t2 = elem1[1]
                        self.s2_t3 = elem1[2]
                        self.s2_t4 = elem1[3]
                        self.s2_t5 = 0
                        self.s2_t = self.Calculate_Value(elem1[1:])
                
                if self.var_exist_3 == 1:
                    if elem1[0] == self.var_id_3:
                        self.s3_t1 = 0
                        self.s3_t2 = elem1[1]
                        self.s3_t3 = elem1[2]
                        self.s3_t4 = elem1[3]
                        self.s3_t5 = 0
                        self.s3_t = self.Calculate_Value(elem1[1:])
            for elem1 in self.list_to_use_bld:
                if self.var_exist_1 == 1:
                    if elem1[0] == self.var_id_1:
                        self.bld_s1_t1 = 0
                        self.bld_s1_t2 = elem1[1]
                        self.bld_s1_t3 = elem1[2]
                        self.bld_s1_t4 = elem1[3]
                        self.bld_s1_t5 = 0
                        self.bld_s1_t = self.Calculate_Value(elem1[1:])
                
                if self.var_exist_2 == 1:
                    if elem1[0] == self.var_id_2:
                        self.bld_s2_t1 = 0
                        self.bld_s2_t2 = elem1[1]
                        self.bld_s2_t3 = elem1[2]
                        self.bld_s2_t4 = elem1[3]
                        self.bld_s2_t5 = 0
                        self.bld_s2_t = self.Calculate_Value(elem1[1:])
                
                if self.var_exist_3 == 1:
                    if elem1[0] == self.var_id_3:
                        self.bld_s3_t1 = 0
                        self.bld_s3_t2 = elem1[1]
                        self.bld_s3_t3 = elem1[2]
                        self.bld_s3_t4 = elem1[3]
                        self.bld_s3_t5 = 0
                        self.bld_s3_t = self.Calculate_Value(elem1[1:])


        if self.Page_Category == 5:
            for elem1 in self.list_to_use:
                if self.var_exist_1 == 1:
                    if elem1[0] == self.var_id_1:
                        self.s1_t1 = elem1[1]
                        self.s1_t2 = elem1[2]
                        self.s1_t3 = elem1[3]
                        self.s1_t4 = 0
                        self.s1_t5 = 0
                        self.s1_t = self.Calculate_Value(elem1[1:])
                
                if self.var_exist_2 == 1:
                    if elem1[0] == self.var_id_2:
                        self.s2_t1 = elem1[1]
                        self.s2_t2 = elem1[2]
                        self.s2_t3 = elem1[3]
                        self.s2_t4 = 0
                        self.s2_t5 = 0
                        self.s2_t = self.Calculate_Value(elem1[1:])
                
                if self.var_exist_3 == 1:
                    if elem1[0] == self.var_id_3:
                        self.s3_t1 = elem1[1]
                        self.s3_t2 = elem1[2]
                        self.s3_t3 = elem1[3]
                        self.s3_t4 = 0
                        self.s3_t5 = 0
                        self.s3_t = self.Calculate_Value(elem1[1:])
            for elem1 in self.list_to_use_bld:
                if self.var_exist_1 == 1:
                    if elem1[0] == self.var_id_1:
                        self.bld_s1_t1 = elem1[1]
                        self.bld_s1_t2 = elem1[2]
                        self.bld_s1_t3 = elem1[3]
                        self.bld_s1_t4 = 0
                        self.bld_s1_t5 = 0
                        self.bld_s1_t = self.Calculate_Value(elem1[1:])
                
                if self.var_exist_2 == 1:
                    if elem1[0] == self.var_id_2:
                        self.bld_s2_t1 = elem1[1]
                        self.bld_s2_t2 = elem1[2]
                        self.bld_s2_t3 = elem1[3]
                        self.bld_s2_t4 = 0
                        self.bld_s2_t5 = 0
                        self.bld_s2_t = self.Calculate_Value(elem1[1:])
                
                if self.var_exist_3 == 1:
                    if elem1[0] == self.var_id_3:
                        self.bld_s3_t1 = elem1[1]
                        self.bld_s3_t2 = elem1[2]
                        self.bld_s3_t3 = elem1[3]
                        self.bld_s3_t4 = 0
                        self.bld_s3_t5 = 0
                        self.bld_s3_t = self.Calculate_Value(elem1[1:])


        if self.Page_Category == 6:
            for elem1 in self.list_to_use:
                if self.var_exist_1 == 1:
                    if elem1[0] == self.var_id_1:
                        self.s1_t1 = elem1[1]
                        self.s1_t2 = 0
                        self.s1_t3 = 0
                        self.s1_t4 = 0
                        self.s1_t5 = 0
                        self.s1_t = self.Calculate_Value(elem1[1:])
                
                if self.var_exist_2 == 1:
                    if elem1[0] == self.var_id_2:
                        self.s2_t1 = elem1[1]
                        self.s2_t2 = 0
                        self.s2_t3 = 0
                        self.s2_t4 = 0
                        self.s2_t5 = 0
                        self.s2_t = self.Calculate_Value(elem1[1:])
                
                if self.var_exist_3 == 1:
                    if elem1[0] == self.var_id_3:
                        self.s3_t1 = elem1[1]
                        self.s3_t2 = 0
                        self.s3_t3 = 0
                        self.s3_t4 = 0
                        self.s3_t5 = 0
                        self.s3_t = self.Calculate_Value(elem1[1:])
            for elem1 in self.list_to_use_bld:
                if self.var_exist_1 == 1:
                    if elem1[0] == self.var_id_1:
                        self.bld_s1_t1 = elem1[1]
                        self.bld_s1_t2 = 0
                        self.bld_s1_t3 = 0
                        self.bld_s1_t4 = 0
                        self.bld_s1_t5 = 0
                        self.bld_s1_t = self.Calculate_Value(elem1[1:])
                
                if self.var_exist_2 == 1:
                    if elem1[0] == self.var_id_2:
                        self.bld_s2_t1 = elem1[1]
                        self.bld_s2_t2 = 0
                        self.bld_s2_t3 = 0
                        self.bld_s2_t4 = 0
                        self.bld_s2_t5 = 0
                        self.bld_s2_t = self.Calculate_Value(elem1[1:])
                
                if self.var_exist_3 == 1:
                    if elem1[0] == self.var_id_3:
                        self.bld_s3_t1 = elem1[1]
                        self.bld_s3_t2 = 0
                        self.bld_s3_t3 = 0
                        self.bld_s3_t4 = 0
                        self.bld_s3_t5 = 0
                        self.bld_s3_t = self.Calculate_Value(elem1[1:])


        if self.Page_Category == 7:
            for elem1 in self.list_to_use:
                if self.var_exist_1 == 1:
                    if elem1[0] == self.var_id_1:
                        self.s1_t1 = 0
                        self.s1_t2 = 0
                        self.s1_t3 = 0
                        self.s1_t4 = elem1[1]
                        self.s1_t5 = 0
                        self.s1_t = self.Calculate_Value(elem1[1:])
                
                if self.var_exist_2 == 1:
                    if elem1[0] == self.var_id_2:
                        self.s2_t1 = 0
                        self.s2_t2 = 0
                        self.s2_t3 = 0
                        self.s2_t4 = elem1[1]
                        self.s2_t5 = 0
                        self.s2_t = self.Calculate_Value(elem1[1:])
                
                if self.var_exist_3 == 1:
                    if elem1[0] == self.var_id_3:
                        self.s3_t1 = 0
                        self.s3_t2 = 0
                        self.s3_t3 = 0
                        self.s3_t4 = elem1[1]
                        self.s3_t5 = 0
                        self.s3_t = self.Calculate_Value(elem1[1:])
            for elem1 in self.list_to_use_bld:
                if self.var_exist_1 == 1:
                    if elem1[0] == self.var_id_1:
                        self.bld_s1_t1 = 0
                        self.bld_s1_t2 = 0
                        self.bld_s1_t3 = 0
                        self.bld_s1_t4 = elem1[1]
                        self.bld_s1_t5 = 0
                        self.bld_s1_t = self.Calculate_Value(elem1[1:])
                
                if self.var_exist_2 == 1:
                    if elem1[0] == self.var_id_2:
                        self.bld_s2_t1 = 0
                        self.bld_s2_t2 = 0
                        self.bld_s2_t3 = 0
                        self.bld_s2_t4 = elem1[1]
                        self.bld_s2_t5 = 0
                        self.bld_s2_t = self.Calculate_Value(elem1[1:])
                
                if self.var_exist_3 == 1:
                    if elem1[0] == self.var_id_3:
                        self.bld_s3_t1 = 0
                        self.bld_s3_t2 = 0
                        self.bld_s3_t3 = 0
                        self.bld_s3_t4 = elem1[1]
                        self.bld_s3_t5 = 0
                        self.bld_s3_t = self.Calculate_Value(elem1[1:])


        if self.Page_Category == 8:
            for elem1 in self.list_to_use:
                if self.var_exist_1 == 1:
                    if elem1[0] == self.var_id_1:
                        self.s1_t1 = 0
                        self.s1_t2 = 0
                        self.s1_t3 = 0
                        self.s1_t4 = 0
                        self.s1_t5 = elem1[1]
                        self.s1_t = self.Calculate_Value(elem1[1:])
                
                if self.var_exist_2 == 1:
                    if elem1[0] == self.var_id_2:
                        self.s2_t1 = 0
                        self.s2_t2 = 0
                        self.s2_t3 = 0
                        self.s2_t4 = 0
                        self.s2_t5 = elem1[1]
                        self.s2_t = self.Calculate_Value(elem1[1:])
                
                if self.var_exist_3 == 1:
                    if elem1[0] == self.var_id_3:
                        self.s3_t1 = 0
                        self.s3_t2 = 0
                        self.s3_t3 = 0
                        self.s3_t4 = 0
                        self.s3_t5 = elem1[1]
                        self.s3_t = self.Calculate_Value(elem1[1:])
            for elem1 in self.list_to_use_bld:
                if self.var_exist_1 == 1:
                    if elem1[0] == self.var_id_1:
                        self.bld_s1_t1 = 0
                        self.bld_s1_t2 = 0
                        self.bld_s1_t3 = 0
                        self.bld_s1_t4 = 0
                        self.bld_s1_t5 = elem1[1]
                        self.bld_s1_t = self.Calculate_Value(elem1[1:])
                
                if self.var_exist_2 == 1:
                    if elem1[0] == self.var_id_2:
                        self.bld_s2_t1 = 0
                        self.bld_s2_t2 = 0
                        self.bld_s2_t3 = 0
                        self.bld_s2_t4 = 0
                        self.bld_s2_t5 = elem1[1]
                        self.bld_s2_t = self.Calculate_Value(elem1[1:])
                
                if self.var_exist_3 == 1:
                    if elem1[0] == self.var_id_3:
                        self.bld_s3_t1 = 0
                        self.bld_s3_t2 = 0
                        self.bld_s3_t3 = 0
                        self.bld_s3_t4 = 0
                        self.bld_s3_t5 = elem1[1]
                        self.bld_s3_t = self.Calculate_Value(elem1[1:])

#---------------------------------------

        self.Text2_Slot1_T1_var.set(self.Format_Text(self.s1_t1, self.bld_s1_t1))
        self.Text2_Slot1_T2_var.set(self.Format_Text(self.s1_t2, self.bld_s1_t2))
        self.Text2_Slot1_T3_var.set(self.Format_Text(self.s1_t3, self.bld_s1_t3))
        self.Text2_Slot1_T4_var.set(self.Format_Text(self.s1_t4, self.bld_s1_t4))
        self.Text2_Slot1_T5_var.set(self.Format_Text(self.s1_t5, self.bld_s1_t5))
        self.Text2_Slot1_T_var.set(self.Format_Text(self.s1_t, self.bld_s1_t))

        self.Text2_Slot2_T1_var.set(self.Format_Text(self.s2_t1, self.bld_s2_t1))
        self.Text2_Slot2_T2_var.set(self.Format_Text(self.s2_t2, self.bld_s2_t2))
        self.Text2_Slot2_T3_var.set(self.Format_Text(self.s2_t3, self.bld_s2_t3))
        self.Text2_Slot2_T4_var.set(self.Format_Text(self.s2_t4, self.bld_s2_t4))
        self.Text2_Slot2_T5_var.set(self.Format_Text(self.s2_t5, self.bld_s2_t5))
        self.Text2_Slot2_T_var.set(self.Format_Text(self.s2_t, self.bld_s2_t))

        self.Text2_Slot3_T1_var.set(self.Format_Text(self.s3_t1, self.bld_s3_t1))
        self.Text2_Slot3_T2_var.set(self.Format_Text(self.s3_t2, self.bld_s3_t2))
        self.Text2_Slot3_T3_var.set(self.Format_Text(self.s3_t3, self.bld_s3_t3))
        self.Text2_Slot3_T4_var.set(self.Format_Text(self.s3_t4, self.bld_s3_t4))
        self.Text2_Slot3_T5_var.set(self.Format_Text(self.s3_t5, self.bld_s3_t5))
        self.Text2_Slot3_T_var.set(self.Format_Text(self.s3_t, self.bld_s3_t))


        if self.var_exist_1 == 1:
            if self.Entry_Slot1_T_var.get() >= self.s1_t:
                self.Text3_Slot1_var.set(LG.button_text(self.dict_main, self.dict_actual,"text_51"))
            elif self.Entry_Slot1_T_var.get() >= self.bld_s1_t:
                self.Text3_Slot1_var.set(LG.button_text(self.dict_main, self.dict_actual,"text_52a", "text_52b"))
            else:
                self.Text3_Slot1_var.set(LG.button_text(self.dict_main, self.dict_actual,"text_53"))
        else:
            self.Text3_Slot1_var.set("")
        
        if self.var_exist_2 == 1:
            if self.Entry_Slot2_T_var.get() >= self.s2_t:
                self.Text3_Slot2_var.set(LG.button_text(self.dict_main, self.dict_actual,"text_51"))
            elif self.Entry_Slot2_T_var.get() >= self.bld_s2_t:
                self.Text3_Slot2_var.set(LG.button_text(self.dict_main, self.dict_actual,"text_52a", "text_52b"))
            else:
                self.Text3_Slot2_var.set(LG.button_text(self.dict_main, self.dict_actual,"text_53"))
        else:
            self.Text3_Slot2_var.set("")

        if self.var_exist_3 == 1:
            if self.Entry_Slot3_T_var.get() >= self.s3_t:

                self.Text3_Slot3_var.set(LG.button_text(self.dict_main, self.dict_actual,"text_51"))
            elif self.Entry_Slot3_T_var.get() >= self.bld_s3_t:
                self.Text3_Slot3_var.set(LG.button_text(self.dict_main, self.dict_actual,"text_52a", "text_52b"))
            else:
                self.Text3_Slot3_var.set(LG.button_text(self.dict_main, self.dict_actual,"text_53"))
        else:
            self.Text3_Slot3_var.set("")


    def Change_Page(self, change):
        self.Page_Inv += change
        self.Text_Number_Page.config(text=LG.translate(self.dict_main, self.dict_actual,"button_3") + str(self.Page_Inv))
    
        self.Button_Previous.config(state=NORMAL)
        self.Button_Next.config(state=NORMAL)
        if self.Page_Inv == 1:
            self.Button_Previous.config(state=DISABLED)
        elif self.Page_Inv == self.Max_Pages:
            self.Button_Next.config(state=DISABLED)
        self.Config_Entries()
        self.Show_Data()

    def Save_Data(self, value):
        list_error = Ef.Fix_Errors_inv(self.Entry_Slot1_T1_var, self.Entry_Slot1_T2_var, self.Entry_Slot1_T3_var, self.Entry_Slot1_T4_var, self.Entry_Slot1_T5_var, self.Entry_Slot2_T1_var, self.Entry_Slot2_T2_var, self.Entry_Slot2_T3_var, self.Entry_Slot2_T4_var, self.Entry_Slot2_T5_var, self.Entry_Slot3_T1_var, self.Entry_Slot3_T2_var, self.Entry_Slot3_T3_var, self.Entry_Slot3_T4_var, self.Entry_Slot3_T5_var)

        if value:
            if len(list_error) == 0:
                Save_question = MessageBox.askokcancel(LG.translate(self.dict_main, self.dict_actual, "message_1"), LG.translate(self.dict_main, self.dict_actual, "message_2"))
                if Save_question:
                    conexion4 = sqlite3.connect("DB SQL/genshin_db.db")

                    if self.var_exist_1 == 1:

                        conexion4.execute(f"""update user_inv set 
                        T1 = {self.Entry_Slot1_T1_var.get()},
                        T2 = {self.Entry_Slot1_T2_var.get()},
                        T3 = {self.Entry_Slot1_T3_var.get()},
                        T4 = {self.Entry_Slot1_T4_var.get()},
                        T5 = {self.Entry_Slot1_T5_var.get()}
                        where Name='{self.var_id_1}'""")
                        conexion4.commit()
                    
                    if self.var_exist_2 == 1:

                        conexion4.execute(f"""update user_inv set 
                        T1 = {self.Entry_Slot2_T1_var.get()},
                        T2 = {self.Entry_Slot2_T2_var.get()},
                        T3 = {self.Entry_Slot2_T3_var.get()},
                        T4 = {self.Entry_Slot2_T4_var.get()},
                        T5 = {self.Entry_Slot2_T5_var.get()}
                        where Name='{self.var_id_2}'""")
                        conexion4.commit()
                    
                    if self.var_exist_3 == 1:

                        conexion4.execute(f"""update user_inv set 
                        T1 = {self.Entry_Slot3_T1_var.get()},
                        T2 = {self.Entry_Slot3_T2_var.get()},
                        T3 = {self.Entry_Slot3_T3_var.get()},
                        T4 = {self.Entry_Slot3_T4_var.get()},
                        T5 = {self.Entry_Slot3_T5_var.get()}
                        where Name='{self.var_id_3}'""")
                        conexion4.commit()
                    conexion4.close()
                    self.Change_Page(0)
                    MessageBox.showinfo(LG.translate(self.dict_main, self.dict_actual, "message_5"), LG.translate(self.dict_main, self.dict_actual, "message_6"))
            elif len(list_error) == 1:
                MessageBox.showerror(LG.translate(self.dict_main, self.dict_actual, "message_3"), LG.translate(self.dict_main, self.dict_actual, "message_4") + "\n" + LG.translate(self.dict_main, self.dict_actual, "error_q_1") + "\n" + Ef.error_list(self.dict_main, self.dict_actual, list_error))
            else:
                MessageBox.showerror(LG.translate(self.dict_main, self.dict_actual, "message_3"), LG.translate(self.dict_main, self.dict_actual, "message_4") + "\n" + LG.translate(self.dict_main, self.dict_actual, "error_q_2a") + str(len(list_error)) + LG.translate(self.dict_main, self.dict_actual, "error_q_2b") + "\n" + Ef.error_list(self.dict_main, self.dict_actual, list_error))
        else:
            self.Change_Page(0)
            MessageBox.showinfo(LG.translate(self.dict_main, self.dict_actual, "message_7"), LG.translate(self.dict_main, self.dict_actual, "message_8"))

