# Generated by Django 3.1.3 on 2021-04-10 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0008_paymenttoken'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paymenttoken',
            name='token',
            field=models.CharField(max_length=40),
        ),
    ]