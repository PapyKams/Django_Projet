# Generated by Django 5.0.1 on 2024-01-24 22:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appBdd', '0008_alter_prospect_revenue'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prospect',
            name='revenue',
            field=models.CharField(default='N/A', max_length=255),
        ),
    ]
