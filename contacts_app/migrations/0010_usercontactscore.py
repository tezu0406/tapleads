# Generated by Django 3.2.8 on 2021-12-09 05:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contacts_app', '0009_alter_method_owner'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserContactScore',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField()),
                ('contact', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contacts_app.contact')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
