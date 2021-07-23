# Generated by Django 3.2.4 on 2021-07-22 09:41

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0002_shopuser_is_deleted'),
    ]

    operations = [
        migrations.AddField(
            model_name='shopuser',
            name='activation_key',
            field=models.CharField(max_length=128, null=True),
        ),
        migrations.AddField(
            model_name='shopuser',
            name='activation_key_start_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]