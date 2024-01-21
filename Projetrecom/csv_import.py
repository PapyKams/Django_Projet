import csv
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Projetrecom.settings")
django.setup()

from appBdd.models import Prospect

def import_csv_to_prospect(file_path):
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            Prospect.objects.create(
                campaign=row['campaign'],
                company_name=row['company_name'],
                civility=row['civility'],
                first_name=row['first_name'],
                last_name=row['last_name'],
                function=row['function'],
                email=row['email'],
                linkedin_url=row['linkedin_url'] if row['linkedin_url'] else None,
                phone=row['phone'] if row['phone'] else None,
                direct_line=row['direct_line'] if row['direct_line'] else None,
                website=row['website'] if row['website'] else None,
                siret=row['siret'] if row['siret'] else None,
                address_street=row['address_street'],
                address_zip=row['address_zip'],
                address_city=row['address_city'],
                department=row['department'],
                sector=row['sector'],
                workforce=int(row['workforce']) if row['workforce'] else None,
                revenue=float(row['revenue']) if row['revenue'] else None,
                naf_code=row['naf_code'] if row['naf_code'] else None,
            )

if __name__ == "__main__":
    csv_files = [
        'csv_files/SIGILIUM.csv',
        # etc.
    ]
    for file_path in csv_files:
        import_csv_to_prospect(file_path)
