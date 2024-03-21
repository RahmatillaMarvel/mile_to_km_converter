from tkinter import *

window = Tk()
window.title('Mile to km converter')
window.geometry('500x200+500+350')


# input
miles_input = Entry(font=('Arial', 25),width=10)
miles_input.grid(column=1, row=0, padx=10, pady=10)

# label
miles_label = Label(text='Miles', font=('Arial', 24, 'bold'))
miles_label.grid(column=2, row=0, padx=10, pady=10)

is_equal_to = Label(text='is equal to', font=('Arial', 24, 'bold'))
is_equal_to.grid(column=0, row=1, padx=10, pady=10)

km_output = Label(text='0', font=('Arial', 24, 'bold'))
km_output.grid(column=1, row=1, padx=10, pady=10)

km_label = Label(text='Km',font=('Arial', 24, 'bold'))
km_label.grid(column=2, row=1, padx=10, pady=10)

def calculation():
    if miles_input.get() == '':
        return
    km_output.config(text=int(miles_input.get()) * 1.60934, font=('Arial', 24, 'bold'))


calculate = Button(text='Calculate', font=('Arial', 20, 'bold'), command=calculation)
calculate.grid(column=1, row=2, padx=10, pady=10)


window.mainloop()