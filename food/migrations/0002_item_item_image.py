# Generated by Django 3.2.3 on 2023-06-21 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='item_image',
            field=models.CharField(default='https://livingstonbagel.com/wp-content/uploads/2016/11/food-placeholder.jpg', max_length=500),
        ),
    ]
