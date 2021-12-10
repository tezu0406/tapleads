# Generated by Django 3.2.8 on 2021-12-10 06:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contacts_app', '0013_alter_userdata_total_limits'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='view',
            name='view_contact',
        ),
        migrations.AddField(
            model_name='view',
            name='contact',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='contacts_app.contact'),
        ),
    ]
