# Generated by Django 3.0.1 on 2020-01-02 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('memories', '0002_auto_20200102_1246'),
    ]

    operations = [
        migrations.AlterField(
            model_name='memory',
            name='date_time',
            field=models.CharField(default='02-01-2020T07:18:20', max_length=200),
        ),
    ]
