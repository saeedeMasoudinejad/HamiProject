# Generated by Django 2.2 on 2020-04-09 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_auto_20200409_1444'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='name',
            field=models.TextField(blank=True, null=True),
        ),
    ]