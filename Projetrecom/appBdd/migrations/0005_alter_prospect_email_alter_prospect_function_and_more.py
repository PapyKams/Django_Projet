# Generated by Django 5.0.1 on 2024-01-24 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appBdd', '0004_alter_prospect_table'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prospect',
            name='email',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='prospect',
            name='function',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='prospect',
            name='sector',
            field=models.CharField(max_length=200),
        ),
    ]
