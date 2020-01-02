# Generated by Django 3.0.1 on 2020-01-02 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('memories', '0007_auto_20200102_2002'),
    ]

    operations = [
        migrations.AlterField(
            model_name='memory',
            name='date_time',
            field=models.CharField(default='02-01-2020 20:47:15', max_length=200),
        ),
        migrations.AlterField(
            model_name='memory',
            name='image',
            field=models.FileField(default='memories_photo/default.jpg', upload_to='memories_photo'),
        ),
    ]
