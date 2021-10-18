# -*- coding: utf-8 -*-
from selenium import webdriver
import time

usr = "" #nombreusuario que en este caso corresponde al mail
pswd = "" #password actual
#menu
print("Eliga una opcion para la pagina uefa.com: 1.inicio de sesion 2.reestablecer pass 3. modificar pass 4. Crear cuenta")
el = int(input())
if el == 1:
    print("iniciando sesion")
    browser = webdriver.Firefox()#teniendo geckodriver en usr/local/bin
    browser.maximize_window()
    browser.get("https://www.falabella.com/falabella-cl") #ingresamos a la pag
    time.sleep(5) #dejamos que cargue todos los elementos durante 5s
    linklogin = browser.find_element_by_class_name("UserActions-module_utils-span-lower__1lYdm")
    browser.implicitly_wait(20)
    linklogin.click()
    browser.implicitly_wait(20)
    time.sleep(3)
    username_box=browser.find_element_by_name("email")
    username_box.send_keys(usr)
    password_box=browser.find_element_by_name("password")
    password_box.send_keys(pswd)
    time.sleep(3)
    browser.implicitly_wait(20)
    login_btn=browser.find_element_by_class_name('jsx-2406274020 login-btn')
    login_btn.submit()
    print("sesion iniciada")

elif el == 2:
    print("Reestableciendo password")
    browser = webdriver.Firefox()#teniendo geckodriver en usr/local/bin
    browser.maximize_window()
    browser.get("https://www.falabella.com/falabella-cl/myaccount/passwordRecoverySearch") #ingresamos a la pag
    time.sleep(3) #dejamos que cargue todos los elementos durante 3s
    username_box=browser.find_element_by_name("email")
    username_box.send_keys(usr)
    browser.implicitly_wait(20)
    bt = browser.find_element_by_id("testId-button-submit-email")
    browser.implicitly_wait(20)
    bt.click()
    print("Para completar este paso, siga las instrucciones del mail que se envió")

elif el == 3:
    print("Escriba su nueva password(Min. 8 car , 1 mayuscula minimo, 1 minuscula minimo, 1 numero minimo y sin espacios): ")
    nuepas = raw_input() #recibimos por terminal la nueva password
    browser = webdriver.Firefox()#teniendo geckodriver en usr/local/bin
    browser.maximize_window()
    browser.get("https://www.falabella.com/falabella-cl/myaccount/userPersonalInformation") #ingresamos a la pag
    time.sleep(3) #dejamos que cargue todos los elementos durante 3s
    username_box=browser.find_element_by_name("email")
    username_box.send_keys(usr)
    password_box=browser.find_element_by_name("password")
    password_box.send_keys(pswd)
    time.sleep(3)
    browser.implicitly_wait(20)
    boton = browser.find_element_by_class_name('jsx-2406274020 login-btn-text')
    boton.click()
    boton.submit()#iniciamos sesion
    time.sleep(2)
    ccontr = browser.find_element_by_class_name("copy1 primary  jsx-3743296357 bold")
    ccontr.click()
    time.sleep(2)
    pasant = browser.find_element_by_name("currentPassword")
    pasant.send_keys(pswd)
    pasact = browser.find_element_by_name("newPassword")
    pasact.send_keys(nuepas)
    botons = browser.find_elements_by_id("testId-Button-submit")

elif el == 4:
    print("Creando cuenta")
    print("Ingrese nombre,apellido,rut,celular,email,password(Min. 8 car , 1 mayuscula minimo, 1 minuscula minimo, 1 numero minimo y sin espacios)")
    nom = raw_input()
    ape = raw_input()
    rut = raw_input()
    cel = raw_input()
    corr = raw_input()
    pas = raw_input()
    browser = webdriver.Firefox()#teniendo geckodriver en usr/local/bin
    browser.maximize_window()
    browser.get("https://www.falabella.com/falabella-cl/myaccount/registration") #ingresamos a la pag
    time.sleep(3) #dejamos que cargue todos los elementos durante 3s
    nombre_box=browser.find_element_by_name("firstName")
    nombre_box.send_keys(nom)
    apellido_box=browser.find_elements_by_name("lastName")
    apellido_box.send_keys(ape)
    rut_box=browser.find_elements_by_name("document")
    rut_box.send_keys(rut)
    cel_box=browser.find_elements_by_name("phoneNumber")
    cel_box.send_keys(cel)
    correo_box=browser.find_elements_by_name("email")
    correo_box.send_keys(corr)
    pass_box=browser.find_elements_by_name("password")
    pass_box.send_keys(pas)
    browser.implicitly_wait(20)
    browser.find_element_by_id("testId-consent-consentTemplateRegistroTyC_FAL_CL-input")
    browser.click()
    browser.find_element_by_id("testId-consent-consentTemplateRegistroPdP_FAL_CL-input")
    browser.click()
    browser.implicitly_wait(20)
    browser.find_element_by_id("testId-Button-submit")
    browser.click()
    browser.submit()
    print("Cuenta creada")

else:
    print("error")
