#This module help to fix possibles errors in the inputs from the user
#With this, there are not negative values (mora, exp), and just will be
#available real options, for example, character_target_lvl < character_lvl
#is not possible.
import Languages as LG
from tkinter import * 


def Fix_Errors_ch(lvl, lvl_tar, list_asc, asc, list_tar_asc, tar_asc, const, tier, wp_lvl, wp_lvl_tar, list_wp_asc, wp_asc, list_tar_wp_asc, tar_wp_asc, act_bas, act_ele, act_def, tar_bas, tar_ele, tar_def):
    Message_Error = ""
    error = 0
    list_error = set()
#lvl, lvl_tar, asc, tar_asc, const, wp_lvl, wp_lvl_tar, wp_asc, tar_wp_asc, act_bas, act_ele, act_def, tar_bas, tar_ele, tar_def
    try:
        lvl.get()
    except:
        list_error.add("error_08")


    try:    
        lvl_tar.get()
    except:
        list_error.add("error_09")


    try:    
        const.get()
    except:
        list_error.add("error_18")


    try:
        wp_lvl.get()
    except:
        list_error.add("error_10")


    try:
        wp_lvl_tar.get()
    except:
        list_error.add("error_11")


    try:
        act_bas.get()
    except:
        list_error.add("error_12")


    try:
        act_ele.get()
    except:
        list_error.add("error_13")


    try:
        act_def.get()
    except:
        list_error.add("error_14")


    try:
        tar_bas.get()
    except:
        list_error.add("error_15")


    try:
        tar_ele.get()
    except:
        list_error.add("error_16")


    try:
        tar_def.get()
    except:
        list_error.add("error_17")



#----------------

    if "error_08" not in list_error:
        if "error_09" not in list_error:
            if check_lvl(lvl.get()):
                if check_lvl(lvl_tar.get()):
                    if int(lvl.get()) > int(lvl_tar.get()):
                        list_error.add("error_01")
                else:
                        list_error.add("error_20")
            elif check_lvl(lvl_tar.get()):
                list_error.add("error_19")
            else:
                list_error.add("error_19")
                list_error.add("error_20")
    
    if "error_10" not in list_error:
        if "error_11" not in list_error:
            if check_lvl(wp_lvl.get()):
                if check_lvl(wp_lvl_tar.get()):
                    if int(wp_lvl.get()) > int(wp_lvl_tar.get()):
                        list_error.add("error_02")
                else:
                        list_error.add("error_22")
            elif check_lvl(lvl_tar.get()):
                list_error.add("error_21")
            else:
                list_error.add("error_21")
                list_error.add("error_22")
    
    if "error_12" not in list_error:
        if "error_15" not in list_error:
            if check_talent(act_bas.get()):
                if check_talent(tar_bas.get()):
                    if int(act_bas.get()) > int(tar_bas.get()):
                        list_error.add("error_03")
                else:
                        list_error.add("error_26")
            elif check_talent(lvl_tar.get()):
                list_error.add("error_23")
            else:
                list_error.add("error_23")
                list_error.add("error_26")

    if "error_13" not in list_error:
        if "error_16" not in list_error:
            if check_talent(act_ele.get()):
                if check_talent(tar_ele.get()):
                    if int(act_ele.get()) > int(tar_ele.get()):
                        list_error.add("error_04")
                else:
                        list_error.add("error_27")
            elif check_talent(lvl_tar.get()):
                list_error.add("error_24")
            else:
                list_error.add("error_24")
                list_error.add("error_27")
    
    if "error_14" not in list_error:
        if "error_17" not in list_error:
            if check_talent(act_def.get()):
                if check_talent(tar_def.get()):
                    if int(act_def.get()) > int(tar_def.get()):
                        list_error.add("error_05")
                else:
                        list_error.add("error_28")
            elif check_talent(lvl_tar.get()):
                list_error.add("error_25")
            else:
                list_error.add("error_25")
                list_error.add("error_28")

    if "error_08" not in list_error:
        if check_lvl(lvl.get()):
            if int(asc.get()) > int(lvl.get()):
                list_error.add("error_06")
            if int(asc.get()) not in list_asc:
                list_error.add("error_30")
        else:
            list_error.add("error_19")
    
    if "error_09" not in list_error:
        if check_lvl(lvl_tar.get()):
            if int(tar_asc.get()) > int(lvl_tar.get()):
                list_error.add("error_31")
            if int(tar_asc.get()) not in list_tar_asc:
                list_error.add("error_32")
        else:
            list_error.add("error_20")


    
    if "error_10" not in list_error:
        if check_lvl(wp_lvl.get()):
            if int(wp_asc.get()) > int(wp_lvl.get()):
                list_error.add("error_07")
            if int(wp_asc.get()) not in list_wp_asc:
                list_error.add("error_33")
        else:
            list_error.add("error_21")

    
    if "error_11" not in list_error:
        if check_lvl(wp_lvl_tar.get()):
            if int(tar_wp_asc.get()) > int(wp_lvl_tar.get()):
                list_error.add("error_34")
            if int(tar_wp_asc.get()) not in list_tar_wp_asc:
                list_error.add("error_35")
        else:
            list_error.add("error_22")
    
    if "error_18" not in list_error:
        if check_const(const.get()) == False:
                list_error.add("error_29")



    return list_error

def check_lvl(lvl):
    value = True
    if lvl < 1 or lvl > 90:
        value = False
    return value

def check_talent(talent):
    value = True
    if talent < 1 or talent > 10:
        value = False
    return value

def check_const(const):
    value = True
    if const < 0 or const > 6:
        value = False
    return value

def error_list(dict_main, dict_actual, list_error):
    
    list_unic_error = list(set(list_error))
    
    
    text_error = ""

    for element_list in list_unic_error:
        # print(f"texto: {text_error}")
        text_error += "\n" + str(LG.translate(dict_main, dict_actual, element_list))
    # print(list_unic_error)
    return text_error



def Fix_Errors_inv(s1_t1, s1_t2, s1_t3, s1_t4, s1_t5, s2_t1, s2_t2, s2_t3, s2_t4, s2_t5, s3_t1, s3_t2, s3_t3, s3_t4, s3_t5):

    list_error = set()

    try:
        s1_t1.get()
        s2_t1.get()
        s3_t1.get()
    except:
        list_error.add("error_36")

    try:
        s1_t2.get()
        s2_t2.get()
        s3_t2.get()
    except:
        list_error.add("error_37")

    try:
        s1_t3.get()
        s2_t3.get()
        s3_t3.get()
    except:
        list_error.add("error_38")

    try:
        s1_t4.get()
        s2_t4.get()
        s3_t4.get()
    except:
        list_error.add("error_39")

    try:
        s1_t5.get()
        s2_t5.get()
        s3_t5.get()
    except:
        list_error.add("error_40")

    return list_error



