# Generated by Django 4.1.3 on 2023-03-09 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_site', '0007_alter_transaction_transaction_totalprice'),
    ]

    operations = [
        migrations.AlterField(
            model_name='promo',
            name='promo_amount',
            field=models.BigIntegerField(null=True, verbose_name='Amount'),
        ),
        migrations.AlterField(
            model_name='promo',
            name='promo_discount',
            field=models.BigIntegerField(null=True, verbose_name='Discount'),
        ),
    ]