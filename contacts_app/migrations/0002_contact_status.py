# Generated by Django 3.2.8 on 2021-12-05 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='status',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
