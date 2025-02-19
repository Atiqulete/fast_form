# Generated by Django 5.0.6 on 2024-07-07 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_contactinfos'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=300)),
                ('Email', models.EmailField(max_length=254)),
                ('Phone', models.CharField(max_length=400)),
                ('Message', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'Contact-Infos',
            },
        ),
        migrations.DeleteModel(
            name='ContactInfos',
        ),
    ]
