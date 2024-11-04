# Generated by Django 5.0.6 on 2024-07-19 06:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0029_rename_images_product_image_image_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='additional_information',
            name='product',
        ),
        migrations.DeleteModel(
            name='banner_area',
        ),
        migrations.RemoveField(
            model_name='product',
            name='brand',
        ),
        migrations.RemoveField(
            model_name='category',
            name='main_category',
        ),
        migrations.RemoveField(
            model_name='sub_category',
            name='category',
        ),
        migrations.RemoveField(
            model_name='product',
            name='colour',
        ),
        migrations.DeleteModel(
            name='Coupon_Code',
        ),
        migrations.RemoveField(
            model_name='order',
            name='user',
        ),
        migrations.RemoveField(
            model_name='product',
            name='categories',
        ),
        migrations.RemoveField(
            model_name='product',
            name='section',
        ),
        migrations.RemoveField(
            model_name='product_image',
            name='product',
        ),
        migrations.DeleteModel(
            name='slider',
        ),
        migrations.DeleteModel(
            name='Additional_information',
        ),
        migrations.DeleteModel(
            name='Brand',
        ),
        migrations.DeleteModel(
            name='Main_category',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='Colour',
        ),
        migrations.DeleteModel(
            name='Order',
        ),
        migrations.DeleteModel(
            name='Sub_category',
        ),
        migrations.DeleteModel(
            name='Section',
        ),
        migrations.DeleteModel(
            name='Product',
        ),
        migrations.DeleteModel(
            name='Product_Image',
        ),
    ]