from BWFapp.models import FemaleSinglePlayer, MaleSinglePlayer
from rest_framework import serializers


class FemaleSinglePlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = FemaleSinglePlayer
        fields = (
            "rank",
            "date",
            "first_name",
            "last_name",
            "country",
            "points",
            "nb_tournaments",
        )


class MaleSinglePlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = MaleSinglePlayer
        fields = (
            "rank",
            "date",
            "first_name",
            "last_name",
            "country",
            "points",
            "nb_tournaments",
        )
