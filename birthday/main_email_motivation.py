import smtplib
import datetime as dt 
import random 


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

dict_of_week = [
            {"Name" :"Sunday",   "enum":0},
            {"Name" :"Monday",   "enum":1},
            {"Name" :"Thursday", "enum":2},
            {"Name" :"Wednesday","enum":3},
            {"Name" :"Tuesday", "enum":4},
            {"Name" :"Friday",   "enum":5},
            {"Name" :"Saturday", "enum":6}
            ]                   


days = [d["Name"] for d in dict_of_week]
with open("quotes.txt", "r") as f:
    text = f.read()
lines = [line for line in text.split("\n") ]




d_s = []
for i , line in  enumerate(lines):
    day = days[i % len(days)]
    d_s.append({"day": day , "sentence":line })



now = dt.datetime.now()
year = now.year
today_day_name = now.strftime("%A")
weekdays = now.weekday()+1


todays_list = [today_s["sentence"]  for today_s in d_s if today_day_name == today_s["day"] ] 
shuffled_copy = random.sample(todays_list, len(todays_list))
todays_sentance  = shuffled_copy[0]

send_email(todays_sentance)

