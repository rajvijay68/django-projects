# Generated by Django 3.0.1 on 2020-01-02 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('memories', '0005_auto_20200102_1554'),
    ]

    operations = [
        migrations.AlterField(
            model_name='memory',
            name='date_time',
            field=models.CharField(default='02-01-2020 18:51:48', max_length=200),
        ),
        migrations.AlterField(
            model_name='memory',
            name='how_was_the_day',
            field=models.CharField(choices=[('HORRIBLE', 'HORRIBLE'), ('BAD', 'BAD'), ('OK', 'OK'), ('GOOD', 'GOOD'), ('AWESOME', 'AWESOME')], default='OK', max_length=50),
        ),
    ]