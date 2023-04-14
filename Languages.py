#The languages will work like modules, every language will need being imported
#and the program will interprete every language following a specific format

#Format: Word_Code - Word_Language_xx

#For example, for the characters

#Ch_1 Amber

#Forma de llamar la funcion
# import Languages as LG

# LG.import_namelg("ch_15", "es")
import os
import pandas as pd
from PIL import ImageTk, Image

# def import_namelg(id, file, language):
#     var_lg = 0
#     namelg = ""

#     if os.path.exists("Languages/" + file + "_" + language +".csv"):
#         Arch_lg = pd.read_csv("Languages/" + file + "_" + language +".csv", delimiter=";", encoding='utf-8')
#         list_lg = [list(row) for row in Arch_lg.values]
#         for i in list_lg:
#             if i[0] == id:
#                 namelg = i[1]
#                 var_lg = 1
        
#     if var_lg == 0:
#         Arch_lg_es = pd.read_csv("Languages/" + file + "_es.csv", delimiter=";", encoding='utf-8')
#         list_lg_es = [list(row) for row in Arch_lg_es.values]
#         for j in list_lg_es:
#             if j[0] == id:
#                 namelg = j[1]
#                 var_lg = 1
    
#     if var_lg == 0 and os.path.exists("Languages/" + file + "_en.csv"):
#         Arch_lg_en = pd.read_csv("Languages/" + file + "_en.csv", delimiter=";", encoding='utf-8')
#         list_lg_en = [list(row) for row in Arch_lg_en.values]
#         for k in list_lg_en:
#             if k[0] == id:
#                 namelg = k[1]
#                 var_lg = 1
#     #REORDENAR
#     if var_lg == 0:
#         namelg = id
#     if pd.isna(namelg):
#         namelg = ""
    
#     return namelg

# def import_idlg(name, file, language):
#     var_lg = 0
#     idlg = ""

#     if os.path.exists("Languages/" + file + "_" + language +".csv"):
#         Arch_lg = pd.read_csv("Languages/" + file + "_" + language +".csv", delimiter=";", encoding='utf-8')
#         list_lg = [list(row) for row in Arch_lg.values]
#         for i in list_lg:
#             if i[1] == name:
#                 idlg = i[0]
#                 var_lg = 1
    
#     if var_lg == 0:
#         Arch_lg_es = pd.read_csv("Languages/" + file + "_es.csv", delimiter=";", encoding='utf-8')
#         list_lg_es = [list(row) for row in Arch_lg_es.values]
#         for j in list_lg_es:
#             if j[1] == name:
#                 idlg = j[0]
#                 var_lg = 1

#     if var_lg == 0 and os.path.exists("Languages/" + file + "_en.csv"):
#         Arch_lg_en = pd.read_csv("Languages/" + file + "_en.csv", delimiter=";", encoding='utf-8')
#         list_lg_en = [list(row) for row in Arch_lg_en.values]
#         for k in list_lg_en:
#             if k[1] == name:
#                 idlg = k[0]
#                 var_lg = 1
#     #REORDENAR
#     if var_lg == 0:
#         idlg = name

#     return idlg
    
def import_imagech(name, language, name_folder, type_image):
    if type_image == 1:
        var_x = 208
        var_y = 248
    elif type_image == 2:
        var_x = 64
        var_y = 64
    elif type_image == 3:
        var_x = 32
        var_y = 32
    elif type_image == 4:
        var_x = 40
        var_y = 40


    if os.path.exists("Images/" + name_folder + "/" + name + ".png"):
        var_image = ImageTk.PhotoImage(Image.open("Images/" + name_folder + "/" + name + ".png").resize((var_x,var_y)))
    elif os.path.exists("Images/error/No_Image_" + language + ".png"):
        var_image = ImageTk.PhotoImage(Image.open("Images/error/No_Image_" + language + ".png").resize((var_x,var_y)))
    elif os.path.exists("Images/error/No_Image_en.png"):
        var_image = ImageTk.PhotoImage(Image.open("Images/error/No_Image_en.png").resize((var_x,var_y)))
    else:
        var_image = ImageTk.PhotoImage(Image.open("Images/error/No_Image_es.png").resize((var_x,var_y)))
    return var_image

def import_imageer():
    language = language_actual()
    
    return import_imagech("ch_0", language, "character", 1)

def language_actual():
    Arch_config = pd.read_json("config.json")
    actual_language = Arch_config["Information"]["language"]
    return actual_language



def button_text(language_base, language_user, *id_text):
    var_number = 0
    for elem in id_text:
        if var_number == 0:
            text = translate(language_base, language_user, elem)
            var_number += 1
        else:
            if translate(language_base, language_user, elem) is not None:
                text += "\n" + translate(language_base, language_user, elem)
    return text

def translate(language_base, language_user, word):
    try:
        if language_user[word] == language_user[word]:
            return language_user[word]
        else:
            if language_base[word] == language_base[word]:
                return language_base[word]
            else:
                word
    except:
        try:
            if language_base[word] == language_base[word]:
                return language_base[word]
            else:
                word
        except:
            return word


# def fastimport_namelg(var, archive):
#     language = language_actual()
#     return import_namelg(var,archive, language)


# def fastimport_idlg(var, archive):
#     language = language_actual()
#     return import_idlg(var,archive, language)

def fastimport_imagech(var, name_folder, type_image):
    language = language_actual()
    return import_imagech(var, language, name_folder, type_image)



def create_language(language = "es", number = 1):
    path_var = "Languages/lg_" + language +".csv"

    if number == 2:
        path_var = "Languages/lg.csv"

    if os.path.exists(path_var):
        Arch_lg = pd.read_csv(path_var, delimiter=";", encoding='utf-8')
        idioma = {}
        for id,val in Arch_lg.values:
            idioma[id] = val
        return idioma



def translate_inv(word, number = 1):
    language=language_actual()
    var_lg = 0
    idlg = ""
    dir_var = "lg_help"
    if number == 2:
        dir_var = "lg"

    if number == 1:
        if os.path.exists("Languages/lg_help_" + language +".csv"):
            Arch_lg = pd.read_csv("Languages/lg_help_" + language +".csv", delimiter=";", encoding='utf-8')
            list_lg = [list(row) for row in Arch_lg.values]
            for i in list_lg:
                if i[1] == word:
                    idlg = i[0]
                    var_lg = 1
        
        if var_lg == 0 and os.path.exists("Languages/lg_help_en.csv"):
            Arch_lg_en = pd.read_csv("Languages/lg_help_en.csv", delimiter=";", encoding='utf-8')
            list_lg_en = [list(row) for row in Arch_lg_en.values]
            for k in list_lg_en:
                if k[1] == word:
                    idlg = k[0]
                    var_lg = 1

        if var_lg == 0:
            Arch_lg_es = pd.read_csv("Languages/lg_help_es.csv", delimiter=";", encoding='utf-8')
            list_lg_es = [list(row) for row in Arch_lg_es.values]
            for j in list_lg_es:
                if j[1] == word:
                    idlg = j[0]
                    var_lg = 1
    elif number == 2:
        if os.path.exists("Languages/lg.csv"):
            Arch_lg = pd.read_csv("Languages/lg.csv", delimiter=";", encoding='utf-8')
            list_lg = [list(row) for row in Arch_lg.values]
            for i in list_lg:
                if i[1] == word:
                    idlg = i[0]
                    var_lg = 1

    #REORDENAR
    if var_lg == 0:
        idlg = word

    return idlg