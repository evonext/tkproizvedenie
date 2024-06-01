from tkinter import *
from tkinter import ttk
root=Tk() # Корневое окно
root.title("First question")
root.geometry('400x250')

def calculate():

    number = int(entry.get())
    total = 1

    if selected_loop.get() == "for":
        for digit in str(abs(number)):
            digit = int(digit)
            if digit != 0:
                total *= digit
    elif selected_loop.get() == "while":
        while number != 0:
            digit = number % 10
            if digit !=0:
                total *= digit
            number //= 10
    entry_result.config(state='normal')
    entry_result.delete(0, END)
    entry_result.insert(0,str(total))
    entry_result.config(state='disable')

def clear():
    entry_result.config(state='normal')
    entry_result.delete(0, END)
    entry_result.config(text="")

#Инициализация виджетов
label_combo = Label(root, text="Выберите цикл") # Надпись над Combobox

selected_loop = StringVar() #Хранит переменную  типа String
combobox = ttk.Combobox(root, textvariable=selected_loop, values= ['for', 'while'] ) #Combobox

label_entry = Label(root, text="Введите целое число")
entry=Entry(root, width=20)
entry_result=Entry(root, width=20)
label_result=Label(root, text="Сумма цифр данного числа:")
execute_Button= Button(root, text="Выполнить", command=calculate)
clear_Button= Button(root, text="Очистить", command=clear)


#Размещение объектов на форме
label_combo.pack(anchor=NW, padx=10)
combobox.pack(anchor=NW, padx=10)
label_entry.pack(anchor = NW, padx=10, pady=(10,0))
entry.pack(anchor=NW, padx=10)
label_result.pack(anchor=NW, padx=10, pady=(10,0))
entry_result.pack(anchor=NW,padx=10)
execute_Button.pack(anchor=NW, padx=(50,10),pady=(30,0),side=LEFT)
clear_Button.pack(anchor=NW, padx=(50,10),pady=(30,0),side=LEFT)
root.mainloop()
