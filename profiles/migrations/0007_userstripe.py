# Generated by Django 3.0.4 on 2020-03-11 21:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0006_auto_20200309_1703'),
    ]

    operations = [
        migrations.CreateModel(
            name='userStripe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stripe_id', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
    ]
