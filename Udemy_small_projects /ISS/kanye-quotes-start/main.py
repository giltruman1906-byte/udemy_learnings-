from tkinter import *
import requests 

def get_quote():
    try:
        resp = requests.get("https://api.kanye.rest", timeout=10)
        resp.raise_for_status()
        quote = resp.json().get("quote", "No quote found.")
        canvas.itemconfig(quote_text, text=quote)   # pass the item id!
    except Exception as e:
        canvas.itemconfig(quote_text, text=f"Error: {e}")




window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file="background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text="press the face", width=250, font=("Arial", 30, "bold"), fill="white")
canvas.grid(row=0, column=0)

kanye_img = PhotoImage(file="kanye.png")
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)



window.mainloop()