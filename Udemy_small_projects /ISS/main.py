import requests 
import smtplib
from datetime import datetime


def send_email(text):
    mymail = "giltruman1906@gmail.com"
    #to_mail = "liaba99@gmail.com"
    to_mail = "giltruman1906@gmail.com"
    my_password = "ygqbucjncpnlfftw"    
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


#----------------iss info ----------------------#

response_iss = requests.get(url= 'http://api.open-notify.org/iss-now.json' )
response_iss.raise_for_status()
iss_data = response_iss.json()["iss_position"]
iss_lat = float(iss_data["latitude"])
iss_lng = float(iss_data["longitude"])



list_iss = [iss_lat ,iss_lng ]


#----------------------my info ------------------#
current_time = datetime.now()
current_hour = current_time.hour

my_lat = 32.085300
my_lng = 34.781769
timestamp = 0
parameters = {
    "lat": my_lat,
    "lng":my_lng,
     "formatted" : timestamp

}

response = requests.get(url= 'https://api.sunrise-sunset.org/json' ,params = parameters)
response.raise_for_status()
data = response.json()
sunrise_hour = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset_hour = int(data["results"]["sunset"].split("T")[1].split(":")[0])

list = [sunrise_hour ,sunset_hour ]
# print (type(my_lat))
# print (type(my_lng))
# print (type(iss_lat))
# print (type(iss_lng))
# print (type(current_hour))
# print (type(sunrise_hour))
# print(type(sunset_hour))

#-----logic----#



def is_dark(current_hour ,sunrise_hour , sunset_hour ):
 if current_hour > sunrise_hour or current_hour < sunset_hour :
    return True

def is_close(my_lat,my_lng ,iss_lat, iss_lng):
 if ( my_lat -5 <= iss_lat and  my_lat+ 5 >= iss_lat) and ( my_lng - 5 <= iss_lng and  my_lng + 5 >= iss_lng):
    return True

if  is_dark(current_hour ,sunrise_hour , sunset_hour )  and is_close(my_lat,my_lng ,iss_lat, iss_lng) :
    try:
        with open("iss_email_format.txt" ,"r") as f:
            file = f.read()
        send_email(file)
    except Exception as e:
        print(f"error - the iss is not in your location rate in this moment - try again later as its in lng:{iss_lng} and lat:{iss_lat}")
    

# print (my_lat)
# print (my_lng)
# print (iss_lat)
# print (iss_lng)
# print (current_hour)
# print (sunrise_hour)
# print(sunset_hour)