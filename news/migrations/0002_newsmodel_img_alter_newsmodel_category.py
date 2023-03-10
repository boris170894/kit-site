# Generated by Django 4.1.7 on 2023-02-14 14:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsmodel',
            name='img',
            field=models.ImageField(default=1, upload_to='uploads/% Y/% m/% d/', verbose_name='Изображение новости'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='newsmodel',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='news.newscategorymodel', verbose_name='Категория'),
        ),
    ]
