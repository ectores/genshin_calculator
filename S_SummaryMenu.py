from tkinter import *
from tkinter.ttk import Combobox
import sqlite3
import math
import Languages as LG
import Number_format as Nf


class Sheet_SummaryMenu():
    def __init__(self, Multiple_Page, Invcal):
        self.Pagina_Multiple = Multiple_Page
        self.Invcal = Invcal

        self.Page = Frame(Multiple_Page)
        self.start = 0

        self.dict_actual = LG.create_language(language=LG.language_actual())
        self.dict_main = LG.create_language()

        self.Text1_Filter = Label(self.Page, text=LG.translate(self.dict_main, self.dict_actual,"text_54"))
        self.Text2_Filter = Label(self.Page, text=LG.translate(self.dict_main, self.dict_actual,"text_55"))

        self.Text1_Filter.place(x=130, y=35, anchor=E)
        self.Text2_Filter.place(x=130, y=70, anchor=E)

        self.List1_Filter_var = StringVar()
        self.List1_Filter = Combobox(self.Page,values= [LG.translate(self.dict_main, self.dict_actual,"type_domain_1"), LG.translate(self.dict_main, self.dict_actual,"type_domain_2")], textvariable=self.List1_Filter_var, state="readonly", width=15)
        self.List1_Filter.bind("<<ComboboxSelected>>", self.Update_List_Button)
        self.List1_Filter_var.set("-")
        self.List2_Filter_var = StringVar()
        self.List2_Filter = Combobox(self.Page,values= [LG.translate(self.dict_main, self.dict_actual,"status_1"), LG.translate(self.dict_main, self.dict_actual,"status_2")], textvariable=self.List2_Filter_var, state="readonly", width=15)
        self.List2_Filter.bind("<<ComboboxSelected>>", self.Update_List_Button)
        self.List2_Filter_var.set("-")

        self.List1_Filter.place(x=140, y=35, anchor=W)
        self.List2_Filter.place(x=140, y=70, anchor=W)

        self.Marco1a = Label(self.Page)
        self.Marco1a.config(relief="groove", width=36, height=10)
        self.Marco1a.place(x=430, y=20, anchor=N) 

        self.Marco1b = Label(self.Page)
        self.Marco1b.config(relief="groove", width=36, height=10)
        self.Marco1b.place(x=713, y=20, anchor=N) 

        self.Text1_Marco1a = Label(self.Page, text=LG.translate(self.dict_main, self.dict_actual,"text_57"))
        self.Text1_Marco1b = Label(self.Page, text=LG.translate(self.dict_main, self.dict_actual,"text_56"))

        self.Text1_Marco1a.place(x=430, y=30, anchor=N)
        self.Text1_Marco1b.place(x=713, y=30, anchor=N)

        self.Text_Image1_Marco1a_var = IntVar()
        self.Text_Image1_Marco1a = Label(self.Page, textvariable=self.Text_Image1_Marco1a_var)
        self.Text_Image1_Marco1a.place(x=360, y=85, anchor=N)
        self.Text_Image2_Marco1a_var = IntVar()
        self.Text_Image2_Marco1a = Label(self.Page, textvariable=self.Text_Image2_Marco1a_var)
        self.Text_Image2_Marco1a.place(x=430, y=85, anchor=N)
        self.Text_Image3_Marco1a_var = IntVar()
        self.Text_Image3_Marco1a = Label(self.Page, textvariable=self.Text_Image3_Marco1a_var)
        self.Text_Image3_Marco1a.place(x=500, y=85, anchor=N)
        self.Text_Image4_Marco1a_var = IntVar()
        self.Text_Image4_Marco1a = Label(self.Page, textvariable=self.Text_Image4_Marco1a_var)
        self.Text_Image4_Marco1a.place(x=360, y=140, anchor=N)
        self.Text_Image5_Marco1a_var = IntVar()
        self.Text_Image5_Marco1a = Label(self.Page, textvariable=self.Text_Image5_Marco1a_var)
        self.Text_Image5_Marco1a.place(x=430, y=140, anchor=N)
        self.Text_Image6_Marco1a_var = IntVar()
        self.Text_Image6_Marco1a = Label(self.Page, textvariable=self.Text_Image6_Marco1a_var)
        self.Text_Image6_Marco1a.place(x=500, y=140, anchor=N)

        self.Text_Image1_Marco1b_var = IntVar()
        self.Text_Image1_Marco1b = Label(self.Page, textvariable=self.Text_Image1_Marco1b_var)
        self.Text_Image1_Marco1b.place(x=643, y=85, anchor=N)
        self.Text_Image2_Marco1b_var = IntVar()
        self.Text_Image2_Marco1b = Label(self.Page, textvariable=self.Text_Image2_Marco1b_var)
        self.Text_Image2_Marco1b.place(x=713, y=85, anchor=N)
        self.Text_Image3_Marco1b_var = IntVar()
        self.Text_Image3_Marco1b = Label(self.Page, textvariable=self.Text_Image3_Marco1b_var)
        self.Text_Image3_Marco1b.place(x=783, y=85, anchor=N)
        self.Text_Image4_Marco1b_var = IntVar()
        self.Text_Image4_Marco1b = Label(self.Page, textvariable=self.Text_Image4_Marco1b_var)
        self.Text_Image4_Marco1b.place(x=643, y=140, anchor=N)
        self.Text_Image5_Marco1b_var = IntVar()
        self.Text_Image5_Marco1b = Label(self.Page, textvariable=self.Text_Image5_Marco1b_var)
        self.Text_Image5_Marco1b.place(x=713, y=140, anchor=N)
        self.Text_Image6_Marco1b_var = IntVar()
        self.Text_Image6_Marco1b = Label(self.Page, textvariable=self.Text_Image6_Marco1b_var)
        self.Text_Image6_Marco1b.place(x=783, y=140, anchor=N)


        self.Marco2 = Label(self.Page)
        self.Marco3 = Label(self.Page)
        self.Marco4 = Label(self.Page)

        self.Text1_Marco2 = Label(self.Page)
        self.Text1_Marco3 = Label(self.Page)
        self.Text1_Marco4 = Label(self.Page)

        self.Text1_Marco2.place(x=27, y=210, anchor=W)
        self.Text1_Marco3.place(x=310, y=210, anchor=W)
        self.Text1_Marco4.place(x=593, y=210, anchor=W)

        self.Text2_Marco2_var = StringVar()
        self.Text2_Marco2 = Label(self.Page, textvariable=self.Text2_Marco2_var, justify=LEFT)
        self.Text2_Marco3_var = StringVar()
        self.Text2_Marco3 = Label(self.Page, textvariable=self.Text2_Marco3_var, justify=LEFT)
        self.Text2_Marco4_var = StringVar()
        self.Text2_Marco4 = Label(self.Page, textvariable=self.Text2_Marco4_var, justify=LEFT)

        self.Text3_Marco2_var = StringVar()
        self.Text3_Marco2 = Label(self.Page, textvariable=self.Text3_Marco2_var)
        self.Text3_Marco3_var = StringVar()
        self.Text3_Marco3 = Label(self.Page, textvariable=self.Text3_Marco3_var)
        self.Text3_Marco4_var = StringVar()
        self.Text3_Marco4 = Label(self.Page, textvariable=self.Text3_Marco4_var)

        self.Text4_Marco2_var = StringVar()
        self.Text4_Marco2 = Label(self.Page, textvariable=self.Text4_Marco2_var)
        self.Text4_Marco3_var = StringVar()
        self.Text4_Marco3 = Label(self.Page, textvariable=self.Text4_Marco3_var)
        self.Text4_Marco4_var = StringVar()
        self.Text4_Marco4 = Label(self.Page, textvariable=self.Text4_Marco4_var)

        self.Text5_Marco2_var = StringVar()
        self.Text5_Marco2 = Label(self.Page, textvariable=self.Text5_Marco2_var)
        self.Text5_Marco3_var = StringVar()
        self.Text5_Marco3 = Label(self.Page, textvariable=self.Text5_Marco3_var)
        self.Text5_Marco4_var = StringVar()
        self.Text5_Marco4 = Label(self.Page, textvariable=self.Text5_Marco4_var)
        
       
        self.Load_Images()

        self.Image1_Marco2 = Label(self.Page, image=self.Image_Resin_var)
        self.Image2_Marco2 = Label(self.Page, image=self.Image_Resin_var)
        self.Image3_Marco2 = Label(self.Page, image=self.Image_Resin_var)
        self.Image4_Marco2 = Label(self.Page, image=self.Image_Mora_var)
        self.Image5_Marco2 = Label(self.Page, image=self.Image_Character_var)
        self.Image6_Marco2 = Label(self.Page, image=self.Image_Book_var)

        self.Image1_Marco3 = Label(self.Page, image=self.Image_Resin_var)
        self.Image2_Marco3 = Label(self.Page, image=self.Image_Resin_var)
        self.Image3_Marco3 = Label(self.Page, image=self.Image_Resin_var)
        self.Image4_Marco3 = Label(self.Page, image=self.Image_Mora_var)
        self.Image5_Marco3 = Label(self.Page, image=self.Image_Character_var)
        self.Image6_Marco3 = Label(self.Page, image=self.Image_Book_var)

        self.Image1_Marco4 = Label(self.Page, image=self.Image_Resin_var)
        self.Image2_Marco4 = Label(self.Page, image=self.Image_Resin_var)
        self.Image3_Marco4 = Label(self.Page, image=self.Image_Resin_var)
        self.Image4_Marco4 = Label(self.Page, image=self.Image_Mora_var)
        self.Image5_Marco4 = Label(self.Page, image=self.Image_Character_var)
        self.Image6_Marco4 = Label(self.Page, image=self.Image_Book_var)

        self.Summary_All()


    def Load_Images(self):

        self.Image_Card_var = LG.fastimport_imagech("card_character", "others", 3)
        self.Image_Resin_var = LG.fastimport_imagech("condensed_resin", "others", 3)
        self.Image_Mora_var = LG.fastimport_imagech("mora", "others", 3)
        self.Image_Character_var = LG.fastimport_imagech("xp_character", "others", 3)
        self.Image_Weapon_var = LG.fastimport_imagech("xp_weapon", "others", 3)
        self.Image_Mat_var = LG.fastimport_imagech("mat_domain_weapon_04", "weapon_asc", 3)
        self.Image_Book_var = LG.fastimport_imagech("mat_domain_book_01", "talent", 3)

        
        self.Image1_Marco1a = Label(self.Page, image=self.Image_Mora_var)
        self.Image2_Marco1a = Label(self.Page, image=self.Image_Character_var)
        self.Image3_Marco1a = Label(self.Page, text=LG.translate(self.dict_main, self.dict_actual,"text_58"))
        self.Image4_Marco1a = Label(self.Page, image=self.Image_Resin_var)
        self.Image5_Marco1a = Label(self.Page, image=self.Image_Resin_var)
        self.Image6_Marco1a = Label(self.Page, image=self.Image_Weapon_var)
    

        self.Image1_Marco1b = Label(self.Page, image=self.Image_Mora_var)
        self.Image2_Marco1b = Label(self.Page, image=self.Image_Character_var)
        self.Image3_Marco1b = Label(self.Page, text=LG.translate(self.dict_main, self.dict_actual,"text_58"))
        self.Image4_Marco1b = Label(self.Page, image=self.Image_Resin_var)
        self.Image5_Marco1b = Label(self.Page, image=self.Image_Resin_var)
        self.Image6_Marco1b = Label(self.Page, image=self.Image_Weapon_var)


        self.Image1_Marco1a.place(x=360,y=50, anchor=N)
        self.Image2_Marco1a.place(x=430,y=50, anchor=N)
        self.Image3_Marco1a.place(x=500,y=57, anchor=N)

        self.Image4_Marco1a.place(x=360,y=105, anchor=N)
        self.Image5_Marco1a.place(x=430,y=105, anchor=N)
        self.Image6_Marco1a.place(x=500,y=105, anchor=N)

        self.Image1_Marco1b.place(x=643,y=50, anchor=N)
        self.Image2_Marco1b.place(x=713,y=50, anchor=N)
        self.Image3_Marco1b.place(x=783,y=57, anchor=N)

        self.Image4_Marco1b.place(x=643,y=105, anchor=N)
        self.Image5_Marco1b.place(x=713,y=105, anchor=N)
        self.Image6_Marco1b.place(x=783,y=105, anchor=N)


        
    def Load_Images_Dynamic(self):


        self.Image1_Marco2.place(x=162,y=200)
        self.Image2_Marco2.place(x=197,y=200)
        self.Image3_Marco2.place(x=232,y=200)
        self.Image4_Marco2.place(x=162,y=230)
        self.Image5_Marco2.place(x=197,y=230)
        self.Image6_Marco2.place(x=232,y=230)

        self.Image1_Marco3.place(x=445,y=200)
        self.Image2_Marco3.place(x=480,y=200)
        self.Image3_Marco3.place(x=515,y=200)
        self.Image4_Marco3.place(x=445,y=230)
        self.Image5_Marco3.place(x=480,y=230)
        self.Image6_Marco3.place(x=515,y=230)

        self.Image1_Marco4.place(x=728,y=200)
        self.Image2_Marco4.place(x=763,y=200)
        self.Image3_Marco4.place(x=798,y=200)
        self.Image4_Marco4.place(x=728,y=230)
        self.Image5_Marco4.place(x=763,y=230)
        self.Image6_Marco4.place(x=798,y=230)

        


    def Summary_All(self):
        

        conexion1 = sqlite3.connect("DB SQL/genshin_db.db")
        query1 = conexion1.execute("select Build, sum(XP_Character), sum(XP_Weapon), sum(Mora_Ascension + Mora_Talent + Mora_Weapon_Ascension + XP_Character*0.2 + XP_Weapon*0.1) as Mora from user group by Build")
        conexion1.commit()

        query1_values = query1.fetchall()

        try:
            var1a=query1_values[0][3] + query1_values[1][3]
        except:
            try:
                var1a=query1_values[0][3]
            except:
                var1a=0

        
        try:
            var2a=query1_values[0][1] + query1_values[1][1]
        except:
            try:
                var2a=query1_values[0][1]
            except:
                var2a=0

        
        try:
            var3a=query1_values[0][2] + query1_values[1][2]
        except:
            try:
                var3a=query1_values[0][2]
            except:
                var3a=0

        try:
            var1b=query1_values[1][3]
        except:
            var1b=0
        
        try:
            var1b=query1_values[1][3]
        except:
            var1b=0
        
        try:
            var2b=query1_values[1][1]
        except:
            var2b=0
        
        try:
            var3b=query1_values[1][2]
        except:
            var3b=0


        # var2a=query1_values[0][1] + query1_values[1][1]
        # var3a=query1_values[0][2] + query1_values[1][2]

        # var1b=query1_values[1][3]
        # var2b=query1_values[1][1]
        # var3b=query1_values[1][2]


        self.Text_Image1_Marco1a_var.set(Nf.format_point(var1a))
        self.Text_Image2_Marco1a_var.set(Nf.format_point(var2a))
        self.Text_Image3_Marco1a_var.set(Nf.format_point(var3a))

        self.Text_Image4_Marco1a_var.set(Nf.format_point(math.ceil(var1a/120000)))
        self.Text_Image5_Marco1a_var.set(Nf.format_point(math.ceil(var2a/245000)))
        self.Text_Image6_Marco1a_var.set(Nf.format_point(math.ceil(var3a/10000)))


        self.Text_Image1_Marco1b_var.set(Nf.format_point(var1b))
        self.Text_Image2_Marco1b_var.set(Nf.format_point(var2b))
        self.Text_Image3_Marco1b_var.set(Nf.format_point(var3b))

        self.Text_Image4_Marco1b_var.set(Nf.format_point(math.ceil(var1b/120000)))
        self.Text_Image5_Marco1b_var.set(Nf.format_point(math.ceil(var2b/245000)))
        self.Text_Image6_Marco1b_var.set(Nf.format_point(math.ceil(var3b/10000)))


    def Load_Marco(self):

        self.Marco2.config(width=36, height=24, relief="groove")
        self.Marco3.config(width=36, height=24, relief="groove")
        self.Marco4.config(width=36, height=24, relief="groove")

        self.Marco2.place(x=147, y=190, anchor=N)
        self.Marco3.place(x=430, y=190, anchor=N)
        self.Marco4.place(x=713, y=190, anchor=N)
        
        self.Text1_Marco2.config(text=LG.translate(self.dict_main, self.dict_actual,"day_1"))
        self.Text1_Marco3.config(text=LG.translate(self.dict_main, self.dict_actual,"day_2"))
        self.Text1_Marco4.config(text=LG.translate(self.dict_main, self.dict_actual,"day_3"))

        self.Text2_Marco2.place(x=27, y=270)
        self.Text2_Marco3.place(x=310, y=270)
        self.Text2_Marco4.place(x=593, y=270)

        self.Text3_Marco2.place(x=152, y=270)
        self.Text3_Marco3.place(x=435, y=270)
        self.Text3_Marco4.place(x=718, y=270)

        self.Text4_Marco2.place(x=187, y=270)
        self.Text4_Marco3.place(x=470, y=270)
        self.Text4_Marco4.place(x=753, y=270)

        self.Text5_Marco2.place(x=222, y=270)
        self.Text5_Marco3.place(x=505, y=270)
        self.Text5_Marco4.place(x=788, y=270)

    def Summary_day(self):

        #Query Total
        build = "status_1"

        list_day1 = []
        list_day2 = []
        list_day3 = []

        list_unic_day1 = set()
        list_unic_day2 = set()
        list_unic_day3 = set()

        if LG.translate_inv(self.List2_Filter_var.get()) == "status_2":
            build= "status_2"
        
        var_book = 1

        for elem in self.query2_values:
            if build == "status_1":
                if elem[3] == 1:
                    
                    list_day1.append([self.dict_actual[elem[0]], self.dict_actual[elem[2]], math.ceil(self.Invcal.Calculate_Value([elem[4], elem[5], elem[6]])/var_book), math.ceil(elem[7]/120000), math.ceil(elem[8]/245000)])
                    list_unic_day1.add(self.dict_actual[elem[2]])
                elif elem[3] == 2:
                    list_day2.append([self.dict_actual[elem[0]], self.dict_actual[elem[2]], math.ceil(self.Invcal.Calculate_Value([elem[4], elem[5], elem[6]])/var_book), math.ceil(elem[7]/120000), math.ceil(elem[8]/245000)])
                    list_unic_day2.add(self.dict_actual[elem[2]])
                elif elem[3] == 3:
                    list_day3.append([self.dict_actual[elem[0]], self.dict_actual[elem[2]], math.ceil(self.Invcal.Calculate_Value([elem[4], elem[5], elem[6]])/var_book), math.ceil(elem[7]/120000), math.ceil(elem[8]/245000)])
                    list_unic_day3.add(self.dict_actual[elem[2]])
            elif build == "status_2":
                if elem[3] == 1 and elem[1] == build:
                    list_day1.append([self.dict_actual[elem[0]], self.dict_actual[elem[2]], math.ceil(self.Invcal.Calculate_Value([elem[4], elem[5], elem[6]])/var_book), math.ceil(elem[7]/120000), math.ceil(elem[8]/245000)])
                    list_unic_day1.add(self.dict_actual[elem[2]])
                elif elem[3] == 2 and elem[1] == build:
                    list_day2.append([self.dict_actual[elem[0]], self.dict_actual[elem[2]], math.ceil(self.Invcal.Calculate_Value([elem[4], elem[5], elem[6]])/var_book), math.ceil(elem[7]/120000), math.ceil(elem[8]/245000)])
                    list_unic_day2.add(self.dict_actual[elem[2]])
                elif elem[3] == 3 and elem[1] == build:
                    list_day3.append([self.dict_actual[elem[0]], self.dict_actual[elem[2]], math.ceil(self.Invcal.Calculate_Value([elem[4], elem[5], elem[6]])/var_book), math.ceil(elem[7]/120000), math.ceil(elem[8]/245000)])
                    list_unic_day3.add(self.dict_actual[elem[2]])


        
        list_day1.sort(key=lambda x: x[1])
        list_day2.sort(key=lambda x: x[1])
        list_day3.sort(key=lambda x: x[1])

        list_unic_day1 = sorted(list_unic_day1)
        list_unic_day2 = sorted(list_unic_day2)
        list_unic_day3 = sorted(list_unic_day3)

        self.Text2_Marco2_var.set(self.List_Text(list_unic_day1, list_day1, "text", 0)) 
        self.Text2_Marco3_var.set(self.List_Text(list_unic_day2, list_day2, "text", 0)) 
        self.Text2_Marco4_var.set(self.List_Text(list_unic_day3, list_day3, "text", 0))

        self.Text3_Marco2_var.set(self.List_Text(list_unic_day1, list_day1, "number", 3)) 
        self.Text3_Marco3_var.set(self.List_Text(list_unic_day2, list_day2, "number", 3)) 
        self.Text3_Marco4_var.set(self.List_Text(list_unic_day3, list_day3, "number", 3))

        self.Text4_Marco2_var.set(self.List_Text(list_unic_day1, list_day1, "number", 4)) 
        self.Text4_Marco3_var.set(self.List_Text(list_unic_day2, list_day2, "number", 4)) 
        self.Text4_Marco4_var.set(self.List_Text(list_unic_day3, list_day3, "number", 4)) 

        self.Text5_Marco2_var.set(self.List_Text(list_unic_day1, list_day1, "number", 2)) 
        self.Text5_Marco3_var.set(self.List_Text(list_unic_day2, list_day2, "number", 2)) 
        self.Text5_Marco4_var.set(self.List_Text(list_unic_day3, list_day3, "number", 2)) 

        

    def List_Text(self, list1, list2, type_value, elem_list):
        text_day = ""
        for elem1 in list1:
            if type_value == "text":
                text_day += elem1 + "\n"
            elif type_value == "number":
                text_day += "\n"
            for elem2 in list2:
                if elem1 == elem2[1]:
                    text_day += f"      {elem2[elem_list]}\n"
        return text_day


    def Update_List_Button(self, event):
        self.Update_List(self.List1_Filter_var, self.List2_Filter_var)

    def Update_List(self, list1_var, list2_var):

        if list1_var.get() != "-" and list2_var.get() != "-":
            self.start = 1

            if LG.translate_inv(list1_var.get()) == "type_domain_1": #talent
                conexion2 = sqlite3.connect("DB SQL/genshin_db.db")
                query2 = conexion2.execute("""select v.Character, u.Build, v.n1, o.order2, sum(v.t2), sum(v.t3), sum(v.t4), (u.Mora_Ascension + u.Mora_Weapon_Ascension + u.Mora_Talent + u.XP_Character*0.2 + u.XP_Weapon*0.1) as mora, (u.XP_Character) as xp_ch from
                                            (select u.Character, b.tal_1_book_1 as n1, u.Tal1_B1_T2 as t2, u.Tal1_B1_T3 as t3, u.Tal1_B1_T4 as t4 from user as u join db_base as b on u.Character = b.id
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
                                            select u.Character, b.tal_3_book_3 as n1, u.Tal3_B3_T2 as t2, u.Tal3_B3_T3 as t3, u.Tal3_B3_T4 as t4 from user as u join db_base as b on u.Character = b.id
                                            ) as v join user as u on v.Character = u.Character join db_order as o on o.id = v.n1
											where (v.t2 + v.t3 + v.t4) != 0 
											group by v.Character, v.n1""")
                conexion2.commit()
            elif LG.translate_inv(list1_var.get()) == "type_domain_2": #mat_weapon
                conexion2 = sqlite3.connect("DB SQL/genshin_db.db")
                query2 = conexion2.execute("select u.Character, u.Build, w.mat_domain_weapon, o.order2, sum(u.Weapon_Material_Domain_Tier2) as matt2, sum(u.Weapon_Material_Domain_Tier3) as matt3, sum(u.Weapon_Material_Domain_Tier4) as matt4, sum(u.Weapon_Material_Domain_Tier5) as matt5, (u.Mora_Ascension + u.Mora_Weapon_Ascension + u.Mora_Talent + u.XP_Character*0.2 + u.XP_Weapon*0.1) as mora, (u.XP_Character) as XP_Character from user as u join db_weapon as w on u.weapon = w.id join db_order as o on o.id = w.mat_domain_weapon group by u.Character, u.Build, w.mat_domain_weapon, o.order2 HAVING (matt2 + matt3 + matt4 + matt5) != 0")
                conexion2.commit()

            self.query2_values = query2.fetchall()

            self.Summary_day()
        
        if self.start == 1:
            self.Load_Marco()
            self.Load_Images_Dynamic()

