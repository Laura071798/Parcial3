import firebase_admin
from firebase_admin import credentials
from firebase_admin import db



from pyfirmata import Arduino, util
from tkinter import *
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
cred = credentials.Certificate(r'C:/Users/laura/Documents/Herramientas2/Parcial/keys/key.json')
# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://parcial3-65f7c.firebaseio.com/'
})

ventana = Tk()
ventana.geometry('850x850')
ventana.configure(bg = 'white')
ventana.title("Bienvenidos a las UI")
texto = Label(ventana, text="entry", bg='cadet blue1', font=("Arial Bold", 14), fg="white")
texto.place(x=20, y=20)
texto = Label(ventana, text="ON(1)-OFF(0)", bg='cadet blue1', font=("Arial Bold", 14), fg="white")
texto.place(x=20, y=100)

status=''

def entrada(input):
    content = dato.get()
    content2= dato2.get()
    dato.delete(0, END)
    dato2.delete(0,END)
    if int(content)== 8:
        if int(content2)==1:
            led1.write(1)
            status= 'ON'
        if int(content2)==0:
            led1.write(0)
            status= 'OFF'
    if int(content)== 9:
        if int(content2)==1:
            led2.write(1)
            status= 'ON'
        if int(content2)==0:
            led2.write(0)
            status= 'OFF'
    if int(content)== 10:
        if int(content2)==1:
            led3.write(1)
            status= 'ON'
        if int(content2)==0:
            led3.write(0)
            status= 'OFF'
    if int(content)== 11:
        if int(content2)==1:
            led4.write(1)
            status= 'ON'
        if int(content2)==0:
            led4.write(0)
            status= 'OFF'
    if int(content)== 12:
        if int(content2)==1:
            led5.write(1)
            status= 'ON'
        if int(content2)==0:
            led5.write(0)
            status= 'OFF'
    if int(content)== 13:
        if int(content2)==1:
            led6.write(1)
            status= 'ON'
        if int(content2)==0:
            led6.write(0)
            status= 'OFF'
    else: 
        popup = Tk()
        popup.wm_title("")
        label = Label(popup, text="digite otro numero", font="Arial")
        label.pack()
        B1 = Button(popup, text="Okay", command = popup.destroy)
        B1.pack()
        popup.mainloop()
    ref = db.reference('Potenciometro')
    ref.update({
            'Potenciometro/Numero de LED': content,
            'Potenciometro/Status': status
    })
    
Label(ventana, text="Input: ").place(x=20, y=60)
dato = Entry(ventana)
dato.place(x=90, y=60)
dato.bind('<Return>', entrada) 

Label(ventana, text="Input: ").place(x=20, y=150)
dato2 = Entry(ventana)
dato2.place(x=90, y=150)
dato2.bind('<Return>', entrada) 

prom_15=Button(ventana,text="Guardar",command=entrada)
prom_15.place(x=120, y=90)

ventana.mainloop()