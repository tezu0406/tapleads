# Generated by Django 3.2.8 on 2021-12-10 15:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contacts_app', '0017_alter_userdata_current_method'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserContactScore',
        ),
    ]
