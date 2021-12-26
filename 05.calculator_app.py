from tkinter import *


root = Tk()
# title serve para mudar o nome mostrado na janela do programa
root.title("Calculadora de adição")
root.geometry("222x255")
root.resizable(0,0)
root.configure(bg="#8A8686")

e = Entry(root, width=30, border=7, borderwidth=0)
# columnspan serve para que a caixa ocupe mais de uma coluna
# neste caso ela irá ocupar 5 (coluna 0, 1, 2, 3, 4)
e.grid(row=0, column=0, columnspan=4, padx=20, pady=10)


# Transformar os números em texto para que não sejam somados, mas sim concatenados
def button_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))

# Limpando os valores clicados
def clear():
    e.delete(0, END)

# Para passar uma variável de uma função para outra é
# preciso utilizar uma variável global
def _sum():
    first_number = e.get()
    global f_num
    global math
    math = "Addition"
    f_num = int(first_number)
    e.delete(0, END)

def _subtract():
    first_number = e.get()
    global f_num
    global math
    math = "Subtraction"
    f_num = int(first_number)
    e.delete(0, END)

def _multiplier():
    first_number = e.get()
    global f_num
    global math
    math = "Multiplication"
    f_num = int(first_number)
    e.delete(0, END)

def _divide():
    first_number = e.get()
    global f_num
    global math
    math = "Division"
    f_num = int(first_number)
    e.delete(0, END)


# Resultado do cálculo
def equal():
    second_number = e.get()
    e.delete(0, END)

    if math == "Addition":
        e.insert(0, f_num + int(second_number))
    
    if math == "Subtraction":
        e.insert(0, f_num - int(second_number))

    if math == "Multiplication":
        e.insert(0, f_num * int(second_number))

    if math == "Division":
        e.insert(0, f_num / float(second_number))

# Definindo as funções de sobreposição do mouse nos botões
def buttonHover1(event):
        button_1["bg"] = "#fff"
        button_1["fg"] = "#696969"

def buttonHoverLeave1(event):
        button_1["bg"] = "#696969"
        button_1["fg"] = "#fff"

def buttonHover2(event):
        button_2["bg"] = "#fff"
        button_2["fg"] = "#696969"

def buttonHoverLeave2(event):
        button_2["bg"] = "#696969"
        button_2["fg"] = "#fff"

def buttonHover3(event):
        button_3["bg"] = "#fff"
        button_3["fg"] = "#696969"

def buttonHoverLeave3(event):
        button_3["bg"] = "#696969"
        button_3["fg"] = "#fff"

def buttonHover4(event):
        button_4["bg"] = "#fff"
        button_4["fg"] = "#696969"

def buttonHoverLeave4(event):
        button_4["bg"] = "#696969"
        button_4["fg"] = "#fff"

def buttonHover5(event):
        button_5["bg"] = "#fff"
        button_5["fg"] = "#696969"

def buttonHoverLeave5(event):
        button_5["bg"] = "#696969"
        button_5["fg"] = "#fff"

def buttonHover6(event):
        button_6["bg"] = "#fff"
        button_6["fg"] = "#696969"

def buttonHoverLeave6(event):
        button_6["bg"] = "#696969"
        button_6["fg"] = "#fff"

def buttonHover7(event):
        button_7["bg"] = "#fff"
        button_7["fg"] = "#696969"

def buttonHoverLeave7(event):
        button_7["bg"] = "#696969"
        button_7["fg"] = "#fff"

def buttonHover8(event):
        button_8["bg"] = "#fff"
        button_8["fg"] = "#696969"

def buttonHoverLeave8(event):
        button_8["bg"] = "#696969"
        button_8["fg"] = "#fff"

def buttonHover9(event):
        button_9["bg"] = "#fff"
        button_9["fg"] = "#696969"

def buttonHoverLeave9(event):
        button_9["bg"] = "#696969"
        button_9["fg"] = "#fff"

def buttonHover0(event):
        button_0["bg"] = "#fff"
        button_0["fg"] = "#696969"

def buttonHoverLeave0(event):
        button_0["bg"] = "#696969"
        button_0["fg"] = "#fff"

def buttonHoveradd(event):
        button_add["bg"] = "#fff"
        button_add["fg"] = "#C0C0C0"

def buttonHoverLeaveadd(event):
        button_add["bg"] = "#C0C0C0"
        button_add["fg"] = "black"

def buttonHoversubtract(event):
        button_subtract["bg"] = "#fff"
        button_subtract["fg"] = "#C0C0C0"

def buttonHoverLeavesubtract(event):
        button_subtract["bg"] = "#C0C0C0"
        button_subtract["fg"] = "black"

def buttonHovermultiplier(event):
        button_multiplier["bg"] = "#fff"
        button_multiplier["fg"] = "#C0C0C0"

def buttonHoverLeavemultiplier(event):
        button_multiplier["bg"] = "#C0C0C0"
        button_multiplier["fg"] = "black"

def buttonHoverdivide(event):
        button_divide["bg"] = "#fff"
        button_divide["fg"] = "#C0C0C0"

