# Generated by Django 2.2.1 on 2021-03-10 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20210310_1402'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff',
            name='availability',
            field=models.ManyToManyField(blank=True, related_name='availability', to='users.Availability'),
        ),
    ]
