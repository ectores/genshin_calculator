from tkinter import *
from tkinter import messagebox as MessageBox
from tkinter.ttk import Combobox
from PIL import ImageTk, Image
import os
import sqlite3
import Languages as LG
import Number_format as Nf
import Error_fix as Ef

language = LG.language_actual()

class Sheet_MyCharacter():
    def __init__(self, Multiple_Page, Summary_Menu, InvCal):
        self.Pagina_Multiple = Multiple_Page
        self.Summary_Menu = Summary_Menu
        self.Invcal = InvCal

        self.Page = Frame(Multiple_Page)

        self.dict_actual = LG.create_language(language=LG.language_actual())
        self.dict_main = LG.create_language()

        self.List_Characters_var = StringVar()

        self.List_Characters = Combobox(self.Page,values= [], textvariable=self.List_Characters_var, state="readonly", width=25, postcommand= self.Update_List)
        self.List_Characters.place(x=250, y=45)
        self.List_Characters.bind("<<ComboboxSelected>>", self.Update_Character)
        self.List_Characters.set(LG.translate(self.dict_main, self.dict_actual,"text_1"))

        self.Text_Static1 = Label(self.Page, justify="left")
        self.Text_Static1.place(x=250, y=70)

        self.Text_Static2 = Label(self.Page)
        self.Text_Static2.place(x=550, y=20, anchor=N)

        self.Text_Static3 = Label(self.Page)
        self.Text_Static3.place(x=750, y=20, anchor=N)

        varx1 = 270 + round((len(LG.translate(self.dict_main, self.dict_actual,"text_30"))+3)*5)
        varx2 = 270 + round((len(LG.translate(self.dict_main, self.dict_actual,"text_30"))+16)*5)

        self.Text_Static4 = Label(self.Page)
        self.Text_Static4.place(x=varx1, y=215, anchor=CENTER)

        self.Text_Static5 = Label(self.Page)
        self.Text_Static5.place(x=varx2, y=215, anchor=CENTER)

        if os.path.exists("Images/error/Select_" + language + ".png"):
            self.Image_Var1 = ImageTk.PhotoImage(Image.open("Images/error/Select_" + language + ".png" ).resize((208,248)))
        else:
            self.Image_Var1 = ImageTk.PhotoImage(Image.open("Images/error/Select_es.png" ).resize((208,248)))

        self.Image_Static1 = Label(self.Page, image = self.Image_Var1)
        self.Image_Static1.place(x=20, y=10)

        self.Text_Edit1 = Label(self.Page)
        self.Text_Edit1.config(relief="groove", width=116, height= 19)
        self.Text_Edit2 = Label(self.Page)
        self.Text_Edit2.config(text=LG.translate(self.dict_main, self.dict_actual,"text_17"), font= ("TkDefaultFont",15))
        
        self.Text_Edit6 = Label(self.Page)
        self.Text_Edit6.config(text=LG.translate(self.dict_main, self.dict_actual, "text_4"))
        self.Text_Edit3 = Label(self.Page)
        self.Text_Edit3.config(text=LG.translate(self.dict_main, self.dict_actual, "text_2"))
        self.Text_Edit4 = Label(self.Page)
        self.Text_Edit4.config(text=LG.translate(self.dict_main, self.dict_actual, "text_11"))
        self.Text_Edit22 = Label(self.Page)
        self.Text_Edit22.config(text=LG.translate(self.dict_main, self.dict_actual, "text_48"))
        self.Text_Edit5 = Label(self.Page)
        self.Text_Edit5.config(text=LG.translate(self.dict_main, self.dict_actual, "text_3"))
        
        self.Text_Edit7 = Label(self.Page)
        self.Text_Edit7.config(text=LG.translate(self.dict_main, self.dict_actual, "text_5"))
        self.Text_Edit8 = Label(self.Page)
        self.Text_Edit8.config(text=LG.translate(self.dict_main, self.dict_actual, "text_6"))
        self.Text_Edit9 = Label(self.Page)
        self.Text_Edit9.config(text=LG.translate(self.dict_main, self.dict_actual, "text_12"))
        self.Text_Edit10 = Label(self.Page)
        self.Text_Edit10.config(text=LG.translate(self.dict_main, self.dict_actual, "text_13"))
        self.Text_Edit23 = Label(self.Page)
        self.Text_Edit23.config(text=LG.translate(self.dict_main, self.dict_actual, "text_49"))


        self.Text_Edit11 = Label(self.Page)
        self.Text_Edit11.config(text=LG.translate(self.dict_main, self.dict_actual, "text_18"))

        self.Text_Edit12 = Label(self.Page)
        self.Text_Edit12.config(text=LG.translate(self.dict_main, self.dict_actual, "text_8"))
        self.Text_Edit13 = Label(self.Page)
        self.Text_Edit13.config(text=LG.translate(self.dict_main, self.dict_actual, "text_14"))
        self.Text_Edit14 = Label(self.Page)
        self.Text_Edit14.config(text=LG.translate(self.dict_main, self.dict_actual, "text_15"))
        self.Text_Edit15 = Label(self.Page)
        self.Text_Edit15.config(text=LG.translate(self.dict_main, self.dict_actual, "text_16"))

        self.Text_Edit16 = Label(self.Page)
        self.Text_Edit16.config(text=LG.translate(self.dict_main, self.dict_actual, "text_9"))
        self.Text_Edit17 = Label(self.Page)
        self.Text_Edit17.config(text=LG.translate(self.dict_main, self.dict_actual, "text_10"))

        self.Text_Edit18 = Label(self.Page)
        self.Text_Edit18.config(text=LG.translate(self.dict_main, self.dict_actual, "text_19"))
        self.Text_Edit19 = Label(self.Page)
        self.Text_Edit19.config(text=LG.translate(self.dict_main, self.dict_actual, "text_19"))
        self.Text_Edit20 = Label(self.Page)
        self.Text_Edit20.config(text=LG.translate(self.dict_main, self.dict_actual, "text_19"))
        self.Text_Edit21 = Label(self.Page)
        self.Text_Edit21.config(text=LG.translate(self.dict_main, self.dict_actual, "text_19"))
        

        self.Entry_lvl_var = IntVar()
        self.Entry_lvl = Entry(self.Page, textvariable= self.Entry_lvl_var, width=5)
        self.Entry_target_lvl_var = IntVar()
        self.Entry_target_lvl = Entry(self.Page,textvariable= self.Entry_target_lvl_var, width=5)
        self.List_asclvl_var = IntVar()
        self.List_asclvl = Combobox(self.Page,textvariable= self.List_asclvl_var, width=3, state="readonly", postcommand= self.Update_List_Asc)
        self.Entry_constellation_var = IntVar()
        self.Entry_constellation = Entry(self.Page,textvariable= self.Entry_constellation_var, width=5)
        self.List_target_asclvl_var = IntVar()
        self.List_target_asclvl = Combobox(self.Page,textvariable= self.List_target_asclvl_var, width=3, state="readonly", postcommand= self.Update_List_Asc)
        
        self.List_weapon_var = StringVar()
        self.List_weapon = Combobox(self.Page, textvariable= self.List_weapon_var, width=32, state="readonly", postcommand= self.Update_List_Weapon)
        self.List_build_var = StringVar()
        self.List_build = Combobox(self.Page, textvariable= self.List_build_var, width=12, state="readonly", postcommand= self.Update_List_Build)        
        self.Entry_weaponlvl_var = IntVar()
        self.Entry_weaponlvl = Entry(self.Page,textvariable= self.Entry_weaponlvl_var, width=5)
        self.Entry_target_weaponlvl_var = IntVar()
        self.Entry_target_weaponlvl = Entry(self.Page,textvariable= self.Entry_target_weaponlvl_var, width=5)
        self.List_weapon_asclvl_var = IntVar()
        self.List_weapon_asclvl = Combobox(self.Page,textvariable= self.List_weapon_asclvl_var, width=3, state="readonly", postcommand= self.Update_List_Weapon_AscLvl)
        self.List_target_weapon_asclvl_var = IntVar()
        self.List_target_weapon_asclvl = Combobox(self.Page,textvariable= self.List_target_weapon_asclvl_var, width=3, state="readonly", postcommand= self.Update_List_Weapon_AscLvl)


        self.Entry_talactbas_var = IntVar()
        self.Entry_talactbas = Entry(self.Page, textvariable= self.Entry_talactbas_var, width=5)
        self.Entry_talactele_var = IntVar()
        self.Entry_talactele = Entry(self.Page, textvariable= self.Entry_talactele_var, width=5)
        self.Entry_talactdef_var = IntVar()
        self.Entry_talactdef = Entry(self.Page, textvariable= self.Entry_talactdef_var, width=5)

        self.Entry_taltarbas_var = IntVar()
        self.Entry_taltarbas = Entry(self.Page, textvariable= self.Entry_taltarbas_var, width=5)
        self.Entry_taltarele_var = IntVar()
        self.Entry_taltarele = Entry(self.Page, textvariable= self.Entry_taltarele_var, width=5)
        self.Entry_taltardef_var = IntVar()
        self.Entry_taltardef = Entry(self.Page, textvariable= self.Entry_taltardef_var, width=5)

        self.ButtonCancelChange = Button(self.Page)
        
        self.ButtonSaveChange = Button(self.Page)

        self.list_asc = [0, 20, 40, 50, 60, 70, 80]
        self.list_asc_v2 = [0, 20, 40, 50, 60]



    def Update_List(self):

        conexion1 = sqlite3.connect("DB SQL/genshin_db.db")
        query1 = conexion1.execute("select Character from user")
        conexion1.commit()

        lista_ddbb_user_lg = []

        for fila in query1:
            lista_ddbb_user_lg.append(LG.translate(self.dict_main, self.dict_actual, fila[0]))

        lista_ddbb_user_lg.sort()
        self.List_Characters.config(values = lista_ddbb_user_lg)
        
        conexion1.close()



    def Update_List_Asc(self):
        
        self.new_listasclvl = []

        for i in self.list_asc:
            if i < int(self.Entry_lvl_var.get()):
                self.new_listasclvl = [i]
            if i == int(self.Entry_lvl_var.get()):
                self.new_listasclvl.append(i)
        self.List_asclvl.config(values= self.new_listasclvl)


        self.new_target_listasclvl = []

        for i in self.list_asc:
            if i < int(self.Entry_target_lvl_var.get()):
                self.new_target_listasclvl = [i]
            if i == int(self.Entry_target_lvl_var.get()):
                self.new_target_listasclvl.append(i)
        self.List_target_asclvl.config(values= self.new_target_listasclvl)



    def Update_List_Weapon_AscLvl(self):
        
        var_type_wp = LG.translate_inv(self.List_weapon_var.get())

        conexion9 = sqlite3.connect("DB SQL/genshin_db.db")
        query9 = conexion9.execute(f"select tier from db_weapon where id ='{var_type_wp}'")
        conexion9.commit()

        tier_weapon = query9.fetchone()[0]



        self.new_wplistasclvl = []

        if tier_weapon in [3, 4, 5]:
            for i in self.list_asc:
                if i < self.Entry_weaponlvl_var.get():
                    self.new_wplistasclvl = [i]
                if i == self.Entry_weaponlvl_var.get():
                    self.new_wplistasclvl.append(i)
        elif tier_weapon in [1, 2]:
            for j in self.list_asc_v2:
                if j < self.Entry_weaponlvl_var.get():
                    self.new_wplistasclvl = [j]
                if j == self.Entry_weaponlvl_var.get():
                    self.new_wplistasclvl.append(j)
        self.List_weapon_asclvl.config(values= self.new_wplistasclvl)


        self.new_target_wplistasclvl = []

        if tier_weapon in [3, 4, 5]:
            for i in self.list_asc:
                if i < int(self.Entry_target_weaponlvl_var.get()):
                    self.new_target_wplistasclvl = [i]
                if i == int(self.Entry_target_weaponlvl_var.get()):
                    self.new_target_wplistasclvl.append(i)
        elif tier_weapon in [1, 2]:
            for j in self.list_asc_v2:
                if j < int(self.Entry_target_weaponlvl_var.get()):
                    self.new_target_wplistasclvl = [j]
                if j == int(self.Entry_target_weaponlvl_var.get()):
                    self.new_target_wplistasclvl.append(j)
        self.List_target_weapon_asclvl.config(values= self.new_target_wplistasclvl)



    def Update_List_Weapon(self):


        var_type_ch_1 = LG.translate_inv(self.List_Characters_var.get())

        conexion2 = sqlite3.connect("DB SQL/genshin_db.db")
        query2 = conexion2.execute(f"select id from db_weapon where type=(select weapon from db_base where id='{var_type_ch_1}')")
        conexion2.commit()

        lista_ddbb_weapon = []

        for fila in query2:
            lista_ddbb_weapon.append(LG.translate(self.dict_main, self.dict_actual, fila[0]))

        lista_ddbb_weapon.sort()
        self.List_weapon.config(values= lista_ddbb_weapon)


        conexion2.close()



    def Update_List_Build(self):
        self.List_build.config(values= [LG.translate(self.dict_main, self.dict_actual, "status_1"),LG.translate(self.dict_main, self.dict_actual, "status_2")])



    def Update_Character_Edit(self): #PJ_EDICION<
        self.Entry_constellation.place(x=145, y=340)
        self.Entry_lvl.place(x=145, y=380)
        self.Entry_target_lvl.place(x=145, y=420)
        self.List_asclvl.place(x=145, y=460)
        self.List_target_asclvl.place(x=145, y=500)

        self.List_weapon.place(x=315, y=340)
        self.Entry_weaponlvl.place(x=315, y=380)
        self.Entry_target_weaponlvl.place(x=315, y=420)
        self.List_weapon_asclvl.place(x=315, y=460)
        self.List_target_weapon_asclvl.place(x=315, y=500)

        self.List_build.place(x=690, y=300)
        
        self.Entry_talactbas.place(x=650, y=380)
        self.Entry_talactele.place(x=650, y=420)
        self.Entry_talactdef.place(x=650, y=460)

        self.Entry_taltarbas.place(x=750, y=380)
        self.Entry_taltarele.place(x=750, y=420)
        self.Entry_taltardef.place(x=750, y=460)

        self.Text_Edit1.place(x=20, y=270)
        self.Text_Edit2.place(x=430, y=290, anchor=CENTER)

        self.Text_Edit6.place(x=145, y=349, anchor=E)
        self.Text_Edit3.place(x=145, y=389, anchor=E)
        self.Text_Edit4.place(x=145, y=429, anchor=E)
        self.Text_Edit22.place(x=145, y=469, anchor=E)
        self.Text_Edit5.place(x=145, y=509, anchor=E)

        self.Text_Edit7.place(x=315, y=349, anchor=E)
        self.Text_Edit8.place(x=315, y=389, anchor=E)
        self.Text_Edit9.place(x=315, y=429, anchor=E)
        self.Text_Edit10.place(x=315, y=469, anchor=E)
        self.Text_Edit23.place(x=315, y=509, anchor=E)

        self.Text_Edit11.place(x=685, y=309, anchor=E)

        self.Text_Edit12.place(x=630, y=349, anchor=E)
        self.Text_Edit13.place(x=630, y=389, anchor=E)
        self.Text_Edit14.place(x=630, y=429, anchor=E)
        self.Text_Edit15.place(x=630, y=469, anchor=E)

        self.Text_Edit16.place(x=685, y=349, anchor=E)
        self.Text_Edit17.place(x=745, y=349, anchor=W)

        self.Text_Edit18.place(x=715, y=349, anchor=CENTER)
        self.Text_Edit19.place(x=715, y=389, anchor=CENTER)
        self.Text_Edit20.place(x=715, y=429, anchor=CENTER)
        self.Text_Edit21.place(x=715, y=469, anchor=CENTER)

        self.ButtonCancelChange.config(text=LG.translate(self.dict_main, self.dict_actual, "button_1_part1") + "\n" + LG.translate(self.dict_main, self.dict_actual, "button_1_part2"), width = 8, height= 2,state=NORMAL,command=lambda: self.Import_Data_Character(False))
        self.ButtonCancelChange.place(x=420, y=520, anchor=CENTER)
        self.ButtonSaveChange.config(text=LG.translate(self.dict_main, self.dict_actual, "button_2_part1") + "\n" + LG.translate(self.dict_main, self.dict_actual, "button_2_part2"), width = 8, height= 2,state=NORMAL,command=lambda: self.Import_Data_Character(True))
        self.ButtonSaveChange.place(x=520, y=520, anchor=CENTER)



    def Set_Values_Edit_Character(self):

        character = LG.translate_inv(self.List_Characters_var.get())

        conexion3 = sqlite3.connect("DB SQL/genshin_db.db")
        query3a = conexion3.execute(f"select * from user where Character='{character}'")
        conexion3.commit()

        for fila in query3a:
            list_compacted_ch = fila

                    
        self.Entry_lvl_var.set(int(list_compacted_ch[4]))
        self.Entry_target_lvl_var.set(int(list_compacted_ch[5]))
        self.List_asclvl_var.set(int(list_compacted_ch[6]))
        self.List_target_asclvl_var.set(int(list_compacted_ch[7]))
        self.Entry_constellation_var.set(int(list_compacted_ch[1]))

        self.List_weapon_var.set(LG.translate(self.dict_main, self.dict_actual, str(list_compacted_ch[8])))
        self.Entry_weaponlvl_var.set(int(list_compacted_ch[9]))
        self.Entry_target_weaponlvl_var.set(int(list_compacted_ch[10]))
        self.List_weapon_asclvl_var.set(int(list_compacted_ch[11]))
        self.List_target_weapon_asclvl_var.set(int(list_compacted_ch[12]))

        self.List_build_var.set(LG.translate(self.dict_main, self.dict_actual, str(list_compacted_ch[2])))

        self.Entry_talactbas_var.set(int(list_compacted_ch[13]))
        self.Entry_talactele_var.set(int(list_compacted_ch[14]))
        self.Entry_talactdef_var.set(int(list_compacted_ch[15]))

        self.Entry_taltarbas_var.set(int(list_compacted_ch[16]))
        self.Entry_taltarele_var.set(int(list_compacted_ch[17]))
        self.Entry_taltardef_var.set(int(list_compacted_ch[18]))


        conexion3.close()



    def Update_Character(self, event): #Actualizar_miPJ
        self.Update_Character_Edit()
        self.Update_Character_Text()

        self.Image_Var1 = LG.fastimport_imagech(LG.translate_inv(self.List_Characters_var.get()), "character", 1)

        self.Image_Static1.config(image = self.Image_Var1)

        self.Set_Values_Edit_Character()



    def Import_Data_Character(self, state_button): #CONSULTA DE DATOS AL GUARDAR/CANCELAR CAMBIOS

        self.Update_List_Asc()
        self.Update_List_Weapon_AscLvl()

        var_type_wp = LG.translate_inv(self.List_weapon_var.get())

        conexion10 = sqlite3.connect("DB SQL/genshin_db.db")
        query10 = conexion10.execute(f"select tier from db_weapon where id ='{var_type_wp}'")
        conexion10.commit()

        tier_weapon = query10.fetchone()[0]


        if state_button:
            list_error = Ef.Fix_Errors_ch(self.Entry_lvl_var, self.Entry_target_lvl_var, self.new_listasclvl, self.List_asclvl_var, self.new_target_listasclvl, self.List_target_asclvl_var, self.Entry_constellation_var, tier_weapon, self.Entry_weaponlvl_var, self.Entry_target_weaponlvl_var, self.new_wplistasclvl, self.List_weapon_asclvl_var, self.new_target_wplistasclvl, self.List_target_weapon_asclvl_var, self.Entry_talactbas_var, self.Entry_talactele_var, self.Entry_talactdef_var, self.Entry_taltarbas_var, self.Entry_taltarele_var, self.Entry_taltardef_var)
            
            if len(list_error) == 0:
                Save_question = MessageBox.askokcancel(LG.translate(self.dict_main, self.dict_actual, "message_1"), LG.translate(self.dict_main, self.dict_actual, "message_2"))
                if Save_question:
                    conexion4_var = sqlite3.connect("DB SQL/genshin_db.db")
                    character = LG.translate_inv(self.List_Characters_var.get())
                    query4 = conexion4_var.execute(f"select * from user where Character='{character}'")
                    conexion4_var.commit()
                    query4_values = query4.fetchone()

                    if query4_values != None:
                        self.Save_Data_Character() #Guardar información de los Entry y list
                        
                        self.Calculate_Talent() #Calcular libros, items, IB y mora de talentos
                        self.Calculate_Character() #Calcular xp y mora de personaje
                        self.Calculate_Weapon() #Calcular xp y mora de arma
                        self.Update_Character_Text()
                        MessageBox.showinfo(LG.translate(self.dict_main, self.dict_actual, "message_5"), LG.translate(self.dict_main, self.dict_actual, "message_6"))

                        if self.Invcal.Page_Category != 0:
                            self.Invcal.Reload_Data()
                            self.Invcal.Show_Data()
                        self.Summary_Menu.Update_List(self.Summary_Menu.List1_Filter_var, self.Summary_Menu.List2_Filter_var)
                        self.Summary_Menu.Summary_All()
                    else:
                        MessageBox.showinfo(LG.translate(self.dict_main, self.dict_actual, "message_16"), LG.translate(self.dict_main, self.dict_actual, "message_17"))
            elif len(list_error) == 1:
                MessageBox.showerror(LG.translate(self.dict_main, self.dict_actual, "message_3"), LG.translate(self.dict_main, self.dict_actual, "message_4") + "\n" + LG.translate(self.dict_main, self.dict_actual, "error_q_1") + "\n" + Ef.error_list(self.dict_main, self.dict_actual, list_error))
            else:
                MessageBox.showerror(LG.translate(self.dict_main, self.dict_actual, "message_3"), LG.translate(self.dict_main, self.dict_actual, "message_4") + "\n" + LG.translate(self.dict_main, self.dict_actual, "error_q_2a") + str(len(list_error)) + LG.translate(self.dict_main, self.dict_actual, "error_q_2b") + "\n" + Ef.error_list(self.dict_main, self.dict_actual, list_error))
        else:
            self.Set_Values_Edit_Character()
            MessageBox.showinfo(LG.translate(self.dict_main, self.dict_actual, "message_7"), LG.translate(self.dict_main, self.dict_actual, "message_8"))



    def Update_Character_Text(self):
        conexion4 = sqlite3.connect("DB SQL/genshin_db.db")
        character = LG.translate_inv(self.List_Characters_var.get())


        #Data actual character
        query4a = conexion4.execute(f"select * from user where Character='{character}'")
        query4b = conexion4.execute(f"select Character, XP_Character, XP_Weapon, round(Mora_Ascension + Mora_Weapon_Ascension + Mora_Talent + XP_Character*0.2 + XP_Weapon*0.1) as Mora_Total from user where Character='{character}'")
        #Data build y no build
        query4c= conexion4.execute(f"select Build, sum(XP_Character) as XP_Character, sum(XP_Weapon) as XP_Weapon, sum(round(Mora_Ascension + Mora_Weapon_Ascension + Mora_Talent + XP_Character*0.2 + XP_Weapon*0.1)) as Mora_Total from user group by Build")
        conexion4.commit()

        info_character = []

        for fila in query4a:
            info_character = fila

        xp_all = 0
        xp_weapon_all = 0
        mora_all = 0

        xp_build = 0
        xp_weapon_build = 0
        mora_build = 0

        status_lvl = LG.translate(self.dict_main, self.dict_actual, "text_21")
        status_weaponlvl = LG.translate(self.dict_main, self.dict_actual, "text_21")
        status_talent = LG.translate(self.dict_main, self.dict_actual, "text_21")

        for fila in query4b:
            xp_character = fila[1]
            xp_weapon_character = fila[2]
            mora_character = fila[3]

        for fila in query4c:
            if fila[0] == "status_1":
                xp_all += fila[1]
                xp_weapon_all += fila[2]
                mora_all += fila[3]
            else:
                xp_all += fila[1]
                xp_weapon_all += fila[2]
                mora_all += fila[3]

                xp_build += fila[1]
                xp_weapon_build += fila[2]
                mora_build += fila[3]


        if info_character[4] == info_character[5] and info_character[6] == info_character[7]:
            status_lvl = LG.translate(self.dict_main, self.dict_actual, "text_20")
        if info_character[9] == info_character[10] and info_character[11] == info_character[12]:
            status_weaponlvl = LG.translate(self.dict_main, self.dict_actual, "text_20")
        if (str(info_character[13]) + "/" + str(info_character[14]) + "/" + str(info_character[15])) == (str(info_character[16]) + "/" + str(info_character[17]) + "/" + str(info_character[18])):
            status_talent = LG.translate(self.dict_main, self.dict_actual, "text_20")

        self.Text_Static1.config(text=LG.translate(self.dict_main, self.dict_actual, "text_2") + str(info_character[4]) + "  -->  " + str(info_character[5]) +  "\n   " + LG.translate(self.dict_main, self.dict_actual, "text_3") + str(info_character[6]) + "  -->  " + str(info_character[7]) + "\n" + LG.translate(self.dict_main, self.dict_actual, "text_4") + str(info_character[1]) + "\n\n" + LG.translate(self.dict_main, self.dict_actual, "text_5") + "\n-> " + LG.translate(self.dict_main, self.dict_actual, info_character[8]) + "\n" + LG.translate(self.dict_main, self.dict_actual, "text_6") + str(int(info_character[9])) + "  -->  " + str(info_character[10]) + "\n   " + LG.translate(self.dict_main, self.dict_actual, "text_7") + str(info_character[11]) + "  -->  " + str(info_character[12]) + "\n\n\n" + LG.translate(self.dict_main, self.dict_actual, "text_8") + str(int(info_character[13])) + "/" + str(int(info_character[14])) + "/" + str(int(info_character[15])) + "          " + str(int(info_character[16])) + "/" + str(int(info_character[17])) + "/" + str(int(info_character[18])), justify="left")
        
        self.Text_Static2.config(text=LG.translate(self.dict_main, self.dict_actual, "text_23") + "\n\n" + LG.translate(self.dict_main, self.dict_actual, "text_18") + LG.translate(self.dict_main, self.dict_actual, info_character[2]) + "\n\n" + LG.translate(self.dict_main, self.dict_actual, "text_24") + Nf.format_point(mora_character) + "\n" + LG.translate(self.dict_main, self.dict_actual, "text_25") + Nf.format_point(xp_character) + "\n" + LG.translate(self.dict_main, self.dict_actual, "text_26") + Nf.format_point(xp_weapon_character) + "\n\n" + LG.translate(self.dict_main, self.dict_actual, "text_27") + "\n\n" + LG.translate(self.dict_main, self.dict_actual, "text_28") +" -> " + status_lvl + "\n" + LG.translate(self.dict_main, self.dict_actual, "text_29") +" -> " + status_weaponlvl + "\n" + LG.translate(self.dict_main, self.dict_actual, "text_30") +" -> " + status_talent, width=25, height= 15, relief="groove")
        
        self.Text_Static3.config(text=LG.translate(self.dict_main, self.dict_actual, "text_31") + "\n\n" + LG.translate(self.dict_main, self.dict_actual, "text_33") + "\n\n" + LG.translate(self.dict_main, self.dict_actual, "text_24") + Nf.format_point(mora_all) + "\n" + LG.translate(self.dict_main, self.dict_actual, "text_25") + Nf.format_point(xp_all) + "\n" + LG.translate(self.dict_main, self.dict_actual, "text_26") + Nf.format_point(xp_weapon_all) + "\n\n" + LG.translate(self.dict_main, self.dict_actual, "text_32") + "\n\n" + LG.translate(self.dict_main, self.dict_actual, "text_24") + Nf.format_point(mora_build) + "\n" + LG.translate(self.dict_main, self.dict_actual, "text_25") + Nf.format_point(xp_build) + "\n" + LG.translate(self.dict_main, self.dict_actual, "text_26") + Nf.format_point(xp_weapon_build), width=25, height= 15, relief="groove")
        
        self.Text_Static4.config(text="(" + LG.translate(self.dict_main, self.dict_actual, "text_9") + ")")

        self.Text_Static5.config(text="(" + LG.translate(self.dict_main, self.dict_actual, "text_10") + ")")

        conexion4.close()



    def Save_Data_Character(self):
        
        character = LG.translate_inv(self.List_Characters_var.get())
        conexion5 = sqlite3.connect("DB SQL/genshin_db.db")
        conexion5.execute(f"""update user set
        Constellation = '{self.Entry_constellation_var.get()}',
        Build = '{LG.translate_inv(self.List_build_var.get())}',
        Lvl = '{self.Entry_lvl_var.get()}',
        Target_Lvl = '{self.Entry_target_lvl_var.get()}',
        Ascension_Lvl = '{self.List_asclvl_var.get()}',
        Target_Ascension_Lvl = '{self.List_target_asclvl_var.get()}',

        Weapon = '{LG.translate_inv(self.List_weapon_var.get())}',
        Weapon_Level = '{self.Entry_weaponlvl_var.get()}',
        Target_Weapon_Level = '{self.Entry_target_weaponlvl_var.get()}',
        Weapon_Ascension_Level = '{self.List_weapon_asclvl_var.get()}',
        Target_Weapon_Ascension_Lvl = '{self.List_target_weapon_asclvl_var.get()}',

        Talent_Actual_Basic = '{self.Entry_talactbas_var.get()}',
        Talent_Actual_Elemental = '{self.Entry_talactele_var.get()}',
        Talent_Actual_Definitive = '{self.Entry_talactdef_var.get()}',
        Talent_Target_Basic = '{self.Entry_taltarbas_var.get()}',
        Talent_Target_Elemental = '{self.Entry_taltarele_var.get()}',
        Talent_Target_Definitive = '{self.Entry_taltardef_var.get()}'
        
        where Character='{character}'""")
        conexion5.commit()

        conexion5.close()


    def Calculate_Talent(self):

        character = LG.translate_inv(self.List_Characters_var.get())
        conexion6 = sqlite3.connect("DB SQL/genshin_db.db")
        query6 = conexion6.execute(f"select Talent_Actual_Basic, Talent_Actual_Elemental, Talent_Actual_Definitive, Talent_Target_Basic, Talent_Target_Elemental, Talent_Target_Definitive from user where Character='{character}'")
        conexion6.commit()

        for fila in query6:
            list_par = [[fila[0], fila[3]],[fila[1], fila[4]],[fila[2], fila[5]]]

        list_tal = [[0,0]]

        mora = 0
        crown = 0

        for elem in list_par:
            list_tal_tar = conexion6.execute(f"SELECT * from db_character_talent where lvl = {elem[1]}")
            list_tal_act = conexion6.execute(f"SELECT * from db_character_talent where lvl = {elem[0]}")
            conexion6.commit()


            tal_b1_t2 = 0
            tal_b1_t3 = 0
            tal_b1_t4 = 0
            tal_b2_t2 = 0
            tal_b2_t3 = 0
            tal_b2_t4 = 0
            tal_b3_t2 = 0
            tal_b3_t3 = 0
            tal_b3_t4 = 0
            tal_c2_t1 = 0
            tal_c2_t2 = 0
            tal_c2_t3 = 0
            tal_matboss = 0

            for fila in list_tal_tar:
                mora += fila[1]
                crown += fila[2]

                tal_b1_t2 += fila[3]
                tal_b1_t3 += fila[4]
                tal_b1_t4 += fila[5]
                tal_b2_t2 += fila[6]
                tal_b2_t3 += fila[7]
                tal_b2_t4 += fila[8]
                tal_b3_t2 += fila[9]
                tal_b3_t3 += fila[10]
                tal_b3_t4 += fila[11]
                tal_c2_t1 += fila[12]
                tal_c2_t2 += fila[13]
                tal_c2_t3 += fila[14]
                tal_matboss += fila[15]

            for fila in list_tal_act:
                mora -= fila[1]
                crown -= fila[2]

                tal_b1_t2 -= fila[3]
                tal_b1_t3 -= fila[4]
                tal_b1_t4 -= fila[5]
                tal_b2_t2 -= fila[6]
                tal_b2_t3 -= fila[7]
                tal_b2_t4 -= fila[8]
                tal_b3_t2 -= fila[9]
                tal_b3_t3 -= fila[10]
                tal_b3_t4 -= fila[11]
                tal_c2_t1 -= fila[12]
                tal_c2_t2 -= fila[13]
                tal_c2_t3 -= fila[14]
                tal_matboss -= fila[15]

            list_tal.append([tal_b1_t2, tal_b1_t3, tal_b1_t4, tal_b2_t2, tal_b2_t3, tal_b2_t4, tal_b3_t2, tal_b3_t3, tal_b3_t4, tal_c2_t1, tal_c2_t2, tal_c2_t3, tal_matboss])

        list_tal[0]= [mora, crown]

        #Continuar
        conexion6.execute(f"""update user set

                Mora_Talent = '{list_tal[0][0]}',
                Crown = '{list_tal[0][1]}',

                Tal1_B1_T2 = '{list_tal[1][0]}',
                Tal1_B1_T3 = '{list_tal[1][1]}',
                Tal1_B1_T4 = '{list_tal[1][2]}',
                Tal1_B2_T2 = '{list_tal[1][3]}',
                Tal1_B2_T3 = '{list_tal[1][4]}',
                Tal1_B2_T4 = '{list_tal[1][5]}',
                Tal1_B3_T2 = '{list_tal[1][6]}',
                Tal1_B3_T3 = '{list_tal[1][7]}',
                Tal1_B3_T4 = '{list_tal[1][8]}',
                Tal1_Com2_T1 = '{list_tal[1][9]}',
                Tal1_Com2_T2 = '{list_tal[1][10]}',
                Tal1_Com2_T3 = '{list_tal[1][11]}',
                Tal1_MatBoss = '{list_tal[1][12]}',

                Tal2_B1_T2 = '{list_tal[2][0]}',
                Tal2_B1_T3 = '{list_tal[2][1]}',
                Tal2_B1_T4 = '{list_tal[2][2]}',
                Tal2_B2_T2 = '{list_tal[2][3]}',
                Tal2_B2_T3 = '{list_tal[2][4]}',
                Tal2_B2_T4 = '{list_tal[2][5]}',
                Tal2_B3_T2 = '{list_tal[2][6]}',
                Tal2_B3_T3 = '{list_tal[2][7]}',
                Tal2_B3_T4 = '{list_tal[2][8]}',
                Tal2_Com2_T1 = '{list_tal[2][9]}',
                Tal2_Com2_T2 = '{list_tal[2][10]}',
                Tal2_Com2_T3 = '{list_tal[2][11]}',
                Tal2_MatBoss = '{list_tal[2][12]}',

                Tal3_B1_T2 = '{list_tal[3][0]}',
                Tal3_B1_T3 = '{list_tal[3][1]}',
                Tal3_B1_T4 = '{list_tal[3][2]}',
                Tal3_B2_T2 = '{list_tal[3][3]}',
                Tal3_B2_T3 = '{list_tal[3][4]}',
                Tal3_B2_T4 = '{list_tal[3][5]}',
                Tal3_B3_T2 = '{list_tal[3][6]}',
                Tal3_B3_T3 = '{list_tal[3][7]}',
                Tal3_B3_T4 = '{list_tal[3][8]}',
                Tal3_Com2_T1 = '{list_tal[3][9]}',
                Tal3_Com2_T2 = '{list_tal[3][10]}',
                Tal3_Com2_T3 = '{list_tal[3][11]}',
                Tal3_MatBoss = '{list_tal[3][12]}'

                
                where Character='{character}'""")
        conexion6.commit()


        conexion6.close()



    def Calculate_Character(self):

        character = LG.translate_inv(self.List_Characters_var.get())
        conexion7 = sqlite3.connect("DB SQL/genshin_db.db")
        query7 = conexion7.execute(f"select lvl, Target_Lvl, Ascension_Lvl, Target_Ascension_Lvl from user where Character='{character}'")
        conexion7.commit()

        for fila in query7:
            list_lvl = [fila[0], fila[1]]
            list_asc = [fila[2], fila[3]]
        #----------- XP -----------
        detail_lvl_end = conexion7.execute(f"SELECT * from db_character_xp where lvl = {list_lvl[1]}")
        detail_lvl_ini = conexion7.execute(f"SELECT * from db_character_xp where lvl = {list_lvl[0]}")
        conexion7.commit()

        xp = 0

        for fila in detail_lvl_end:
            xp += fila[2]

        for fila in detail_lvl_ini:
            xp -= fila[2]
        #----------- ASC -----------
        detail_asc_end = conexion7.execute(f"SELECT * from db_character_asc where asc_lvl = {list_asc[1]}")
        detail_asc_ini = conexion7.execute(f"SELECT * from db_character_asc where asc_lvl = {list_asc[0]}")
        conexion7.commit()

        mora = 0
        cristal_t2 = 0
        cristal_t3 = 0
        cristal_t4 = 0
        cristal_t5 = 0
        mat_boss = 0
        mat_local = 0
        mat_com_t1 = 0
        mat_com_t2 = 0
        mat_com_t3 = 0

        for fila in detail_asc_end:
            mora += fila[1]
            cristal_t2 += fila[2]
            cristal_t3 += fila[3]
            cristal_t4 += fila[4]
            cristal_t5 += fila[5]
            mat_boss += fila[6]
            mat_local += fila[7]
            mat_com_t1 += fila[8]
            mat_com_t2 += fila[9]
            mat_com_t3 += fila[10]

        for fila in detail_asc_ini:
            mora -= fila[1]
            cristal_t2 -= fila[2]
            cristal_t3 -= fila[3]
            cristal_t4 -= fila[4]
            cristal_t5 -= fila[5]
            mat_boss -= fila[6]
            mat_local -= fila[7]
            mat_com_t1 -= fila[8]
            mat_com_t2 -= fila[9]
            mat_com_t3 -= fila[10]

        conexion7.execute(f"""update user set
                        XP_Character = '{xp}',

                        Mora_Ascension = '{mora}',
                        Ascension_Cristal_Tier2 = '{cristal_t2}',
                        Ascension_Cristal_Tier3 = '{cristal_t3}',
                        Ascension_Cristal_Tier4 = '{cristal_t4}',
                        Ascension_Cristal_Tier5 = '{cristal_t5}',
                        Ascension_Material_NormalBoss = '{mat_boss}',
                        Ascension_Material_Local = '{mat_local}',
                        Ascension_Material_Common_2_Tier1 = '{mat_com_t1}',
                        Ascension_Material_Common_2_Tier2 = '{mat_com_t2}',
                        Ascension_Material_Common_2_Tier3 = '{mat_com_t3}'
                        
                        where Character='{character}'""")
        conexion7.commit()

        conexion7.close()



    def Calculate_Weapon(self):

        character = LG.translate_inv(self.List_Characters_var.get())
        conexion8 = sqlite3.connect("DB SQL/genshin_db.db")
        query8 = conexion8.execute(f"SELECT user.Weapon_Level, user.Target_Weapon_Level, user.Weapon_Ascension_Level, user.Target_Weapon_Ascension_Lvl, db_weapon.tier from user join db_weapon on user.weapon = db_weapon.id where user.Character='{character}'")
        conexion8.commit()

        for fila in query8:
            list_lvl = [fila[0], fila[1]]
            list_asc = [fila[2], fila[3]]
            tier = fila[4]
        #----------- XP -----------
        detail_lvl_end = conexion8.execute(f"select * from db_weaponxp where Lvl = '{list_lvl[1]}' and Tier = '{tier}'")
        detail_lvl_ini = conexion8.execute(f"select * from db_weaponxp where Lvl = '{list_lvl[0]}' and Tier = '{tier}'")
        conexion8.commit()

        xp = 0

        for fila in detail_lvl_end:
            xp += fila[3]

        for fila in detail_lvl_ini:
            xp -= fila[3]
        #----------- ASC -----------
        detail_asc_end = conexion8.execute(f"SELECT * from db_weaponasc where Lvl = '{list_asc[1]}' and Tier = '{tier}'")
        detail_asc_ini = conexion8.execute(f"SELECT * from db_weaponasc where Lvl = '{list_asc[0]}' and Tier = '{tier}'")
        conexion8.commit()
        mora = 0
        mat_asc_t2 = 0
        mat_asc_t3 = 0
        mat_asc_t4 = 0
        mat_asc_t5 = 0
        mat_com1_t2 = 0
        mat_com1_t3 = 0
        mat_com1_t4 = 0
        mat_com2_t1 = 0
        mat_com2_t2 = 0
        mat_com2_t3 = 0

        for fila in detail_asc_end:
            mora += fila[2]
            mat_asc_t2 += fila[3]
            mat_asc_t3 += fila[4]
            mat_asc_t4 += fila[5]
            mat_asc_t5 += fila[6]
            mat_com1_t2 += fila[7]
            mat_com1_t3 += fila[8]
            mat_com1_t4 += fila[9]
            mat_com2_t1 += fila[10]
            mat_com2_t2 += fila[11]
            mat_com2_t3 += fila[12]

        for fila in detail_asc_ini:
            mora -= fila[2]
            mat_asc_t2 -= fila[3]
            mat_asc_t3 -= fila[4]
            mat_asc_t4 -= fila[5]
            mat_asc_t5 -= fila[6]
            mat_com1_t2 -= fila[7]
            mat_com1_t3 -= fila[8]
            mat_com1_t4 -= fila[9]
            mat_com2_t1 -= fila[10]
            mat_com2_t2 -= fila[11]
            mat_com2_t3 -= fila[12]

        conexion8.execute(f"""update user set
                        XP_Weapon = '{xp}',

                        Mora_Weapon_Ascension = '{mora}',
                        Weapon_Material_Domain_Tier2 = '{mat_asc_t2}',
                        Weapon_Material_Domain_Tier3 = '{mat_asc_t3}',
                        Weapon_Material_Domain_Tier4 = '{mat_asc_t4}',
                        Weapon_Material_Domain_Tier5 = '{mat_asc_t5}',
                        Weapon_Material_Common_1_Tier2 = '{mat_com1_t2}',
                        Weapon_Material_Common_1_Tier3 = '{mat_com1_t3}',
                        Weapon_Material_Common_1_Tier4 = '{mat_com1_t4}',
                        Weapon_Material_Common_2_Tier1 = '{mat_com2_t1}',
                        Weapon_Material_Common_2_Tier2 = '{mat_com2_t2}',
                        Weapon_Material_Common_2_Tier3 = '{mat_com2_t3}'

                        where Character='{character}'""")
        conexion8.commit()
        conexion8.close()
