# Generated by Django 4.0.4 on 2022-05-12 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Parser', '0003_remove_news_link'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Url',
        ),
        migrations.AddField(
            model_name='news',
            name='link',
            field=models.CharField(default='qwe', max_length=300),
            preserve_default=False,
        ),
    ]
