from django.core.management.base import BaseCommand
from BWFapp.scraping import scrape_players
from django.core.management import call_command


class Command(BaseCommand):
    help = "Scrapes the website and updates the database"

    def handle(self, *args, **options):
        self.stdout.write("Starting web scraping...")
        URL_BWF = "https://www.tournamentsoftware.com/ranking/ranking.aspx?rid=70"
        call_command("flush", interactive=False)
        scrape_players(URL_BWF, male=True)
        scrape_players(URL_BWF, male=False)
        self.stdout.write("Scraping finished!")
