import csv
from appBdd.models import prospect
from django.core.management.base import BaseCommand

def to_decimal(value):
    try:
        return float(value.replace(',', '.').strip()) if value else None
    except ValueError:
        return None

class Command(BaseCommand):
    help = "Load a list of prospects from a CSV file into the database"

    def add_arguments(self, parser):
        parser.add_argument('csv_file_path', type=str, help="Le chemin absolu vers le fichier CSV.")

    def handle(self, *args, **options):
        prospects = []

        with open(options['csv_file_path'], newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                prospect = prospect(
                    campaign=row['Campagne'],
                    company_name=row['Company name'],
                    civility=row['Civilité'],
                    first_name=row['Prénom'],
                    last_name=row['Nom de famille'],
                    function=row['Fonction'],
                    email=row['Email'],
                    linkedin_url=row['URL LinkedIn'],
                    phone=row['Téléphone'],
                    direct_line=row['Ligne directe/Mobile'],
                    website=row['Site web'],
                    siret=row['Siret'],
                    address_street=row['Adresse - Rue'],
                    address_zip=row['Adresse - CP'],
                    address_city=row['Adresse - Ville'],
                    department=row['Département'],
                    sector=row['Secteur d activité'],
                    workforce=row['Effectif'] if row['Effectif'] else 0,
                    revenue=to_decimal(row['CA']),
                    naf_code=row['Code NAF']
                )
                prospects.append(prospect)

        prospect.objects.bulk_create(prospects)
        self.stdout.write(self.style.SUCCESS(f"{len(prospects)} prospects importés avec succès."))
