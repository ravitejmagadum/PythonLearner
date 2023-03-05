##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

import pandas as pd
import smtplib
import random
import datetime as dt
import os

bday_dates = pd.read_csv("birthdays.csv")
now = dt.datetime.now()
date = now.strftime('%d')
month = now.strftime('%m')

def check_bday():


    try:
        index_day = bday_dates[bday_dates['day'] == int(date)].index[0]
        index_month = bday_dates[bday_dates['month'] == int(month)].index[0]


        if index_day == index_month:
            bday_person = bday_dates.loc[index_day, "name"]
            bday_email = bday_dates.loc[index_day, "email"]

            def prepare_letter():
                dir_path = "letter_templates"
                letters_paths = [f for f in os.listdir(dir_path) if f.endswith('.txt')]
                letter = random.choice(letters_paths)
                with open(f"letter_templates/{letter}", "r") as l:
                    content = l.read()
                    newname = content.replace("[NAME]", bday_person)
                return newname

            def send_wish():
                email = "magadumravitej38@gmail.com"
                password = "pxywicsvuuyirear"  # password is generated for this program which is different from google password

                connection = smtplib.SMTP("smtp.gmail.com", 587)
                connection.starttls()
                connection.login(user=email, password=password)
                connection.sendmail(from_addr=email,
                                    to_addrs="ravitejmagadum1999@gmail.com",
                                    msg=f"Subject: Happy Birthday {bday_person}\n\n{prepare_letter()}")
                connection.quit()

            prepare_letter()
            send_wish()
    except IndexError:
        print("Today is no one's birthday")

check_bday()


