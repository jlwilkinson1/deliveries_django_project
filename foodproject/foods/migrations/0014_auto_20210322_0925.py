# Generated by Django 3.1.7 on 2021-03-22 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foods', '0013_auto_20210321_2008'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restarantinfo',
            name='rest_image',
            field=models.ImageField(blank=True, default='foods/placehold_stock.jpg', upload_to=''),
        ),
    ]