import pandas
import datetime as dt
import random
import smtplib

MY_EMAIL = "sumitpy5@gmail.com"
MY_PASSWORD = "mixahknftwqmgnqv"


FILE_PATH = f"letter_templates/letter_{random.randint(1,3)}.txt"
##################### Hard Starting Project ######################

# 1. Update the birthdays.csv with your friends & family's details. 
# HINT: Make sure one of the entries matches today's date for testing purposes. 

# 2. Check if today matches a birthday in the birthdays.csv

pd = pandas.read_csv("birthdays.csv")

# HINT 1: Only the month and day matter. 
# HINT 2: You could create a dictionary from birthdays.csv that looks like this:
birthdays_dict = {(row["month"], row["day"]): row for _, row in pd.iterrows()}

#     (month, day): data_row
# }
#HINT 3: Then you could compare and see if today's month/day matches one of the keys in birthday_dict like this:
now = dt.datetime.now()
today_tuple = (now.month,now.day)



# if (today_month, today_day) in birthdays_dict:
if today_tuple in birthdays_dict:
    birthday_name = birthdays_dict[today_tuple]
    with open(FILE_PATH) as letters:
        message = letters.read()
        new_message = message.replace("[NAME]",birthday_name["name"])
        print(new_message)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL,password=MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,to_addrs="antishoot7@gmail.com",msg=f"Subject: Happy Birthday\n\n {new_message}")
        
        
        
        
        
        

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
# HINT: https://www.w3schools.com/python/ref_string_replace.asp

# 4. Send the letter generated in step 3 to that person's email address.
# HINT: Gmail(smtp.gmail.com), Yahoo(smtp.mail.yahoo.com), Hotmail(smtp.live.com), Outlook(smtp-mail.outlook.com)



