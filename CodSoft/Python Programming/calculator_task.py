from tkinter import *
import math

expression = ""

def press(num):
	global expression
	expression = expression + str(num)
	equation.set(expression)

def equalpress():
	try:
		global expression
		if "!" in expression:
			num = int(expression[:-1])
			result = math.factorial(num)
		else:
			result = str(eval(expression))

		equation.set(result)
		expression = str(result)
	except:
		equation.set("Error")
		expression = ""

def clear():
	global expression
	expression = ""
	equation.set("")

def sqrt_press():
	try:
		global expression
		result = math.sqrt(float(expression))
		equation.set(result)
		expression = str(result)
	except:
		equation.set("Error")
		expression = ""

def backspace():
	global expression
	expression = expression[:-1]
	equation.set(expression)

gui = Tk()
gui.title("Calculator")
gui.geometry("270x280")
gui.configure(bg="#2c3e50")

equation = StringVar()
expression_field = Entry(gui, textvariable=equation, font=("Arial", 14), bg="#34495e", fg="#ecf0f1", insertbackground="#ecf0f1")
expression_field.grid(row=0, column=0, columnspan=4, pady=10, padx=10, ipadx=60)

buttons = [
	["7", "8", "9", "+"],
	["4", "5", "6", "-"],
	["1", "2", "3", "*"],
	["0", ".", "/", "!"]
]

row = 1
for button_row in buttons:
	col = 0
	for button_text in button_row:
		if button_text in ["+", "-", "*", "/"]:
			button = Button(gui, text=button_text, font=("Arial", 12, "bold"), padx=12, pady=12, bd=0, bg="#e74c3c", fg="#ecf0f1",
							activebackground="#c0392b", activeforeground="#ecf0f1",
							command=lambda button_text=button_text: press(button_text))
		elif button_text == "!":
			button = Button(gui, text=button_text, font=("Arial", 12, "bold"), padx=12, pady=12, bd=0, bg="#e74c3c", fg="#ecf0f1",
							activebackground="#c0392b", activeforeground="#ecf0f1",
							command=lambda button_text=button_text: press(button_text))
		else:
			button = Button(gui, text=button_text, font=("Arial", 12, "bold"), padx=12, pady=12, bd=0, bg="#95a5a6", fg="#ecf0f1",
							activebackground="#7f8c8d", activeforeground="#ecf0f1",
							command=lambda button_text=button_text: press(button_text))
		button.grid(row=row, column=col, pady=5, padx=5)
		col += 1
	row += 1

sqrt_button = Button(gui, text="√", font=("Arial", 12, "bold"), padx=12, pady=12, bd=0, bg="#2ecc71", fg="#ecf0f1",
					activebackground="#27ae60", activeforeground="#ecf0f1",
					command=sqrt_press)
sqrt_button.grid(row=row, column=0, pady=5, padx=5)

backspace_button = Button(gui, text="<-", font=("Arial", 12, "bold"), padx=12, pady=12, bd=0, bg="#95a5a6", fg="#ecf0f1",
						  activebackground="#7f8c8d", activeforeground="#ecf0f1",
						  command=backspace)
backspace_button.grid(row=row, column=1, pady=5, padx=5)

clear_button = Button(gui, text="C", font=("Arial", 12, "bold"), padx=12, pady=12, bd=0, bg="#3498db", fg="#ecf0f1",
					  activebackground="#2980b9", activeforeground="#ecf0f1",
					  command=clear)
clear_button.grid(row=row, column=2, pady=5, padx=5)

equal_button = Button(gui, text="=", font=("Arial", 12, "bold"), padx=12, pady=12, bd=0, bg="#9b59b6", fg="#ecf0f1",
					 activebackground="#8e44ad", activeforeground="#ecf0f1",
					 command=equalpress)
equal_button.grid(row=row, column=3, pady=5, padx=5)

gui.mainloop()
