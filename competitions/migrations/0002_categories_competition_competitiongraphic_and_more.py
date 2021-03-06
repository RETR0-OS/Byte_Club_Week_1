# Generated by Django 4.0.6 on 2022-07-08 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('competitions', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CategoryName', models.CharField(max_length=200)),
                ('category_code', models.CharField(max_length=4, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='competition',
            name='CompetitionGraphic',
            field=models.ImageField(blank=True, null=True, upload_to='competitions/graphics/'),
        ),
        migrations.AddField(
            model_name='competition',
            name='CompetitionCategory',
            field=models.ManyToManyField(blank=True, related_name='competition', to='competitions.categories'),
        ),
    ]
