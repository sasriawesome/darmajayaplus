# Generated by Django 3.0.5 on 2020-04-06 23:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=256, verbose_name='Full name')),
                ('nickname', models.CharField(blank=True, max_length=256, null=True, verbose_name='Nick name')),
                ('gender', models.CharField(choices=[('M', 'MALE'), ('F', 'FEMALE')], default='M', max_length=1, verbose_name='Gender')),
                ('religion', models.CharField(blank=True, max_length=255, null=True, verbose_name='Religion')),
                ('nation', models.CharField(blank=True, max_length=255, null=True, verbose_name='Nation')),
                ('date_of_birth', models.DateField(blank=True, default=django.utils.timezone.now, null=True, verbose_name='Date of birth')),
                ('place_of_birth', models.CharField(blank=True, max_length=255, null=True, verbose_name='Place of birth')),
                ('account', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='person', to=settings.AUTH_USER_MODEL, verbose_name='User account')),
            ],
            options={
                'verbose_name': 'Person',
                'verbose_name_plural': 'Persons',
            },
        ),
    ]