# Generated by Django 4.1.6 on 2023-03-29 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_rename_transiaction_id_order_transaction_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='desc',
            field=models.TextField(null=True),
        ),
    ]