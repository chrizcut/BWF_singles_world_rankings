from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time
import re
import requests
import datetime

import os
import django
from django.core.management import call_command


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "BWFsite.settings")
django.setup()

from BWFapp.models import FemaleSinglePlayer, MaleSinglePlayer


URL_males = (
    "https://www.tournamentsoftware.com/ranking/category.aspx?id=44877&category=472"
)
URL_females = (
    "https://www.tournamentsoftware.com/ranking/category.aspx?id=44877&category=473"
)

# options = webdriver.ChromeOptions()
# options.add_experimental_option("detach", True)
# driver = webdriver.Chrome(options=options)

call_command("flush", interactive=False)


def scrape_players(URL, male):
    driver = webdriver.Chrome()
    driver.get(URL)

    time.sleep(3)

    cookie_button = driver.find_element(
        By.XPATH, "/html/body/div/div/div/main/form/div[1]/button[1]"
    )
    cookie_button.click()

    time.sleep(3)

    consent_button = driver.find_element(
        By.XPATH, '//*[@id="bdBase"]/div/div[2]/div[2]/div[2]/div[2]/button[2]'
    )
    consent_button.click()

    time.sleep(3)

    select_element = driver.find_element(By.ID, "_pagesize")
    select = Select(select_element)
    select.select_by_value("100")

    rankings_date_tmp = list(
        map(
            int,
            driver.find_element(
                By.XPATH,
                '//*[@id="cphPage_cphPage_cphPage_dlPublication_chosen"]/a/span',
            ).text.split("/"),
        )
    )
    rankings_date = datetime.date(
        rankings_date_tmp[2], rankings_date_tmp[0], rankings_date_tmp[1]
    )
    list_players = driver.find_elements(By.XPATH, f'//*[@id="content"]/table/tbody/tr')[
        2:-1
    ]

    # if male == True:
    #     MaleSinglePlayer.objects.all().delete()
    # else:
    #     FemaleSinglePlayer.objects.all().delete()

    for p in list_players:
        list_data = p.find_elements(By.TAG_NAME, "td")
        rank = list_data[0].text
        first_name = " ".join(
            re.findall("[A-Z]{1}[a-z\.-]+[A-Za-z]*", list_data[4].text)
        )
        last_name = " ".join(re.findall("[A-Z]{2,}", list_data[4].text))

        img = list_data[4].find_element(By.TAG_NAME, "img")
        src = img.get_attribute("src")

        img_data = requests.get(src).content
        with open(f"media/country_images/{src[-7:-4]}.svg", "wb") as handler:
            handler.write(img_data)

        points = list_data[7].text
        nb_tournaments = list_data[8].text
        country = list_data[10].text

        if male == True:
            MaleSinglePlayer(
                first_name=first_name,
                last_name=last_name,
                rank=rank,
                date=rankings_date,
                country=country,
                country_image=f"media/country_images/{src[-7:-4]}.svg",
                nb_tournaments=nb_tournaments,
                points=points,
            ).save()
        else:
            FemaleSinglePlayer(
                first_name=first_name,
                last_name=last_name,
                rank=rank,
                date=rankings_date,
                country=country,
                nb_tournaments=nb_tournaments,
                country_image=f"media/country_images/{src[-7:-4]}.svg",
                points=points,
            ).save()
    driver.close()


scrape_players(URL_males, True)
scrape_players(URL_females, False)
