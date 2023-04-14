from tkinter import *
from tkinter import messagebox as MessageBox
import sqlite3
import Languages as LG


class Sheet_CharactersList():
    def __init__(self, Multiple_Page, My_Character, Summary_Menu, InvCal):
        self.Pagina_Multiple = Multiple_Page
        self.My_Character = My_Character
        self.Summary_Menu = Summary_Menu
        self.Invcal = InvCal

        self.Page = Frame(Multiple_Page)

        self.dict_actual = LG.create_language(language=LG.language_actual())
        self.dict_main = LG.create_language()
        
        self.Page_Characters = 1
        self.list_all = []
        self.list_test = []

        #Se crea conexion a la BBDD
        conexion1 = sqlite3.connect("DB SQL/genshin_db.db")
        # query1=conexion1.execute("select id, element, weapon, tal_1, tal_2, tal_3 from db_base")
        query1=conexion1.execute("select id, element, weapon, tal_1_book_1, tal_1_book_2, tal_1_book_3, tal_2_book_1, tal_2_book_2, tal_2_book_3, tal_3_book_1, tal_3_book_2, tal_3_book_3 from db_base")
        conexion1.commit()

        #Obtengo la lista de personajes con atributos e id




        for fila in query1:
            test_list = [fila[3], fila[4], fila[5], fila[6], fila[7], fila[8], fila[9], fila[10], fila[11]]
            test_len = len(set(test_list))

            if test_len == 1:
                self.list_all.append([fila[0], LG.translate(self.dict_main, self.dict_actual, fila[0]), LG.translate(self.dict_main, self.dict_actual, fila[1]), LG.translate(self.dict_main, self.dict_actual,fila[2]), LG.translate(self.dict_main, self.dict_actual,fila[3]), ""])

            elif test_len == 3:
                self.list_all.append([fila[0], LG.translate(self.dict_main, self.dict_actual,fila[0]), LG.translate(self.dict_main, self.dict_actual, fila[1]), LG.translate(self.dict_main, self.dict_actual,fila[2]), LG.translate(self.dict_main, self.dict_actual,fila[3]), LG.translate(self.dict_main, self.dict_actual,fila[4]) + ", " + LG.translate(self.dict_main, self.dict_actual,fila[5])])

            else:
                self.list_all.append([fila[0], LG.translate(self.dict_main, self.dict_actual,fila[0]), LG.translate(self.dict_main, self.dict_actual,fila[1]), LG.translate(self.dict_main, self.dict_actual,fila[2]), LG.translate(self.dict_main, self.dict_actual,fila[3]), LG.translate(self.dict_main, self.dict_actual,fila[4]) + ", " + LG.translate(self.dict_main, self.dict_actual,"text_50")])

                
            self.list_test.append([fila[0], fila[1], fila[2], fila[3], fila[4], fila[5]])


        self.list_all.sort(key=lambda x: x[1])

        #Creo objetos de la GUI
        self.Text_Description = Label(self.Page, relief="groove", text=LG.translate(self.dict_main, self.dict_actual,"text_35") + "\n" + LG.translate(self.dict_main, self.dict_actual,"text_36"), width=70, height= 3)
        self.Text_Description.place(x=430, y=40, anchor=CENTER)

        self.Text_Name_Character_1 = Label(self.Page)
        self.Text_Name_Character_1.place(x=115, y=100, anchor=CENTER)
        self.Text_Name_Character_2 = Label(self.Page)
        self.Text_Name_Character_2.place(x=325, y=100, anchor=CENTER)
        self.Text_Name_Character_3 = Label(self.Page)
        self.Text_Name_Character_3.place(x=535, y=100, anchor=CENTER)
        self.Text_Name_Character_4 = Label(self.Page)
        self.Text_Name_Character_4.place(x=745, y=100, anchor=CENTER)

        self.Text_Description_1 = Label(self.Page, relief="groove", width=20, height= 4)
        self.Text_Description_1.place(x=115, y=415, anchor=CENTER)
        self.Text_Description_2 = Label(self.Page, relief="groove", width=20, height= 4)
        self.Text_Description_2.place(x=325, y=415, anchor=CENTER)
        self.Text_Description_3 = Label(self.Page, relief="groove", width=20, height= 4)
        self.Text_Description_3.place(x=535, y=415, anchor=CENTER)
        self.Text_Description_4 = Label(self.Page, relief="groove", width=20, height= 4)
        self.Text_Description_4.place(x=745, y=415, anchor=CENTER)

        self.Check_1_var = IntVar()
        self.Check_1 = Checkbutton(self.Page, variable=self.Check_1_var, command=lambda: self.Update_Check(1))
        self.Check_1.place(x=40, y=455)
        self.Check_2_var = IntVar()
        self.Check_2 = Checkbutton(self.Page, variable=self.Check_2_var, command=lambda: self.Update_Check(2))
        self.Check_2.place(x=250, y=455)
        self.Check_3_var = IntVar()
        self.Check_3 = Checkbutton(self.Page, variable=self.Check_3_var, command=lambda: self.Update_Check(3))
        self.Check_3.place(x=460, y=455)
        self.Check_4_var = IntVar()
        self.Check_4 = Checkbutton(self.Page, variable=self.Check_4_var, command=lambda: self.Update_Check(4))
        self.Check_4.place(x=670, y=455)

        self.Text_Number_Page = Label(self.Page)
        self.Text_Number_Page.place(x=430, y=530, anchor=CENTER)


        self.Button_Previous = Button(self.Page, command=lambda: self.Change_Page(-1))
        self.Button_Previous.place(x=325, y=530, anchor=CENTER)
        self.Button_Next = Button(self.Page, command=lambda: self.Change_Page(1))
        self.Button_Next.place(x=535, y=530, anchor=CENTER)

        self.Image_Character_1 = Label(self.Page)
        self.Image_Character_1.place(x=115, y=115, anchor=N)
        self.Image_Character_2 = Label(self.Page)
        self.Image_Character_2.place(x=325, y=115, anchor=N)
        self.Image_Character_3 = Label(self.Page)
        self.Image_Character_3.place(x=535, y=115, anchor=N)
        self.Image_Character_4 = Label(self.Page)
        self.Image_Character_4.place(x=745, y=115, anchor=N)
        
        self.Change_Page(0)

        conexion1.close()


    def Update_Check(self, check_var):

        conexion2 = sqlite3.connect("DB SQL/genshin_db.db")
        id_ch = self.list_all[self.Page_Characters*4-(-check_var + 5)][0]
        weapon = self.Give_Weapon(id_ch)

        add = 0
        if check_var == 1:
            if int(self.Check_1_var.get()) == 1:
                add = 1
        elif check_var == 2:
            if int(self.Check_2_var.get()) == 1:
                add = 1
        elif check_var == 3:
            if int(self.Check_3_var.get()) == 1:
                add = 1
        elif check_var == 4:
            if int(self.Check_4_var.get()) == 1:
                add = 1

        Save_question = False

        if add == 0:
            Save_question = MessageBox.askokcancel(LG.translate(self.dict_main, self.dict_actual,"message_9"), LG.translate(self.dict_main, self.dict_actual,"message_10") + "\n" + LG.translate(self.dict_main, self.dict_actual,"message_11") + LG.translate(self.dict_main, self.dict_actual,"menu_2"))
        else:
            var = 'notrv'
            if self.Check_Traveler(self.list_all[self.Page_Characters*4-(-check_var + 5)][0]):
                var = 'trv'
            conexion2.execute(f"insert into user (Character) values ('{id_ch}')")
            conexion2.execute(f"update user set Weapon='{weapon}' where Character='{id_ch}'")
            conexion2.commit()

        if Save_question:
            
            conexion2.execute(f"delete from user where Character='{id_ch}'")
            conexion2.commit()
            #---------------------------------
            if add == 0:
                MessageBox.showinfo(LG.translate(self.dict_main, self.dict_actual,"message_12"), LG.translate(self.dict_main, self.dict_actual,"message_13"))
          
        else:
            if add == 1:
                if check_var == 1:
                    self.Check_1.select()
                elif check_var == 2:
                    self.Check_2.select()
                elif check_var == 3:
                    self.Check_3.select()
                elif check_var == 4:
                    self.Check_4.select()
            else:
                if check_var == 1:
                    self.Check_1.deselect()
                elif check_var == 2:
                    self.Check_2.deselect()
                elif check_var == 3:
                    self.Check_3.deselect()
                elif check_var == 4:
                    self.Check_4.deselect()
        conexion2.close()
        self.Update_Text_and_Image()
        if self.Invcal.Page_Category != 0:
           self.Invcal.Reload_Data()
           self.Invcal.Show_Data()
        self.Summary_Menu.Update_List(self.Summary_Menu.List1_Filter_var, self.Summary_Menu.List2_Filter_var)
        self.Summary_Menu.Summary_All()

           


