##################### Extra Hard Starting Project ######################
import smtplib
import datetime as dt 
import random 
import pandas as  pd 
import os 


mymail = "giltruman1906@gmail.com"
to_mail = "liaba99@gmail.com"
#to_mail = "giltruman1906@gmail.com"
my_password = "ygqbucjncpnlfftw"
def send_email(text):
    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=mymail, password=my_password)
            connection.sendmail(from_addr=mymail,
                                to_addrs=to_mail,
                                msg= f"Subject:Every day motivations\n This is the motivation sentence for the day:\n\n\n{text}"
            )
        print(f"email was delivered to {to_mail} from {mymail} ")
    except:
        print("error - fail to sent")

# Read CSV and ignore spaces right after commas
df = pd.read_csv("birthday project - Sheet1.csv", skipinitialspace=True)

# Strip any leading/trailing spaces (and normalize if you want)
df.columns = df.columns.str.strip()

now = dt.datetime.now()
today_date = dt.date.today()
records = df[["name", "birthday date"]].to_dict("records")

for r in records:
    if r["birthday date"] == today_date:
        new_name = r["name"]  
        file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
        with open(file_path , "r") as f:
            file = f.read()
        new_text = file.replace("[NAME]", new_name)
send_email(new_text)
# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.
