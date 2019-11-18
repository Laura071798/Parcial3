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
led = placa.get_pin('d:9:p') 
led2 = placa.get_pin('d:10:p') 
led3 = placa.get_pin('d:11:p') 

# Fetch the service account key JSON file contents
cred = credentials.Certificate(r'C:/Users/laura/Documents/Herramientas2/Parcial/keys/key.json')
# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://parcial3-65f7c.firebaseio.com/'
})


ventana = Tk()
ventana.geometry('750x250')
ventana.configure(bg = 'light slate blue')
ventana.title("Parcial")
texto = Label(ventana, text="CAMBIO DE INTENSIDAD GET FIREBASE", bg='light slate blue', font=("Arial Bold", 25), fg="white")
texto.grid(padx=20, pady=20,column=0, row=0)

def led_pwm():
    ref = db.reference("Potenciometro/Potenciometro")
    x=ref.get()
    print(x)
    print(x.get('Potenciometro1'))
    led.write(x.get('Potenciometro1'))

def led_pwm2():
    ref = db.reference("Potenciometro/Potenciometro")
    x=ref.get()
    print(x)
    print(x.get('Potenciometro2'))
    led2.write(x.get('Potenciometro2'))

def led_pwm3():
    ref = db.reference("Potenciometro/Potenciometro")
    x=ref.get()
    print(x)
    print(x.get('Potenciometro3'))
    led3.write(x.get('Potenciometro3'))
 

adc1_update=Button(ventana,text="adc1_update",command=led_pwm)
adc1_update.place(x=50, y=100)
adc2_update=Button(ventana,text="adc2_update",command=led_pwm2)
adc2_update.place(x=150, y=100)
adc3_update=Button(ventana,text="adc3_update",command=led_pwm3)
adc3_update.place(x=250, y=100)





ventana.mainloop()