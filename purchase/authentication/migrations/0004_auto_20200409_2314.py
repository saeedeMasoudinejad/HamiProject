# Generated by Django 2.2 on 2020-04-09 18:44

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('authentication', '0003_profile_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(blank=True, max_length=10, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+219999999' or '0219999999' . Up to 10 digits allowed.", regex='^(0|\\+)\\d{8,10}$')])),
                ('address', models.TextField()),
                ('date_time', models.DateField()),
                ('purchase', models.CharField(max_length=150)),
                ('name', models.CharField(max_length=150)),
                ('email', models.EmailField(max_length=254)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]
