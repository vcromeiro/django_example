# Generated by Django 2.0.5 on 2018-05-28 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to='product_image'),
        ),
    ]