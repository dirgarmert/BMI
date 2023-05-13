import tkinter
from tkinter import *
from tkinter.ttk import *
window = tkinter.Tk()
window.title("BMI")
p1=PhotoImage(file="png-transparent-dumbbell-computer-icons-weight-training-dumbbell-angle-physical-fitness-text-thumbnail.png")
window.iconphoto(False,p1)
window.config(padx=40, pady=40)


def clicked_button():
    user_input = my_entry_weight.get()
    user_input_2 = my_entry_height.get()
    if user_input_2 == "" or user_input == "":
        result_label.config(text="Tüm verileri giriniz!")
    else:
        try:
            x = float(user_input)
            y = float(user_input_2) * float(user_input_2)
            your_BMI = x / y * 10000
            result_string = your_status(your_BMI)
            result_label.config(text = result_string)
        except:
            result_label.config(text="Sayı giriniz!")


my_label = tkinter.Label(text="BMI Calculator", font=("Ariel", 15, "normal"))
my_label.grid(row=1, column=2)
my_label_2 = tkinter.Label(text="Enter your Weight (kg)", font=("Ariel", 10, "bold"))
my_label_2.grid(row=2, column=2)
my_entry_weight = tkinter.Entry()
my_entry_weight.grid(row=3, column=2)
my_label_3 = tkinter.Label(text="Enter your Height (cm)", font=("Ariel", 10, "bold"))
my_label_3.grid(row=5, column=2)
my_entry_height = tkinter.Entry()
my_entry_height.grid(row=6, column=2)
my_button = tkinter.Button(width=10, height=3, text="Enter", font=("Ariel", 8, "bold"), command=clicked_button)
my_button.grid(row=8, column=2)
result_label = tkinter.Label()
result_label.grid(row=9, column=2)


def your_status(your_BMI):
    status_string = f"Your BMI is {round(your_BMI, 2)}.You are "
    if your_BMI <= 16:
        status_string += "severly thin"
    elif 16 < your_BMI <= 17:
        status_string += "modernate thin"
    elif 17 < your_BMI <= 18.5:
        status_string += "mild thin"
    elif 18.5 < your_BMI <= 25:
        status_string += "normal"
    elif 25 < your_BMI <= 30:
        status_string += "overweight"
    elif 30 < your_BMI <= 35:
        status_string += "Obese Class I"
    elif 35 < your_BMI <= 40:
        status_string += "Obese Class II"
    elif your_BMI > 40:
        status_string += "Obese Class III"
    return status_string



window.mainloop()
