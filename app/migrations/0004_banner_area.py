# Generated by Django 5.0.6 on 2024-06-28 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_rename_brand_slider_brand_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='banner_area',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='media/banner_img')),
                ('Discount_Deal', models.CharField(max_length=100)),
                ('Quotes', models.CharField(max_length=100)),
                ('Discount', models.IntegerField()),
            ],
        ),
    ]
