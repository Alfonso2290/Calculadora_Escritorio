
from tkinter import *

ventana=Tk()

miFrame=Frame(ventana)
miFrame.pack()

valor=StringVar()
operacion=StringVar()
res=StringVar()
resFinal=StringVar()
contador=StringVar()
operador=StringVar()
mensaje=StringVar()
valor.set("0")
resFinal.set("0")

#---------------------------pantalla--------------------
preResultado=Entry(miFrame,bg="black",fg="#03f943",justify="right",textvariable=operacion)
preResultado.grid(row=0,column=1,padx=1,columnspan=4)

pantalla=Entry(miFrame,bg="black",fg="#03f943",justify="right",textvariable=valor)
pantalla.grid(row=1,column=1,padx=1,columnspan=4)
pantalla.focus()

fondo=Entry(miFrame,state=DISABLED,textvariable=mensaje)
fondo.grid(row=2,column=1,padx=1,pady=1,columnspan=4)

#---------------------------funciones-------------------
def deshabilitarOperadores():
	botonSum.config(state=DISABLED)
	botonMul.config(state=DISABLED)
	botonDiv.config(state=DISABLED)
	botonRes.config(state=DISABLED)

def habilitarOperadores():
	botonSum.config(state=NORMAL)
	botonMul.config(state=NORMAL)
	botonDiv.config(state=NORMAL)
	botonRes.config(state=NORMAL)

def cantidadPuntosDecimales():
	texto=valor.get()
	cont=0
	for i in texto:
		if(i=="."):
			cont+=1
	if(cont==0):
		return True
	else:
		return False

def pulsarTeclado(num):

	habilitarOperadores() 
	if(res.get()==valor.get()):
		if((valor.get()=="0" or valor.get()=="0.0") and num=="."):
			valor.set("0")
			res.set("")
		else:
			valor.set("")
			res.set("")
		
	if(valor.get()=="0" or valor.get()=="0.0"):
		if(num=="0"):
			valor.set("0")
		elif(num=="."):
			valor.set(valor.get() + num)
		else:
			valor.set(num)
	elif(num=="."):
		if(cantidadPuntosDecimales()):
			if(valor.get()==""):
				valor.set("0" + num)
			else:
				valor.set(valor.get() + num)
	else:
		valor.set(valor.get() + num)

def limpiarPantalla():
	valor.set("0")
	operacion.set("")
	resFinal.set("0")
	operador.set("")
	pantalla.config(state=NORMAL)
	preResultado.config(state=NORMAL)
	boton0.config(state=NORMAL)
	boton1.config(state=NORMAL)
	boton2.config(state=NORMAL)
	boton3.config(state=NORMAL)
	boton4.config(state=NORMAL)
	boton5.config(state=NORMAL)
	boton6.config(state=NORMAL)
	boton7.config(state=NORMAL)
	boton8.config(state=NORMAL)
	boton9.config(state=NORMAL)
	botonSum.config(state=NORMAL)
	botonMul.config(state=NORMAL)
	botonDiv.config(state=NORMAL)
	botonRes.config(state=NORMAL)
	botonComa.config(state=NORMAL)
	botonIgual.config(state=NORMAL)
	mensaje.set("")

def deshabilitarElementos():
	pantalla.config(state=DISABLED)
	preResultado.config(state=DISABLED)
	boton0.config(state=DISABLED)
	boton1.config(state=DISABLED)
	boton2.config(state=DISABLED)
	boton3.config(state=DISABLED)
	boton4.config(state=DISABLED)
	boton5.config(state=DISABLED)
	boton6.config(state=DISABLED)
	boton7.config(state=DISABLED)
	boton8.config(state=DISABLED)
	boton9.config(state=DISABLED)
	botonSum.config(state=DISABLED)
	botonMul.config(state=DISABLED)
	botonDiv.config(state=DISABLED)
	botonRes.config(state=DISABLED)
	botonComa.config(state=DISABLED)
	botonIgual.config(state=DISABLED)

