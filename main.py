from tkinter import *
#configurações da tela 
root= Tk()
root.title('Calculadora dos inteiros.')
root.geometry("394x400")
root.configure(background="#05eb8b")

primeiro_num = ""
divisao = FALSE
multipli = FALSE
subt = FALSE
soma = FALSE

e = Entry(root, width=25,borderwidth=10, relief=FLAT,fg= "#000000",bg="#E0FFFF",font=("futura", 15,"italic" ),justify=RIGHT)
e.grid(
    row= 0,
    column=0,
    columnspan=4,
    pady= 5
)
#funções
def click(num):
    e.insert(END,num)
    return

def tecla_div():
    global primeiro_num
    global divisao
    divisao = True
    primeiro_num = e.get()
    e.delete(0,END)
    return

def tecla_multi():
    global primeiro_num
    global multipli
    multipli = True
    primeiro_num = e.get()
    e.delete(0,END)
    return

def tecla_subt():
    global primeiro_num
    global subt
    subt = True
    primeiro_num = e.get()
    e.delete(0,END)
    return

def tecla_soma():
    global primeiro_num
    global soma
    soma = True
    primeiro_num = e.get()
    e.delete(0,END) 
    return

def tecla_limpa():
    e.delete(0,END)
    return

def tecla_igual():
    global divisao
    global multipli
    global subt
    global soma
    segundo_num = e.get()
    e.delete(0,END)
    if divisao == TRUE:
        e.insert(0,int(primeiro_num) / int(segundo_num))
        divisao = FALSE
    if multipli == TRUE:
        e.insert(0,int(primeiro_num) * int(segundo_num))
        multipli= FALSE
    if subt == TRUE:
        e.insert(0,int(primeiro_num) - int(segundo_num))
        subt = FALSE
    if soma == TRUE:
        e.insert(0,int(primeiro_num) + int(segundo_num))
        soma = FALSE
    return

#operadores
divisao = Button(root,
                text='/',
                padx=38,
                pady=20,
                command=tecla_div,
                fg='#1C1C1C',
                activebackground='#000000',
                bg="#6a9688",
                activeforeground="#09543e",
                relief=FLAT,
                font=("futura", 15,"italic"),
                justify=CENTER              
)
divisao.grid(row=0,column=4)

multipli = Button(root,
                text='X',
                padx=35,
                pady=20,
                command=tecla_multi,
                fg='#1C1C1C',
                activebackground='#000000',
                bg="#6a9688",
                activeforeground="#09543e",
                relief=FLAT,
                font=("futura", 15,"italic")              
)
multipli.grid(row=1,column=4)

subt = Button(root,
                text='-',
                padx=38,
                pady=20,
                command=tecla_subt,
                fg='#1C1C1C',
                activebackground='#000000',
                bg="#6a9688",
                activeforeground="#09543e",
                relief=FLAT,
                font=("futura", 15,"italic")              
)
subt.grid(row=2,column=4)

soma = Button(root,
                text='+',
                padx=35,
                pady=20,
                command=tecla_soma,
                fg='#1C1C1C',
                activebackground='#000000',
                bg="#6a9688",
                activeforeground="#09543e",
                relief=FLAT,
                font=("futura", 15,"italic")              
)
soma.grid(row=3,column=4)

igual = Button(root,
                text='=',
                padx=35,
                pady=20,
                command=tecla_igual,
                fg='#1C1C1C',
                activebackground='#000000',
                bg="#6a9688",
                activeforeground="#09543e",
                relief=FLAT,
                font=("futura", 15,"italic")              
)
igual.grid(row=4,column=4)


#primeira fileira de numeros!!!!!!

numero1 = Button(root,
                text='1',
                padx=35,
                pady=20,
                command=lambda:click(1),
                fg='#1C1C1C',
                activebackground='#000000',
                bg="#05eb8b",
                activeforeground="#09543e",
                relief=FLAT,
                font=("futura", 15,"italic")
)
numero1.grid(row=1,column=0)

numero2 = Button(root,
                text='2',
                padx=35,
                pady=20,
                command=lambda:click(2),
                fg='#1C1C1C',
                activebackground='#000000',
                bg="#05eb8b",
                activeforeground="#09543e",
                relief=FLAT,
                font=("futura", 15,"italic")
)
numero2.grid(row=1,column=1)

numero3 = Button(root,
                text='3',
                padx=38,
                pady=20,
                command=lambda:click(3),
                fg='#1C1C1C',
                activebackground='#000000',
                bg="#05eb8b",
                activeforeground="#09543e",
                relief=FLAT,
                font=("futura", 15,"italic")
)
numero3.grid(row=1,column=2)

#Segunda fileira de numeros!!!!!!
numero4 = Button(root,
                text='4',
                padx=35,
                pady=20,
                command=lambda:click(5),
                fg='#1C1C1C',
                activebackground='#000000',
                bg="#05eb8b",
                activeforeground="#09543e",
                relief=FLAT,
                font=("futura", 15,"italic")
)
numero4.grid(row=2,column=0)

numero5 = Button(root,
                text='5',
                padx=35,
                pady=20,
                command=lambda:click(5),
                fg='#1C1C1C',
                activebackground='#000000',
                bg="#05eb8b",
                activeforeground="#09543e",
                relief=FLAT,
                font=("futura", 15,"italic")
)
numero5.grid(row=2,column=1)

numero6 = Button(root,
                text='6',
                padx=38,
                pady=20,
                command=lambda:click(6),
                fg='#1C1C1C',
                activebackground='#000000',
                bg="#05eb8b",
                activeforeground="#09543e",
                relief=FLAT,
                font=("futura", 15,"italic")
)
numero6.grid(row=2,column=2)

#Terceira fileira de numeros!!!!!!

numero7 = Button(root,
                text='7',
                padx=35,
                pady=20,
                command=lambda:click(7),
                fg='#1C1C1C',
                activebackground='#000000',
                bg="#05eb8b",
                activeforeground="#09543e",
                relief=FLAT,
                font=("futura", 15,"italic")
)
numero7.grid(row=3,column=0)

numero8 = Button(root,
                text='8',
                padx=35,
                pady=20,
                command=lambda:click(8),
                fg='#1C1C1C',
                activebackground='#000000',
                bg="#05eb8b",
                activeforeground="#09543e",
                relief=FLAT,
                font=("futura", 15,"italic")
)
numero8.grid(row=3,column=1)

numero9 = Button(root,
                text='9',
                padx=38,
                pady=20,
                command=lambda:click(9),
                fg='#1C1C1C',
                activebackground='#000000',
                bg="#05eb8b",
                activeforeground="#09543e",
                relief=FLAT,
                font=("futura", 15,"italic")
)
numero9.grid(row=3,column=2)

#ultima fileira

numero0 = Button(root,
                text='0',
                padx=83,
                pady=20,
                command=lambda:click(0),
                fg='#1C1C1C',
                activebackground='#000000',
                bg="#05eb8b",
                activeforeground="#09543e",
                relief=FLAT,
                font=("futura", 15,"italic")
)
numero0.grid(row=4,column=0,columnspan=2)

limpa = Button(root,
                text='C',
                padx=37,
                pady=20,
                command=tecla_limpa,
                fg='#1C1C1C',
                activebackground='#000000',
                bg="#DC2338",
                activeforeground="#09543e",
                relief=FLAT,
                font=("futura", 15,"italic")              
)
limpa.grid(row=4,column=2)




root.mainloop()