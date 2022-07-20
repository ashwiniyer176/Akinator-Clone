import pandas as pd
from django.db import models

# Create your models here.
class Character(models.Model):
    name = models.CharField(max_length=100)
    id_status = models.CharField(max_length=100)
    align = models.CharField(max_length=100)
    eye = models.CharField(max_length=100)
    hair = models.CharField(max_length=100)
    sex = models.CharField(max_length=100)
    gsm = models.CharField(max_length=100)
    alive = models.BooleanField(default=True)
    appearances = models.IntegerField()
    first_appearance = models.TextField()
    year = models.IntegerField()
    company = models.CharField(max_length=10)


def populate_from_csv(csv_path):
    characters = []
    df = pd.read_csv(csv_path)
    for idx, data in df.iterrows():
        alive = False
        if data["ALIVE"][0] == "L":
            alive = True
        characters.append(
            Character(
                name=data["name"],
                id_status=data["ID"],
                align=data["ALIGN"],
                eye=data["EYE"],
                hair=data["HAIR"],
                sex=data["SEX"],
                gsm=data["GSM"],
                alive=alive,
                appearances=data["APPEARANCES"],
                first_appearance=data["FIRST APPEARANCE"],
                year=int(df["YEAR"]),
                company=df["Company"],
            )
        )
