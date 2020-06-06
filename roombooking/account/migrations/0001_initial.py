# Generated by Django 3.0.3 on 2020-03-14 18:43

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
            name='Available',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Advance_Booking_Days', models.IntegerField(null=True)),
                ('Time_For_available', models.TimeField(default=django.utils.timezone.now, null=True)),
                ('Time_up_to_available', models.TimeField(default=django.utils.timezone.now, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Category', models.CharField(choices=[('single', 'single'), ('double', 'double'), ('king', 'king'), ('queen', 'queen')], max_length=200)),
                ('description', models.CharField(max_length=200)),
                ('price', models.FloatField()),
                ('date', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('guestFirstName', models.CharField(max_length=255)),
                ('guestLastName', models.CharField(max_length=255)),
                ('CheckIn', models.DateField(default=django.utils.timezone.now, null=True)),
                ('CheckOut', models.DateField(default=django.utils.timezone.now, null=True)),
                ('status', models.CharField(default='UnBooked', max_length=10, null=True)),
                ('room', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='account.Room')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('email', models.CharField(max_length=200, null=True)),
                ('Phone', models.CharField(max_length=20, null=True)),
                ('date', models.DateTimeField(auto_now_add=True, null=True)),
                ('room', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='account.Room')),
            ],
        ),
    ]
