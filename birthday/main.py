import smtplib

mymail = "giltruman1906@gmail.com"
to_mail = "liaba99@gmail.com"
my_password = "ygqbucjncpnlfftw"
connection = smtplib.SMTP("smtp.gmail.com", 587)
connection.starttls()
connection.login(user=mymail, password=my_password)
connection.sendmail(from_addr=mymail, to_addrs=to_mail, msg="Subject: Test\n\nhello")
connection.close()