def pulsarOperacion(ope):
	
	deshabilitarOperadores()
	numero=float(resFinal.get())
	numero2=float(valor.get())
	operacion.set(operacion.get() + valor.get()+ " " +ope)
	signo=operador.get()
	if(signo=="+"):
		resFinal.set(numero + numero2)
	elif(signo=="-"):
		resFinal.set(numero - numero2)
	elif(signo=="x"):
		resFinal.set(numero * numero2)
	elif(signo=="/"):
		if(numero2==0):
			mensaje.set("ERROR:División entre 0")
			valor.set("")
			deshabilitarElementos()
		else:
			resFinal.set(numero / numero2)
	else:
		resFinal.set(numero2)
	if(mensaje.get()!="ERROR:División entre 0"):
		valor.set(resFinal.get())
	res.set(resFinal.get())
	operador.set(ope)

def mostrarResultado(igu):

	habilitarOperadores()
	num2=float(valor.get())
	num1=float(resFinal.get())
	opera=operador.get()
	if(opera=="+"):
		valor.set(num1 + num2)
	elif(opera=="-"):
		valor.set(num1 - num2)
	elif(opera=="x"):
		valor.set(num1 * num2)
	elif(opera=="/"):
		try:
			valor.set(num1 / num2)
		except ZeroDivisionError:
			mensaje.set("ERROR:División entre 0")
			deshabilitarElementos()
	operacion.set("")
	operador.set("")
	res.set(valor.get())


#-------------------------fila 1------------------------
boton7=Button(miFrame,text="7",width=2,command=lambda:pulsarTeclado("7"))
boton7.grid(row=3,column=1,padx=1,pady=1)
boton8=Button(miFrame,text="8",width=2,command=lambda:pulsarTeclado("8"))
boton8.grid(row=3,column=2,padx=1,pady=1)
boton9=Button(miFrame,text="9",width=2,command=lambda:pulsarTeclado("9"))
boton9.grid(row=3,column=3,padx=1,pady=1)
botonDiv=Button(miFrame,text="/",width=2,command=lambda:pulsarOperacion("/"))
botonDiv.grid(row=3,column=4,padx=1,pady=1)

#-------------------------fila 2------------------------
boton4=Button(miFrame,text="4",width=2,command=lambda:pulsarTeclado("4"))
boton4.grid(row=4,column=1,padx=1,pady=1)
boton5=Button(miFrame,text="5",width=2,command=lambda:pulsarTeclado("5"))
boton5.grid(row=4,column=2,padx=1,pady=1)
boton6=Button(miFrame,text="6",width=2,command=lambda:pulsarTeclado("6"))
boton6.grid(row=4,column=3,padx=1,pady=1)
botonMul=Button(miFrame,text="x",width=2,command=lambda:pulsarOperacion("x"))
botonMul.grid(row=4,column=4,padx=1,pady=1)

#-------------------------fila 3------------------------
boton1=Button(miFrame,text="1",width=2,command=lambda:pulsarTeclado("1"))
boton1.grid(row=5,column=1,padx=1,pady=1)
boton2=Button(miFrame,text="2",width=2,command=lambda:pulsarTeclado("2"))
boton2.grid(row=5,column=2,padx=1,pady=1)
boton3=Button(miFrame,text="3",width=2,command=lambda:pulsarTeclado("3"))
boton3.grid(row=5,column=3,padx=1,pady=1)
botonRes=Button(miFrame,text="-",width=2,command=lambda:pulsarOperacion("-"))
botonRes.grid(row=5,column=4,padx=1,pady=1)

#-------------------------fila 4------------------------
boton0=Button(miFrame,text="0",width=2,command=lambda:pulsarTeclado("0"))
boton0.grid(row=6,column=1,padx=1,pady=1)
botonComa=Button(miFrame,text=".",width=2,command=lambda:pulsarTeclado("."))
botonComa.grid(row=6,column=2,padx=1,pady=1)
botonIgual=Button(miFrame,text="=",width=2,command=lambda:mostrarResultado("="))
botonIgual.grid(row=6,column=3,padx=1,pady=1)
botonSum=Button(miFrame,text="+",width=2,command=lambda:pulsarOperacion("+"))
botonSum.grid(row=6,column=4,padx=1,pady=1)

##-------------------------fila 5------------------------
botonLimpiar=Button(miFrame,text="limpiar",width=16,command=limpiarPantalla)
botonLimpiar.grid(row=7,column=1,padx=1,pady=10,columnspan=4)


ventana.mainloop()