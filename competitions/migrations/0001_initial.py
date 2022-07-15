# Generated by Django 4.0.6 on 2022-07-08 16:27

from django.conf import settings
from django.db import migrations, models
import django_quill.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Competition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CompetitionTitle', models.CharField(max_length=200)),
                ('RegistrationStartDate', models.DateField()),
                ('RegistrationEndDate', models.DateField()),
                ('CompetitionDetails', django_quill.fields.QuillField()),
                ('RegisteredUsers', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]