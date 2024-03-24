from tkinter import *
from tkinter import font

def button_press(num):
    global equation_text

    equation_text = equation_text + str(num)

    equation_label.set(equation_text)

def equals():
    global equation_text 
    try:
        total = str(eval(equation_text))
        equation_label.set(total)
        equation_text = total
        history.append(f"{total}")
    except ZeroDivisionError:
        equation_label.set("Arithmetic Error")
        equation_text = ""
    except SyntaxError:
        equation_label.set("Syntax Error")
        equation_text = ""

def clear():
    global equation_text

    equation_label.set("")

    equation_text = ""

def show_history():  # Ubah nama fungsi menjadi show_history()
    history_window = Tk()
    history_window.title("Calculation History")
    history_window.geometry("300x300")

    history_label = Label(history_window, text="Calculation History", font=('consolas', 14), pady=10)
    history_label.pack()

    history_text = Text(history_window, font=('consolas', 12), height=15, width=40)
    history_text.pack()

    # Menampilkan setiap item di riwayat
    for item in history:
        history_text.insert(END, item + "\n")

    history_text.config(state=DISABLED)

    history_window.mainloop()

window = Tk()
window.title("Calculator Program")
window.geometry("500x500")

equation_text = ""

equation_label = StringVar()

label = Label(window, textvariable=equation_label, font=('consolas', 20), fg="white", bg="black", width=24, height=2)  # Mengatur teks menjadi putih dan latar belakang menjadi hitam
label.pack()

frame = Frame(window, bg="black")  # Mengatur latar belakang frame menjadi hitam
frame.pack()

button1 = Button(frame, text=1, height=4, width=9, font=35, 
                 command=lambda: button_press(1))
button1.grid(row=0,column=0)

button2 = Button(frame, text=2, height=4, width=9, font=35, 
                 command=lambda: button_press(2))
button2.grid(row=0,column=1)

button3 = Button(frame, text=3, height=4, width=9, font=35, 
                 command=lambda: button_press(3))
button3.grid(row=0,column=2)

button4 = Button(frame, text=4, height=4, width=9, font=35, 
                 command=lambda: button_press(4))
button4.grid(row=1,column=0)

button5 = Button(frame, text=5, height=4, width=9, font=35, 
                 command=lambda: button_press(5))
button5.grid(row=1,column=1)

button6 = Button(frame, text=6, height=4, width=9, font=35, 
                 command=lambda: button_press(6))
button6.grid(row=1,column=2)

button7 = Button(frame, text=7, height=4, width=9, font=35, 
                 command=lambda: button_press(7))
button7.grid(row=2,column=0)

button8 = Button(frame, text=8, height=4, width=9, font=35, 
                 command=lambda: button_press(8))
button8.grid(row=2,column=1)

button9 = Button(frame, text=9, height=4, width=9, font=35, 
                 command=lambda: button_press(9))
button9.grid(row=2,column=2)

button0 = Button(frame, text=0, height=4, width=9, font=35, 
                 command=lambda: button_press(0))
button0.grid(row=3,column=0)

plus = Button(frame, text='+', height=4, width=9, font=35, 
                 command=lambda: button_press('+'))
plus.grid(row=0,column=3)

min = Button(frame, text='-', height=4, width=9, font=35, 
                 command=lambda: button_press('-'))
min.grid(row=1,column=3)

multiply = Button(frame, text='*', height=4, width=9, font=35, 
                 command=lambda: button_press('*'))
multiply.grid(row=2,column=3)

divide = Button(frame, text='/', height=4, width=9, font=35, 
                 command=lambda: button_press('/'))
divide.grid(row=3,column=3)

equal = Button(frame, text='=', height=4, width=9, font=35, 
                 command=equals)
equal.grid(row=3,column=2)

decimal = Button(frame, text='.', height=4, width=9, font=35, 
                 command=lambda: button_press('.'))
decimal.grid(row=3,column=1)

clear = Button(window, text='clear', height=4, width=13, font=35, 
                 command=clear)

history_button = Button(window, text='History', height=4, width=9, font=35, command=show_history)
history_button.pack(side=RIGHT)


clear.pack(side=LEFT)

history = [] 

window.mainloop()