# Generated by Django 3.1.7 on 2021-03-22 02:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foods', '0011_auto_20210321_2007'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restarantinfo',
            name='rest_image',
            field=models.ImageField(blank=True, default='foodproject\\foods\\placehold_stock.jpg', upload_to=''),
        ),
    ]