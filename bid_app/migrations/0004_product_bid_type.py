# Generated by Django 4.0.4 on 2022-05-18 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bid_app', '0003_category_sub_category_send_feedback_product_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='bid_type',
            field=models.CharField(max_length=100, null=True),
        ),
    ]