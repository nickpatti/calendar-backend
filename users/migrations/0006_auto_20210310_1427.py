# Generated by Django 2.2.1 on 2021-03-10 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20210310_1420'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='user',
            field=models.OneToOneField(on_delete=models.SET('not_active'), to='users.Account'),
        ),
    ]
