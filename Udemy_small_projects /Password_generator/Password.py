import tkinter as tk
import string
import random
from tkinter import messagebox
import  json
# ---------------------------- CONSTANTS ------------------------------- #
PERPEL = "#7231cc"
WHITE = "#f8f7f7"
RED = "#c7300e"
BLAKE = "#090909"
YELLOW = "#6b6203"
FONT_NAME = "Courier"

# ---------------------------- password generator  ------------------------------- # 



# Option 1: dictionary
password_chars = {
    "lowercase": list(string.ascii_lowercase),   # a-z
    "uppercase": list(string.ascii_uppercase),   # A-Z
    "digits": list(string.digits),               # 0-9
    "symbols": list(string.punctuation)          # !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
}

# Option 2: flat list (all characters combined)
all_chars = (
    string.ascii_lowercase +
    string.ascii_uppercase +
    string.digits +
    string.punctuation
)


def generate_password():
    for key , value in password_chars.items():
        if key == "lowercase":
            random_lower_list =  [ random.choice(value) for n in range (4)]
        elif key == "uppercase":
            random_upper_list =  [ random.choice(value) for n in range (4)]  
        elif key == "digits":
            random_digit_list =  [ random.choice(value) for n in range (3)]
        else:
            random_symbol_list =  [ random.choice(value) for n in range (3)]
    random_char_list = random_lower_list + random_upper_list + random_digit_list + random_symbol_list   
    random.shuffle(random_char_list)
    password = "".join(random_char_list)
    pass_entry.delete(0, tk.END)
    pass_entry.insert(0, password)
    

   
#--------------------------------search function ------------------------------- #
def search_password():
     try:
        with open ("data.json", "r") as data_file:
            #   Reading old data
            data = json.load(data_file) 
            web = website_entry.get()
            if web not in data:
                messagebox.showinfo("Error", f"No details for {web} exists.")
            else:
                email = data[web]["email"] 
                password = data[web]["password"]
                messagebox.showinfo("Details", f"Email: {email}\nPassword: {password}")
     except FileNotFoundError as e :
        messagebox.showinfo("Error", "please see that you are writing it right!.")


# ---------------------------- ADD Function  ------------------------------- # 


def add_password():
    data_website = website_entry.get()
    data_user = user_entry.get()
    pass_website = pass_entry.get()
    data_text = data_website + " | " + data_user + " | " + pass_website + "\n"
    new_data = { 
            data_website : {
                "email": data_user,
                "password": pass_website        
            }
        }
    try:
        with open ("data.json", "r") as data_file:
            # Reading old data
            data = json.load(data_file)
            # updarting old data with new data
            data.update(new_data)
    except FileNotFoundError as e :
        with open ("data.json", "w") as data_file:
            # Creating new file
            json.dump(new_data, data_file, indent=4)
            messagebox.showinfo("Success", "creating first line!")
    else:
        with open ("data.json", "w") as data_file:    
        #saving updated data
            json.dump(data, data_file, indent=4)
            messagebox.showinfo("Success", "Password saved successfully!")
    website_entry.delete(0, tk.END)
    user_entry.delete(0, tk.END)
    pass_entry.delete(0, tk.END)


# ---------------------------- validation function ------------------------------- # 


def validate_password(password: str) -> bool:
    # Count categories
    lowercase = sum(1 for c in password if c in string.ascii_lowercase)
    uppercase = sum(1 for c in password if c in string.ascii_uppercase)
    digits    = sum(1 for c in password if c in string.digits)
    symbols   = sum(1 for c in password if c in string.punctuation)

    # Debug (optional)
    if lowercase >= 4 and uppercase >= 4 and digits >= 3 and symbols >= 3:
        return True
    else:
        return False

def check_password():
    password = pass_entry.get()
    data_user = user_entry.get()
    pass_website = pass_entry.get()
    if validate_password(password) == True:
        messagebox.showinfo("Success", "✅ Password meets the criteria!")
        add_password()
    elif  len(password) == 0 or len(data_user) == 0 or len(pass_website) == 0:
        messagebox.showinfo("Error","❌ Password does not meet the criteria. Please try again.")
# ---------------------------- UI SETUP ------------------------------- #


window = tk.Tk()
window.title("Password")
window.config(padx=100, pady=50, bg=WHITE)



# canvas 

canvas = tk.Canvas(width=220, height=250, bg = WHITE ,   highlightthickness=0)
logo_img = tk.PhotoImage(file="logo.png")
canvas.create_image(110,125, image=logo_img)
canvas.grid(row=0, column=0,  padx=20, pady=20, columnspan=3)

# label 
website_lable = tk.Label( text = "Website:", fg = BLAKE , bg= WHITE  , font=(FONT_NAME, 20))
website_lable.grid(row=1, column=0)

user_lable = tk.Label( text = "User/Email:", fg = BLAKE , bg= WHITE , font=(FONT_NAME, 20))
user_lable.grid(row=2, column=0)

user_lable = tk.Label( text = "Password:", fg = BLAKE , bg= WHITE ,  font=(FONT_NAME, 20))
user_lable.grid(row=3, column=0)
# button 
Generate_Password = tk.Button(text="Generate Password" , command = generate_password,  width= 20, fg= RED,  font=(FONT_NAME, 20) )
Generate_Password.grid(row=3, column=2, padx= 10, pady = 10 , columnspan=2  ) 

add_button = tk.Button(text="Add" , command = check_password , width= 37, fg= RED,  font=(FONT_NAME, 20) )
add_button.grid(row=4, column=2 , padx= 10, pady = 10 , columnspan=2)    


search_button = tk.Button(text="Search" , command= search_password,   width= 10, fg= RED,  font=(FONT_NAME, 20) )
search_button.grid(row=1, column=2 , padx= 10, pady = 10 , columnspan=2)

#entry 
website_entry = tk.Entry(width=20 ,fg = BLAKE , bg= WHITE , font=(FONT_NAME, 15))
website_entry.grid(row=1, column=1)
data_website = website_entry.get()

user_entry = tk.Entry(width=20,fg = BLAKE , bg= WHITE , font=(FONT_NAME, 15))
user_entry.grid(row=2, column=1)
data_user = user_entry.get()

pass_entry = tk.Entry(width=20,  fg = BLAKE , bg= WHITE ,  font=(FONT_NAME, 15))
pass_entry.grid(row=3, column=1)
pass_website = pass_entry.get()

window.mainloop() 