# Generated by Django 4.0.6 on 2022-07-12 15:32

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('competitions', '0005_remove_competition_competition_category_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='competition',
            name='Competition_Title',
            field=models.CharField(max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='competition',
            name='Registered_Users',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL),
        ),
    ]
