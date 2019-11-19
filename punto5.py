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
led1= placa.get_pin('d:9:o') 
led2= placa.get_pin('d:11:o') 
led3= placa.get_pin('d:13:o') 
time.sleep(1)
ventana = Tk()
ventana.geometry('800x400')
ventana.title("Parcial")

# Fetch the service account key JSON file contents
cred = credentials.Certificate(r'C:/Users/laura/Documents/Herramientas2/Parcial/keys3/key3.json')
# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://punto5.firebaseio.com//'
})

frame1 = Frame(ventana, bg="mediumpurple1", highlightthickness=1, width=400, height=300, bd= 5)
frame1.place(x = 150,y = 50)
b=Label(frame1,text="")




valor= Label(frame1, bg='mediumpurple1', font=("Arial Bold", 55), fg="white", width=7)
valor2= Label(frame1, text='°C', bg='mediumpurple1', font=("Arial Bold", 55), fg="white", width=2)
valor3= Label(frame1, text='', bg='mediumpurple1', font=("Arial Bold", 55), fg="white", width=2)
valor2.place(x=280, y=50)
valor3.place(x=120, y=150)
adc_data=StringVar()


def adc_read():
        x=a_0.read()
        print(x)
        adc_data.set(x*100/2)
        time.sleep(0.7)
        if (x*100/2)<10:
            valor3.configure(text='TEMPERATURA BAJA', bg='white', font=("Arial Bold", 7), fg="blue", width=15)
            led1.write(1)
            time.sleep(1)
        if (x*100/2)>10 and (x*100/2)<25:
            valor3.configure(text='TEMPERATURA MEDIA', bg='white', font=("Arial Bold", 7), fg="yellow", width=15)
            led3.write(1)
            time.sleep(1)
        if (x*100/2)>30:
            valor3.configure(text='TEMPERATURA ALTA', bg='white', font=("Arial Bold", 7), fg="red", width=15)
            led2.write(1)
            time.sleep(1)
            
            
        ref = db.reference('sensor')
        ref.update({
            'sensor/Temperatura': x*100/2,
                })
    


    


valor.configure(textvariable=adc_data)
valor.place(x=5, y=50)



prom_15=Button(frame1,text="send",command=adc_read)
prom_15.place(x=20, y=200)


ventana.mainloop()