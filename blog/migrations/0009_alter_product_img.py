# Generated by Django 5.0 on 2024-06-19 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_alter_product_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='product'),
        ),
    ]
