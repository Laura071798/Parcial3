import firebase_admin
from firebase_admin import credentials
from firebase_admin import db


from pyfirmata import Arduino, util
from tkinter import *
from PIL import Image
from PIL import ImageTk
import time

placa = Arduino ('COM4')
it = util.Iterator(placa)
#inicio el iteratodr
it.start()

led1= placa.get_pin('d:8:o') 
led2= placa.get_pin('d:9:o') 
led3= placa.get_pin('d:10:o') 
led4= placa.get_pin('d:11:o') 
led5= placa.get_pin('d:12:o') 
led6= placa.get_pin('d:13:o') 

# Fetch the service account key JSON file contents
cred = credentials.Certificate(r'C:/Users/laura/Documents/Herramientas2/Parcial/keys2/key2.json')
# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://punto4-67946.firebaseio.com/'
})


ventana = Tk()
ventana.geometry('980x450')
ventana.configure(bg = 'red')
ventana.title("Parcial")
texto = Label(ventana, text="BASE DE DATOS ESTUDIANTES EN CASO DE EMERGENCIA", bg='red', font=("Arial Bold", 25), fg="white")
texto.grid(padx=0, pady=20,column=0, row=0)

b=Label(ventana,text="")
img = Image.open("C:/Users/laura/Pictures/help.png")
img = img.resize((150,150), Image.ANTIALIAS)
photoImg=  ImageTk.PhotoImage(img)
b.configure(image=photoImg)
b.place(x = 760,y = 250)

def datos_persona():
    
    content = dato.get()
    content2= dato2.get()
    content3=dato3.get()
    dato.delete(0, END)
    dato2.delete(0,END)
    dato3.delete(0,END)
    
    ref = db.reference('Persona')
    ref.update({
            'Persona/Nombre': content,
            'Persona/Edad': content2,
            'Persona/Telefono': content3
    })
    
def edad_leds():
    ref = db.reference("Persona/Persona")
    x=ref.get()
    y=x.get('Edad')
    print(y)
    if int(y)==5:
        led1.write(0)
        led2.write(0)
        led3.write(0)
        led4.write(1)
        led5.write(0)
        led6.write(1)
        time.sleep(1)
    if int(y)==6:
        led1.write(0)
        led2.write(0)
        led3.write(0)
        led4.write(1)
        led5.write(1)
        led6.write(0)
        time.sleep(1)
    if int(y)==7:
        led1.write(0)
        led2.write(0)
        led3.write(0)
        led4.write(0)
        led5.write(0)
        led6.write(1)
        time.sleep(1)
    if int(y)==8:
        led1.write(0)
        led2.write(0)
        led3.write(1)
        led4.write(0)
        led5.write(0)
        led6.write(0)
        time.sleep(1)
    if int(y)==9:
        led1.write(0)
        led2.write(0)
        led3.write(1)
        led4.write(0)
        led5.write(0)
        led6.write(1)
        time.sleep(1)
    if int(y)==10:
        led1.write(0)
        led2.write(0)
        led3.write(1)
        led4.write(0)
        led5.write(1)
        led6.write(0)
        time.sleep(1)
    if int(y)==11:
        led1.write(0)
        led2.write(0)
        led3.write(1)
        led4.write(0)
        led5.write(1)
        led6.write(1)
        time.sleep(1)
    if int(y)==12:
        led1.write(0)
        led2.write(0)
        led3.write(1)
        led4.write(1)
        led5.write(0)
        led6.write(0)
        time.sleep(1)
    if int(y)==13:
        led1.write(0)
        led2.write(0)
        led3.write(1)
        led4.write(1)
        led5.write(0)
        led6.write(1)
        time.sleep(1)
    if int(y)==14:
        led1.write(0)
        led2.write(0)
        led3.write(1)
        led4.write(1)
        led5.write(1)
        led6.write(0)
        time.sleep(1)
    if int(y)==15:
        led1.write(0)
        led2.write(0)
        led3.write(1)
        led4.write(1)
        led5.write(1)
        led6.write(1)
        time.sleep(1)
    if int(y)==16:
        led1.write(0)
        led2.write(1)
        led3.write(0)
        led4.write(0)
        led5.write(0)
        led6.write(0)
        time.sleep(1)
    if int(y)==17:
        led1.write(0)
        led2.write(1)
        led3.write(0)
        led4.write(0)
        led5.write(0)
        led6.write(1)
        time.sleep(1)
    if int(y)==18:
        led1.write(0)
        led2.write(1)
        led3.write(0)
        led4.write(0)
        led5.write(1)
        led6.write(0)
        time.sleep(1)
    if int(y)==19:
        led1.write(0)
        led2.write(0)
        led3.write(0)
        led4.write(0)
        led5.write(0)
        led6.write(1)
        time.sleep(1)
    if int(y)==20:
        led1.write(0)
        led2.write(1)
        led3.write(0)
        led4.write(1)
        led5.write(0)
        led6.write(0)
        time.sleep(1)
    if int(y)==21:
        led1.write(0)
        led2.write(1)
        led3.write(0)
        led4.write(1)
        led5.write(0)
        led6.write(1)
        time.sleep(1)
    if int(y)==22:
        led1.write(0)
        led2.write(1)
        led3.write(0)
        led4.write(1)
        led5.write(1)
        led6.write(0)
        time.sleep(1)
    if int(y)==23:
        led1.write(0)
        led2.write(0)
        led3.write(0)
        led4.write(0)
        led5.write(0)
        led6.write(1)
        time.sleep(1)
    if int(y)==24:
        led1.write(0)
        led2.write(1)
        led3.write(1)
        led4.write(0)
        led5.write(0)
        led6.write(0)
        time.sleep(1)
    else:   
        led1.write(0)
        led2.write(0)
        led3.write(0)
        led4.write(0)
        led5.write(0)
        led6.write(0)
        time.sleep(1)
    
        



Label(ventana, text="Nombre: ").place(x=20, y=80)
dato = Entry(ventana)
dato.place(x=90, y=80)
dato.bind('<Return>', datos_persona) 

Label(ventana, text="Edad: ").place(x=20, y=120)
dato2 = Entry(ventana)
dato2.place(x=90, y=120)
dato2.bind('<Return>', datos_persona) 

Label(ventana, text="Telefono: ").place(x=20, y=160)
dato3 = Entry(ventana)
dato3.place(x=90, y=160)
dato3.bind('<Return>', datos_persona) 


update=Button(ventana,text="enviar",command=datos_persona)
update.place(x=250, y=100)

get=Button(ventana,text="edad binario",command=edad_leds)
get.place(x=350, y=100)




ventana.mainloop()