def buttonHoverLeavedivide(event):
        button_divide["bg"] = "#C0C0C0"
        button_divide["fg"] = "black"

def buttonHoverequal(event):
        button_equal["bg"] = "#C0C0C0"
        button_equal["fg"] = "#fff"

def buttonHoverLeaveequal(event):
        button_equal["bg"] = "#fff"
        button_equal["fg"] = "#696969"

def buttonHoverclear(event):
        button_clear["bg"] = "#696969"
        button_clear["fg"] = "#fff"

def buttonHoverLeaveclear(event):
        button_clear["bg"] = "#fff"
        button_clear["fg"] = "#696969"

# Definindo os botões

# Para passar parametros com botões deve-se usar o 'lambda'

button_1 = Button(root, text="1", padx=20, pady=10, fg="#fff", bg="#696969", command=lambda: button_click(1))
button_2 = Button(root, text="2", padx=20, pady=10, fg="#fff", bg="#696969", command=lambda: button_click(2))
button_3 = Button(root, text="3", padx=20, pady=10, fg="#fff", bg="#696969", command=lambda: button_click(3))
button_4 = Button(root, text="4", padx=20, pady=10, fg="#fff", bg="#696969", command=lambda: button_click(4))
button_5 = Button(root, text="5", padx=20, pady=10, fg="#fff", bg="#696969", command=lambda: button_click(5))
button_6 = Button(root, text="6", padx=20, pady=10, fg="#fff", bg="#696969", command=lambda: button_click(6))
button_7 = Button(root, text="7", padx=20, pady=10, fg="#fff", bg="#696969", command=lambda: button_click(7))
button_8 = Button(root, text="8", padx=20, pady=10, fg="#fff", bg="#696969", command=lambda: button_click(8))
button_9 = Button(root, text="9", padx=20, pady=10, fg="#fff", bg="#696969", command=lambda: button_click(9))
button_0 = Button(root, text="0", padx=20, pady=10, fg="#fff", bg="#696969", command=lambda: button_click(0))

button_add = Button(root, text="+", padx=18.5, pady=10, bg="#C0C0C0", command=lambda: _sum())
button_subtract = Button(root, text="-", padx=20, pady=10, bg="#C0C0C0", command=lambda: _subtract())
button_multiplier = Button(root, text="*", padx=20, pady=10, bg="#C0C0C0", command=lambda: _multiplier())
button_divide = Button(root, text="/", padx=20, pady=10, bg="#C0C0C0", command=lambda: _divide())

button_equal = Button(root, text="=", padx=47, pady=10, command=lambda: equal())
button_clear = Button(root, text="Clear", padx=9, pady=10, command=lambda: clear())

# Colocando os botões na tela

button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=0)    

button_add.grid(row=1, column=3)
button_subtract.grid(row=2, column=3)
button_multiplier.grid(row=3, column=3)
button_divide.grid(row=4, column=3)

button_equal.grid(row=4, column=1, columnspan=2)
button_clear.grid(row=5, column=3)

# incluindo efeito de mouse sobre o botão
button_1.bind("<Enter>", buttonHover1)
button_1.bind("<Leave>", buttonHoverLeave1)

button_2.bind("<Enter>", buttonHover2)
button_2.bind("<Leave>", buttonHoverLeave2)

button_3.bind("<Enter>", buttonHover3)
button_3.bind("<Leave>", buttonHoverLeave3)

button_4.bind("<Enter>", buttonHover4)
button_4.bind("<Leave>", buttonHoverLeave4)

button_5.bind("<Enter>", buttonHover5)
button_5.bind("<Leave>", buttonHoverLeave5)

button_6.bind("<Enter>", buttonHover6)
button_6.bind("<Leave>", buttonHoverLeave6)

button_7.bind("<Enter>", buttonHover7)
button_7.bind("<Leave>", buttonHoverLeave7)

button_8.bind("<Enter>", buttonHover8)
button_8.bind("<Leave>", buttonHoverLeave8)

button_9.bind("<Enter>", buttonHover9)
button_9.bind("<Leave>", buttonHoverLeave9)

button_0.bind("<Enter>", buttonHover0)
button_0.bind("<Leave>", buttonHoverLeave0)

button_add.bind("<Enter>", buttonHoveradd)
button_add.bind("<Leave>", buttonHoverLeaveadd)

button_subtract.bind("<Leave>", buttonHoverLeavesubtract)
button_subtract.bind("<Enter>", buttonHoversubtract)

button_multiplier.bind("<Enter>", buttonHovermultiplier)
button_multiplier.bind("<Leave>", buttonHoverLeavemultiplier)

button_divide.bind("<Enter>", buttonHoverdivide)
button_divide.bind("<Leave>", buttonHoverLeavedivide)

button_equal.bind("<Enter>", buttonHoverequal)
button_equal.bind("<Leave>", buttonHoverLeaveequal)

button_clear.bind("<Enter>", buttonHoverclear)
button_clear.bind("<Leave>", buttonHoverLeaveclear)

root.mainloop()
