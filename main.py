from cgitb import text
from tkinter import *

window = Tk()
window.title("miles to km converter")
window.config(padx=20,pady=20)

def button_click():
    km_result =float(miles_input.get())*1.6
    km_result_label.config(text = f"{km_result}")

miles_input = Entry(text =0,width=7)
miles_input.grid(column=1 , row=0)


miles_label = Label(text = "Miles")
miles_label.grid(column = 2 , row = 0)


is_equal_label = Label(text = "is equal to ")
is_equal_label.grid(column= 0,row = 1)


km_result_label = Label(text =0)
km_result_label.grid(column=1,row=1)

kilometer_label = Label(text ="Km")
kilometer_label.grid(column=2,row =1)



calculate_button = Button(text = "Calculate",command=button_click)
calculate_button.grid(column=1,row=2)








window.mainloop()



