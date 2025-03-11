from django.shortcuts import render
from .models import FemaleSinglePlayer, MaleSinglePlayer
import collections
import datetime
from django.core import serializers
from django.conf import settings


# Create your views here.
def home(request):
    return render(request, "BWFapp/home.html")


def womens_singles(request):
    female_players = FemaleSinglePlayer.objects.all()
    date = female_players[0].date.strftime("%d %B %Y")
    list_female_countries = sorted(
        list(set(FemaleSinglePlayer.objects.values_list("country", flat=True)))
    )

    list_female_players = list(female_players.values())
    for player in list_female_players:
        player["country_image"] = request.build_absolute_uri(
            settings.MEDIA_URL + player["country_image"]
        )

    return render(
        request,
        "BWFapp/singles.html",
        {
            "players": female_players,
            "players_list": list_female_players,
            "date": date,
            "countries": list_female_countries,
        },
    )


def mens_singles(request):
    male_players = MaleSinglePlayer.objects.all()
    date = male_players[0].date.strftime("%d %B %Y")
    list_male_countries = sorted(
        list(set(MaleSinglePlayer.objects.values_list("country", flat=True)))
    )

    list_male_players = list(male_players.values())
    for player in list_male_players:
        player["country_image"] = request.build_absolute_uri(
            settings.MEDIA_URL + player["country_image"]
        )

    return render(
        request,
        "BWFapp/singles.html",
        {
            "players": male_players,
            "players_list": list_male_players,
            "date": date,
            "countries": list_male_countries,
        },
    )


def singles_charts(request):
    female_countries = list(
        FemaleSinglePlayer.objects.values_list("country", flat=True)
    )
    female_countries_counter = dict(
        sorted(collections.Counter(female_countries).items(), key=lambda item: item[1])
    )
    male_countries = list(MaleSinglePlayer.objects.values_list("country", flat=True))
    male_countries_counter = dict(
        sorted(collections.Counter(male_countries).items(), key=lambda item: item[1])
    )
    list_countries = sorted(
        list(
            set(FemaleSinglePlayer.objects.values_list("country", flat=True)).union(
                set(MaleSinglePlayer.objects.values_list("country", flat=True))
            )
        )
    )
    female_players = FemaleSinglePlayer.objects.all()
    date = female_players[0].date.strftime("%d %B %Y")
    return render(
        request,
        "BWFapp/singles_charts.html",
        {
            "female_countries_counter": female_countries_counter,
            "male_countries_counter": male_countries_counter,
            "list_countries": list_countries,
            "date": date,
        },
    )
