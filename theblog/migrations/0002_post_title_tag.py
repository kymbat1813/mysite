# Generated by Django 3.2.3 on 2021-05-14 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='title_tag',
            field=models.CharField(default='Заголовок объявления', max_length=255),
        ),
    ]