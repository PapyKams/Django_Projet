# Generated by Django 5.0.1 on 2024-01-24 23:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appBdd', '0014_alter_prospect_address_street_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prospect',
            name='direct_line',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
