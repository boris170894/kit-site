# Generated by Django 4.1.7 on 2023-02-14 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_newsmodel_img_alter_newsmodel_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsmodel',
            name='img',
            field=models.ImageField(upload_to='uploads/news/%Y/%m/%d/', verbose_name='Изображение новости'),
        ),
    ]
