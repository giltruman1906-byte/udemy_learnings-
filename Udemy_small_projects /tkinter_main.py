import tkinter as tk


window = tk.Tk()
minimum_size = (500, 500)

lable = tk.Label(window , text="hello world", font=("Helvetica", 16, "bold"))
lable.grid(row=0, column=0, padx=20, pady=20)




def button_clicked ():
    print("i got clicked")
    new_text = input.get()
    lable.config(text=new_text)
    # lable.config(text="i got clicked")


    
button_1 = tk.Button(window, text="click me", command=button_clicked, bg="blue", fg="white")
button_1.grid(row=2, column=2, padx=30, pady=30)    


# entry 
input  = tk.Entry(width=30)
input.grid(row=1, column=1, padx=40, pady=40)
print(input.get())


window.mainloop()
