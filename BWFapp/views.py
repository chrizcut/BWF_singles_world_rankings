from django.shortcuts import render
from .models import FemaleSinglePlayer, MaleSinglePlayer
import collections


# Create your views here.
def home(request):
    return render(request, "BWFapp/home.html")


def womens_singles(request):
    female_players = FemaleSinglePlayer.objects.all()
    return render(request, "BWFapp/singles.html", {"players": female_players})


def mens_singles(request):
    male_players = MaleSinglePlayer.objects.all()
    return render(request, "BWFapp/singles.html", {"players": male_players})


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
    return render(
        request,
        "BWFapp/singles_charts.html",
        {
            "female_countries_counter": female_countries_counter,
            "male_countries_counter": male_countries_counter,
            "list_countries": list_countries,
        },
    )
