# Generated by Django 3.2.19 on 2023-08-24 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='management',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group', models.IntegerField()),
                ('name', models.CharField(max_length=50)),
                ('capacity', models.IntegerField()),
            ],
        ),
    ]