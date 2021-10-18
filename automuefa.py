# -*- coding: utf-8 -*-
from selenium import webdriver
import time

usr = "vhencripto@gmail.com" #nombreusuario que en este caso corresponde al mail
pswd = "Hola 123" #password actual
nameus = "Vincent" #nombre que usaste en la pagina para ingresar(ej. Jaime)
#menu
print("Eliga una opcion para la pagina uefa.com: 1.inicio de sesion 2.reestablecer pass 3. modificar pass 4. Crear cuenta")
el = int(input())
if el == 1:
    print("iniciando sesion")
    browser = webdriver.Firefox()#teniendo geckodriver en usr/local/bin
    browser.maximize_window()
    browser.get("https://www.uefa.com") #ingresamos a la pag
    time.sleep(5) #dejamos que cargue todos los elementos durante 5s
    linklogin = browser.find_element_by_link_text("Login")
    browser.implicitly_wait(20)
    linklogin.click()
    browser.implicitly_wait(20)
    linklogin.click()
    browser.implicitly_wait(20)
    username_box=browser.find_element_by_name("username")
    username_box.send_keys(usr)
    password_box=browser.find_element_by_name("password")
    password_box.send_keys(pswd)
    login_btn=browser.find_element_by_class_name("gigya-input-submit")
    login_btn.submit()
    print("sesion iniciada")

elif el == 2:
    print("Reestableciendo password")
    browser = webdriver.Firefox()#teniendo geckodriver en usr/local/bin
    browser.maximize_window()
    browser.get("https://www.uefa.com") #ingresamos a la pag
    time.sleep(5) #dejamos que cargue todos los elementos durante 5s
    linklogin = browser.find_element_by_link_text("Login")
    browser.implicitly_wait(20)
    linklogin.click()
    browser.implicitly_wait(20)
    time.sleep(3)
    resetpas = browser.find_element_by_link_text("I forgot my password") #olvidamos la pass
    resetpas.click()
    email_box=browser.find_element_by_name("username")
    email_box.send_keys(usr)#rellenamos con nuestro mail
    reset_btn=browser.find_element_by_class_name("gigya-input-submit")
    reset_btn.submit()
    print("Para terminar el proceso, ingrese al mail correspondiente")

elif el == 3:
    print("Escriba su nueva password(Min. 8 car , 1 mayuscula minimo, 1 minuscula minimo, 1 numero minimo y 1 caracter especial): ")
    nuepas = raw_input() #recibimos por terminal la nueva password
    browser = webdriver.Firefox()#teniendo geckodriver en usr/local/bin
    browser.maximize_window()
    browser.get("https://www.uefa.com")
    time.sleep(5)
    linklogin = browser.find_element_by_link_text("Login")
    browser.implicitly_wait(20)
    linklogin.click()
    browser.implicitly_wait(20)
    linklogin.click()
    browser.implicitly_wait(20)
    username_box=browser.find_element_by_name("username")
    username_box.send_keys(usr)
    password_box=browser.find_element_by_name("password")
    password_box.send_keys(pswd)
    login_btn=browser.find_element_by_class_name("gigya-input-submit")
    login_btn.submit() #inicio de sesion
    time.sleep(3)
    userin = browser.find_element_by_link_text(nameus)
    userin.click()
    userin2 = browser.find_element_by_link_text("Profile")
    userin2.click()
    time.sleep(2)
    changepas = browser.find_element_by_xpath('//div[contains(text(),"Change password")]')
    changepas.click()
    #time.sleep(2)
    password_box1=browser.find_element_by_xpath('//input[@id="gigya-password-password"]')
    password_box1.send_keys(pswd)
    Pasres = nuepas
    newpass= browser.find_element_by_xpath('//input[@id="gigya-password-newPassword"]')
    newpass.send_keys(Pasres) #ingresamos la nueva password
    repas= browser.find_element_by_xpath('//input[@id="gigya-password-passwordRetype"]')
    repas.send_keys(Pasres) #reingresamos
    confnp = browser.find_element_by_xpath('//input[@value="Submit"]')
    confnp.submit()

elif el == 4:
    print("Escriba el mail de la cuenta: ")
    cuenta = raw_input() #recibimos la nueva cuenta
    print("Escriba la password de la cuenta(Min. 8 car , 1 mayuscula minimo, 1 minuscula minimo, 1 numero minimo y 1 caracter especial): ")
    pasw = raw_input() #recibimos la nueva pass
    print("Escriba su primer nombre: ")
    prnom = raw_input() #recibimos el nombre
    print("Escriba su apellido: ")
    apellido = raw_input() #recibimos el apellido
    print("Escriba el dia de nacimiento: ")
    dia = raw_input() #recibimos el dia
    print("Escriba el mes de nacimiento: ")
    mes = raw_input() #recibimos el mes
    print("Escriba el año de nacimiento: ")
    anio = raw_input() #recibimos año
    
    browser = webdriver.Firefox()#teniendo geckodriver en usr/local/bin
    browser.maximize_window()
    browser.get("https://www.uefa.com") #ingresamos a la pag
    time.sleep(5) #dejamos que cargue todos los elementos durante 5s
    linklogin = browser.find_element_by_link_text("Login")
    browser.implicitly_wait(20)
    linklogin.click()
    browser.implicitly_wait(20)
    linklogin.click()
    browser.implicitly_wait(20)
    ncuenta = browser.find_element_by_link_text("Create your UEFA account")
    browser.implicitly_wait(20)
    ncuenta.submit()
    browser.implicitly_wait(20)
    ncuenta.click()
    email_box=browser.find_element_by_name("email")
    email_box.send_keys(cuenta)
    psw_box=browser.find_element_by_name("password")
    psw_box.send_keys(pasw)
    name_box=browser.find_element_by_name("profile.firstName")
    name_box.send_keys(prnom)
    apell_box=browser.find_element_by_name("profile.lastName")
    apell_box.send_keys(apellido)
    dia_box=browser.find_element_by_name("profile.birthDay")
    dia_box.send_keys(dia)
    mes_box=browser.find_element_by_name("profile.birthMonth")
    mes_box.send_keys(mes)
    anio_box=browser.find_element_by_name("profile.birthYear")
    anio_box.send_keys(anio)
    terminos = browser.find_element_by_link_text("I accept UEFA's")
    terminos.click()
    crear = browser.find_element_by_link_text("Create account")

else:
    print("error")
