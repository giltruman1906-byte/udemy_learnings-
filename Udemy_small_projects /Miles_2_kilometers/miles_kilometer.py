# import tkinter as tk


# #start 
# window = tk.Tk()
# window.title("Miles to Kilometer Converter")
# window.config(padx=20, pady=20)


# def button_clicked():
#     try:
#         miles = float(input.get())
#         kilometer = round(miles * 1.609, 2)
#         text_2.config(text=kilometer)
#     except ValueError:
#         text_2.config(text="Invalid input")


# #input 
# input = tk.Entry(width=7 )
# input.grid(row=0, column=1)  #bottom right
# data = input.get()


# #lable 
# text = tk.Label( text = "Miles" , font=("Arial", 24 ))
# text.grid(row=0, column=2 )   # next to input

# text_1 = tk.Label( text = "Is Equal to" , font=("Arial", 24 ))
# text_1.grid(row= 1, column=0 )

# text_2 = tk.Label( text = "0" , font=("Arial", 20 ))
# text_1.grid(row=1, column=1 )

# text_3 = tk.Label( text = "Km" , font=("Arial", 24 ))
# text_3.grid(row=1, column=2 )
# # button 
# button  = tk.Button(text= "calculate", command=button_clicked)
# button.grid(row =2, column= 3  )





# window.mainloop()


count = 270
hours  = count // 60
minutes = count % 60
print(f"{hours}:{minutes}") 