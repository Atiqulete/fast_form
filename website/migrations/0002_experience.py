# Generated by Django 5.0.6 on 2024-07-04 04:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('p_year', models.CharField(max_length=300)),
                ('sc', models.CharField(max_length=300)),
                ('address', models.CharField(max_length=400)),
                ('det', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'Experience',
            },
        ),
    ]
