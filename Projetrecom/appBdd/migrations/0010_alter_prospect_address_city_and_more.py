# Generated by Django 5.0.1 on 2024-01-24 22:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appBdd', '0009_alter_prospect_revenue'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prospect',
            name='address_city',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='prospect',
            name='direct_line',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='prospect',
            name='email',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='prospect',
            name='naf_code',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='prospect',
            name='phone',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='prospect',
            name='revenue',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='prospect',
            name='siret',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='prospect',
            name='workforce',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
    ]
