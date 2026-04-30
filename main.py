import os
import smtplib
import datetime as dt
import pandas as pd
import random

# ----------------------------- EMAIL SETTINGS ----------------------------------------- #
MY_EMAIL = os.environ.get("MY_EMAIL")
MY_PASSWORD = os.environ.get("MY_PASSWORD")
today = dt.datetime.now()

# ----------------------------- IMPORT CSV --------------------------------------------- #

birthdays= pd.read_csv("birthdays.csv")
birthday_list = birthdays.to_dict(orient="records")
letters_list = []

# ------------------------------ LOGIC ------------------------------------------------- #

for _, row in birthdays.iterrows():
    if row["day"] == today.day and row["month"] == today.month:
        for i in range(1, 4):
            with open(f"letter_templates/letter_{i}.txt", "r") as letter_file:
                content = letter_file.read()
                formatted = content.replace("[NAME]", row["name"])
                letters_list.append(formatted)

        chosen_letter = random.choice(letters_list)

        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email, to_addrs=row["email"],
                                msg="Subject: Happy Birthday!\n\n"
                                    f"{chosen_letter}")
