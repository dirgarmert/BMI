import tkinter

window = tkinter.Tk()
window.title("BMI")
window.minsize(width=400, height=400)

def clicked_button():
    user_input = my_entry_weight.get()
    user_input_2 = my_entry_height.get()
    x = int(user_input)
    y = int(user_input_2) * int(user_input_2)
    your_BMI = x / y * 10000
    print("your_BMI is", your_BMI)
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

window.mainloop()