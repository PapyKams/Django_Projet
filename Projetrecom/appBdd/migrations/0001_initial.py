# Generated by Django 5.0.1 on 2024-01-20 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Prospect',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=255)),
                ('civility', models.CharField(max_length=50)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('function', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('linkedin_url', models.URLField(blank=True, null=True)),
                ('phone', models.CharField(blank=True, max_length=50, null=True)),
                ('direct_line', models.CharField(blank=True, max_length=50, null=True)),
                ('website', models.URLField(blank=True, null=True)),
                ('siret', models.CharField(blank=True, max_length=14, null=True)),
                ('address_street', models.CharField(max_length=255)),
                ('address_zip', models.CharField(max_length=10)),
                ('address_city', models.CharField(max_length=100)),
                ('department', models.CharField(max_length=100)),
                ('campaign', models.CharField(max_length=100)),
                ('sector', models.CharField(max_length=100)),
                ('workforce', models.IntegerField(blank=True, null=True)),
                ('revenue', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True)),
                ('naf_code', models.CharField(blank=True, max_length=10, null=True)),
            ],
        ),
    ]
