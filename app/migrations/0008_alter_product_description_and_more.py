# Generated by Django 5.0.6 on 2024-06-30 09:29

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_section_product_additional_information_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='description',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_information',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
