# Generated by Django 5.0.1 on 2024-01-24 21:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appBdd', '0005_alter_prospect_email_alter_prospect_function_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prospect',
            name='sector',
            field=models.CharField(max_length=250),
        ),
    ]