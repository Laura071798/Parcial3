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
it.start()
a_0 = placa.get_pin('a:0:i')
a_1 = placa.get_pin('a:1:i')
a_2 = placa.get_pin('a:2:i')
time.sleep(1)
ventana = Tk()
ventana.geometry('800x400')
ventana.title("Parcial")

# Fetch the service account key JSON file contents
cred = credentials.Certificate(r'C:/Users/laura/Documents/Herramientas2/Parcial/keys/key.json')
# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://parcial3-65f7c.firebaseio.com/'
})

frame1 = Frame(ventana, bg="gray", highlightthickness=1, width=400, height=300, bd= 5)
frame1.place(x = 200,y = 50)
b=Label(frame1,text="")




valor= Label(frame1, bg='mediumpurple1', font=("Arial Bold", 15), fg="white", width=5)
adc_data=StringVar()
valor2 = Label(frame1, bg='mediumpurple1', font=("Arial Bold", 15), fg="white", width=5)
adc_data2=StringVar()
valor3= Label(frame1, bg='mediumpurple1', font=("Arial Bold", 15), fg="white", width=5)
adc_data3=StringVar()


def adc_read():
        x=a_0.read()
        print(x)
        adc_data.set(x)
        y=a_1.read()
        print(y)
        adc_data2.set(y)
        z=a_2.read()
        print(z)
        adc_data3.set(z)
        time.sleep(0.7)
        ref = db.reference('Potenciometro')
        ref.update({
            'Potenciometro/Potenciometro1': a_0.read(),
            'Potenciometro/Potenciometro2': a_1.read(),
            'Potenciometro/Potenciometro3': a_2.read()
    })
     



valor.configure(textvariable=adc_data)
valor.place(x=20, y=30)
valor2.configure(textvariable=adc_data2)
valor2.place(x=20, y=90)
valor3.configure(textvariable=adc_data3)
valor3.place(x=20, y=150)

prom_15=Button(frame1,text="send",command=adc_read)
prom_15.place(x=120, y=90)


ventana.mainloop()