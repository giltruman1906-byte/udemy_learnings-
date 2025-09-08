##################### Extra Hard Starting Project ######################
import pandas as pd 
import datetime as dt

now = dt.datetime.now()
data =  pd.read_csv("birthday project - Sheet1.csv")
df = pd.DataFrame(data)
print(df["birthday date"])


# with open("birthday project - Sheet1.csv" ,"r") as f:
#     text = f.read()
# for name in text ["name"]:
#     print(name)


# 1. Update the birthdays.csv



# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.




