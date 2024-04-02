from customtkinter import *
import tkinter

app = CTk()
app.geometry("500x400")
def  teste():
    print("teste")

Titulo = CTkLabel(master=app, text="Reinf RPA")
Titulo.pack( padx=30,pady = 100,anchor="s")
btnExecutar = CTkButton(master=app, text="Executar",  command=teste )
btnExecutar.place(relx= 0.5,rely = 0.5, anchor= "center")


btnLog = CTkButton(master=app, text="Log Erros",width=20)
btnLog.place(relx=0.1,rely = 0.9, anchor="n")
app.title = "Reinf RPA"
app.mainloop()
