# Generated by Django 4.1.6 on 2023-04-04 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_alter_profile_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