#CONTINUAR

    def Check_Traveler(self, id):

        conexion3 = sqlite3.connect("DB SQL/genshin_db.db")
        query3 = conexion3.execute(f"select traveller from db_base where id='{id}'")
        conexion3.commit()

        istrv = False

        for fila in query3:
            if fila[0] == 1:
                istrv = True
        
        conexion3.close()

        return istrv


    def Give_Weapon(self, id):

        conexion4 = sqlite3.connect("DB SQL/genshin_db.db")
        query4 = conexion4.execute(f"select weapon from db_base where id='{id}'")
        conexion4.commit()

        for fila in query4:
            type_weapon = fila[0]
            
        if type_weapon == "weapon_type_1":
            name_weapon = "weapon_name_16"
        elif type_weapon == "weapon_type_2":
            name_weapon = "weapon_name_7"
        elif type_weapon == "weapon_type_3":
            name_weapon = "weapon_name_84"
        elif type_weapon == "weapon_type_4":
            name_weapon = "weapon_name_96"
        else:
            name_weapon = "weapon_name_71"
        
        conexion4.close()
        
        return name_weapon
    

    def Character_Account(self, id):
        
        conexion5 = sqlite3.connect("DB SQL/genshin_db.db")
        query5 = conexion5.execute(f"select Character from user")
        conexion5.commit()

        havech = False

        for fila in query5:
            if fila[0] == id:
                havech = True
                break
        
        conexion5.close()

        return havech
    
    # def Talents_Name(self, talent1, talent2, talent3):
    #     if talent1 == talent2 and talent2 == talent3:
    #         talent = talent1
    #     else:
    #         talent = f"{talent1}\n, {talent2}, {talent3}"
    #     return talent
    

    def Update_Text_and_Image(self):

        if self.Page_Characters*4-3 <= len(self.list_all):
            self.Text_Name_Character_1.config(text=self.list_all[self.Page_Characters*4-4][1])
            self.Image_Character_1_var = LG.fastimport_imagech(self.list_all[self.Page_Characters*4-4][0], "character", 1)
            if self.list_all[self.Page_Characters*4-4][5] != "":
                self.Text_Description_1.config(text= LG.translate(self.dict_main, self.dict_actual,"text_37") + self.list_all[self.Page_Characters*4-4][2] + "\n" + LG.translate(self.dict_main, self.dict_actual,"text_38") + self.list_all[self.Page_Characters*4-4][3] + "\n" + LG.translate(self.dict_main, self.dict_actual,"text_39") + self.list_all[self.Page_Characters*4-4][4] + "\n" + self.list_all[self.Page_Characters*4-4][5])
            else:
                self.Text_Description_1.config(text= LG.translate(self.dict_main, self.dict_actual,"text_37") + self.list_all[self.Page_Characters*4-4][2] + "\n" + LG.translate(self.dict_main, self.dict_actual,"text_38") + self.list_all[self.Page_Characters*4-4][3] + "\n" + LG.translate(self.dict_main, self.dict_actual,"text_39") + self.list_all[self.Page_Characters*4-4][4])
            if self.Character_Account(self.list_all[self.Page_Characters*4-4][0]):
                self.Check_1.select()
                self.Check_1.config(state=NORMAL, text=LG.translate(self.dict_main, self.dict_actual,"text_41"))
            else:
                self.Check_1.deselect()
                self.Check_1.config(state=NORMAL, text=LG.translate(self.dict_main, self.dict_actual,"text_40"))
        else:
            self.Text_Name_Character_1.config(text=LG.translate(self.dict_main, self.dict_actual,"text_34"))
            self.Image_Character_1_var = LG.import_imageer()
            self.Text_Description_1.config(text="-")
            self.Check_1.deselect()
            self.Check_1.config(text="-", state=DISABLED)
        if self.Page_Characters*4-2 <= len(self.list_all):
            self.Text_Name_Character_2.config(text=self.list_all[self.Page_Characters*4-3][1])
            self.Image_Character_2_var = LG.fastimport_imagech(self.list_all[self.Page_Characters*4-3][0], "character", 1)
            if self.list_all[self.Page_Characters*4-3][5] != "":
                self.Text_Description_2.config(text= LG.translate(self.dict_main, self.dict_actual,"text_37") + self.list_all[self.Page_Characters*4-3][2] + "\n" + LG.translate(self.dict_main, self.dict_actual,"text_38") + self.list_all[self.Page_Characters*4-3][3] + "\n" + LG.translate(self.dict_main, self.dict_actual,"text_39") + self.list_all[self.Page_Characters*4-3][4] + "\n" + self.list_all[self.Page_Characters*4-3][5])
            else:
                self.Text_Description_2.config(text= LG.translate(self.dict_main, self.dict_actual,"text_37") + self.list_all[self.Page_Characters*4-3][2] + "\n" + LG.translate(self.dict_main, self.dict_actual,"text_38") + self.list_all[self.Page_Characters*4-3][3] + "\n" + LG.translate(self.dict_main, self.dict_actual,"text_39") + self.list_all[self.Page_Characters*4-3][4])
            if self.Character_Account(self.list_all[self.Page_Characters*4-3][0]):
                self.Check_2.select()
                self.Check_2.config(state=NORMAL, text=LG.translate(self.dict_main, self.dict_actual,"text_41"))
            else:
                self.Check_2.deselect()
                self.Check_2.config(state=NORMAL, text=LG.translate(self.dict_main, self.dict_actual,"text_40"))
        else:
            self.Text_Name_Character_2.config(text=LG.translate(self.dict_main, self.dict_actual,"text_34"))
            self.Image_Character_2_var = LG.import_imageer()
            self.Text_Description_2.config(text="-")
            self.Check_2.deselect()
            self.Check_2.config(text="-", state=DISABLED)
        if self.Page_Characters*4-1 <= len(self.list_all):
            self.Text_Name_Character_3.config(text=self.list_all[self.Page_Characters*4-2][1])
            self.Image_Character_3_var = LG.fastimport_imagech(self.list_all[self.Page_Characters*4-2][0], "character", 1)
            if self.list_all[self.Page_Characters*4-2][5] != "":
                self.Text_Description_3.config(text= LG.translate(self.dict_main, self.dict_actual,"text_37") + self.list_all[self.Page_Characters*4-2][2] + "\n" + LG.translate(self.dict_main, self.dict_actual,"text_38") + self.list_all[self.Page_Characters*4-2][3] + "\n" + LG.translate(self.dict_main, self.dict_actual,"text_39") + self.list_all[self.Page_Characters*4-2][4] + "\n" + self.list_all[self.Page_Characters*4-2][5])
            else:
                self.Text_Description_3.config(text= LG.translate(self.dict_main, self.dict_actual,"text_37") + self.list_all[self.Page_Characters*4-2][2] + "\n" + LG.translate(self.dict_main, self.dict_actual,"text_38") + self.list_all[self.Page_Characters*4-2][3] + "\n" + LG.translate(self.dict_main, self.dict_actual,"text_39") + self.list_all[self.Page_Characters*4-2][4])
            if self.Character_Account(self.list_all[self.Page_Characters*4-2][0]):
                self.Check_3.select()
                self.Check_3.config(state=NORMAL, text=LG.translate(self.dict_main, self.dict_actual,"text_41"))
            else:
                self.Check_3.deselect()
                self.Check_3.config(state=NORMAL, text=LG.translate(self.dict_main, self.dict_actual,"text_40"))
        else:
            self.Text_Name_Character_3.config(text=LG.translate(self.dict_main, self.dict_actual,"text_34"))
            self.Image_Character_3_var = LG.import_imageer()
            self.Text_Description_3.config(text="-")
            self.Check_3.deselect()
            self.Check_3.config(text="-", state=DISABLED)
        if self.Page_Characters*4-0 <= len(self.list_all):
            self.Text_Name_Character_4.config(text=self.list_all[self.Page_Characters*4-1][1])
            self.Image_Character_4_var = LG.fastimport_imagech(self.list_all[self.Page_Characters*4-1][0], "character", 1)
            if self.list_all[self.Page_Characters*4-1][5] != "":
                self.Text_Description_4.config(text= LG.translate(self.dict_main, self.dict_actual,"text_37") + self.list_all[self.Page_Characters*4-1][2] + "\n" + LG.translate(self.dict_main, self.dict_actual,"text_38") + self.list_all[self.Page_Characters*4-1][3] + "\n" + LG.translate(self.dict_main, self.dict_actual,"text_39") + self.list_all[self.Page_Characters*4-1][4] + "\n" + self.list_all[self.Page_Characters*4-1][5])
            else:
                self.Text_Description_4.config(text= LG.translate(self.dict_main, self.dict_actual,"text_37") + self.list_all[self.Page_Characters*4-1][2] + "\n" + LG.translate(self.dict_main, self.dict_actual,"text_38") + self.list_all[self.Page_Characters*4-1][3] + "\n" + LG.translate(self.dict_main, self.dict_actual,"text_39") + self.list_all[self.Page_Characters*4-1][4])
            if self.Character_Account(self.list_all[self.Page_Characters*4-1][0]):
                self.Check_4.select()
                self.Check_4.config(state=NORMAL, text=LG.translate(self.dict_main, self.dict_actual,"text_41"))
            else:
                self.Check_4.deselect()
                self.Check_4.config(state=NORMAL, text=LG.translate(self.dict_main, self.dict_actual,"text_40"))
        else:
            self.Text_Name_Character_4.config(text=LG.translate(self.dict_main, self.dict_actual,"text_34"))
            self.Image_Character_4_var = LG.import_imageer()
            self.Text_Description_4.config(text="-")
            self.Check_4.deselect()
            self.Check_4.config(text="-", state=DISABLED)

    
        self.Image_Character_1.config(image= self.Image_Character_1_var)
        self.Image_Character_2.config(image= self.Image_Character_2_var)
        self.Image_Character_3.config(image= self.Image_Character_3_var)
        self.Image_Character_4.config(image= self.Image_Character_4_var)

        self.Text_Number_Page.config(text=LG.translate(self.dict_main, self.dict_actual,"button_3") + str(self.Page_Characters))

        self.Button_Previous.config(text=LG.translate(self.dict_main, self.dict_actual,"button_3a"))
        self.Button_Next.config(text=LG.translate(self.dict_main, self.dict_actual,"button_3b"))

        if len(self.list_all) % 4 == 0:
            self.Max_Page = len(self.list_all) // 4
        else:
            self.Max_Page = (len(self.list_all) // 4) + 1

        if self.Page_Characters == 1:
            self.Button_Previous.config(state=DISABLED)
        elif self.Page_Characters == (self.Max_Page):
            self.Button_Next.config(state=DISABLED)
        else:
            self.Button_Previous.config(state=NORMAL)
            self.Button_Next.config(state=NORMAL)

    def Change_Page(self, change):
        self.Page_Characters += change

        self.Update_Text_and_Image()      