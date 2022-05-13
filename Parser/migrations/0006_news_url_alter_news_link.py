# Generated by Django 4.0.4 on 2022-05-12 14:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Parser', '0005_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='url',
            field=models.CharField(default='link', max_length=300),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='news',
            name='link',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Parser.url'),
        ),
    ]
