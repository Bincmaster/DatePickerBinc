from tkinter import *
from tkinter import ttk
from tkinter import messagebox
#from ventanas_menu.V_Islas.RP import *
#from ventanas_menu.V_Islas.lista_fechas import *
from lista_fechas import *#En este modulo importamos la lista de meses dias y años, como al igual lo años biciestos
from io import *

class vdatepiker(Frame):
	def __init__(self, subraiz, placey, place, vfecha):#el place y y el placex son las variables que resivira el datepiker para ubicarlo
#                                                   en nuestra ventana principal	

#--------------variables del date piker----------------------
		self.datosmeses=Meses
		self.datosdias=Dias
		self.datosanios=Anios
		self.datosaniosbic=aniosbiciestos
		self.Vdias=StringVar()
		self.Vmeses=StringVar()
		self.Vanios=StringVar() 
		self.datofecha=vfecha
		self.calendarioimg=PhotoImage(file="multimedia\\Calendario.png")
#-------------------------Las siguentes variables a declarar sion las que por el estado inicial recivira el date piker de la ventana 
#						  principal la cual la localizara mediante un place
		self.placey=placey
		self.placex=placex		

#--------------------configucarion del frame---------------------		
		self.subraiz=Frame()
		self.subraiz.config(width=160, height=72)
		self.subraiz.place(x=self.placex.get(), y=self.placey.get())
		self.menudatepiker()

#----------------------------en la siguientes funciones declararemos la cosntrucion de los date piker

	def menudatepiker(self):
		
		self.t_meses=Label(self.subraiz, text="Mes: ")
		self.listado_mes=ttk.Combobox(self.subraiz,width=7, font=("Arial",9), state='readonly', textvariable=self.Vmeses)
		self.listado_mes['values']=self.datosmeses
		self.listado_mes.bind("<<ComboboxSelected>>", self.funciodias)		
		self.t_dias=Label(self.subraiz, text="Dias: ")
		self.listado_dias=ttk.Combobox(self.subraiz,width=2, font=("Arial",9), state='readonly', textvariable=self.Vdias)
		self.listado_dias.bind("<<ComboboxSelected>>", self.funcianios)
		self.t_anios=Label(self.subraiz, text="Años: ")
		self.listado_anios=ttk.Combobox(self.subraiz,width=4, font=("Arial",9), state='readonly', textvariable=self.Vanios)
		self.listado_anios.bind("<<ComboboxSelected>>", self.enviardatosfecha)		
		
		self.t_fecha=Label(self.subraiz, text="FECHA:", font=("Arial",10,"bold"))
		self.t_fecha.place(y=5, x=1)
		self.Boton_fecha=Button(self.subraiz, relief=FLAT, width=18, height=18, image=self.calendarioimg, command=self.borarOmostrar)
		self.Boton_fecha.place(y=3, x=55)

#-----------------------------------------Funciones del datepiker-----------------------------

	def borarOmostrar(self):
		if self.t_meses.place_info() != {}:
			self.t_meses.place_forget()
			self.listado_mes.place_forget()
			self.t_dias.place_forget()
			self.listado_dias.place_forget()
			self.t_anios.place_forget()
			self.listado_anios.place_forget()
				
		else:
			self.t_meses.place(y=28, x=1)
			self.listado_mes.place(y=50, x=1)
			self.t_dias.place(y=28, x=75)
			self.listado_dias.place(y=50, x=73)
			self.t_anios.place(y=28, x=112)
			self.listado_anios.place(y=50,x=110)




	def funciodias(self, event):

		if self.Vmeses.get()== self.datosmeses[0]:
				
			self.Vdias.set("")
			self.Vanios.set("")
			self.listado_dias['values']=self.datosdias

				
			
		elif self.Vmeses.get()== self.datosmeses[1]:
			self.Vdias.set("")
			self.Vanios.set("")
			self.listado_dias['values']=self.datosdias[0:28]
			

		elif self.Vmeses.get()== self.datosmeses[2]:
			self.Vdias.set("")
			self.Vanios.set("")
			self.listado_dias['values']=self.datosdias
			

		elif self.Vmeses.get()== self.datosmeses[3]:
			self.Vdias.set("")
			self.Vanios.set("")
			self.listado_dias['values']=self.datosdias[0:29]
			
			
		elif self.Vmeses.get()== self.datosmeses[4]:
			self.Vdias.set("")
			self.Vanios.set("")
			self.listado_dias['values']=self.datosdias
		
		elif self.Vmeses.get()== self.datosmeses[5]:
			self.Vdias.set("")
			self.Vanios.set("")
			self.listado_dias['values']=self.datosdias[0:29]
		
		elif self.Vmeses.get()== self.datosmeses[6]:
			self.Vdias.set("")
			self.Vanios.set("")
			self.listado_dias['values']=self.datosdias
			

		elif self.Vmeses.get()== self.datosmeses[7]:
			self.Vdias.set("")
			self.Vanios.set("")
			self.listado_dias['values']=self.datosdias
			


		elif self.Vmeses.get()== self.datosmeses[8]:
			self.Vdias.set("")
			self.Vanios.set("")
			self.listado_dias['values']=self.datosdias[0:29]
			


		elif self.Vmeses.get()== self.datosmeses[9]:
			self.Vdias.set("")
			self.Vanios.set("")
			self.listado_dias['values']=self.datosdias
			


		elif self.Vmeses.get()== self.datosmeses[10]:
			self.Vdias.set("")
			self.Vanios.set("")
			self.listado_dias['values']=self.datosdias[0:29]
			

		elif self.Vmeses.get()== self.datosmeses[11]:
			self.Vdias.set("")
			self.Vanios.set("")
			self.listado_dias['values']=self.datosdias
			


		else:
			self.Vdias.set("")				
			self.Vanios.set("")
			self.listado_dias['values']=("")	

	def funcianios(self, event):
		if self.Vmeses.get()== self.datosmeses[1] and self.Vdias.get()=="29":
			self.Vanios.set("")
			self.listado_anios['values']=self.datosaniosbic	
				
		else:
			self.Vanios.set("")
			self.listado_anios['values']=self.datosanios

	def enviardatosfecha(self, event):
		self.datofecha.set(self.Vdias.get()+"/"+self.Vmeses.get()+"/"+self.Vanios.get())
		self.borarOmostrar()










root=Tk()
placey=IntVar()
placex=IntVar()
vfecha=StringVar()

run=vdatepiker(root, placey, placex, vfecha)
Entry(root, textvariable=vfecha).place(y=90, x=5)

root.mainloop()
