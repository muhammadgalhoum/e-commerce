# Generated by Django 4.1.7 on 2023-02-21 15:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_product_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='transiaction_id',
            new_name='transaction_id',
        ),
    ]