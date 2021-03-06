# Generated by Django 3.0.1 on 2020-01-02 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Memory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('one_line_description', models.CharField(default='Meh..', help_text='Describe your day in 1 line', max_length=200)),
                ('how_was_the_day', models.CharField(choices=[('H', 'HORRIBLE'), ('B', 'BAD'), ('O', 'OK'), ('G', 'GOOD'), ('A', 'AWESOME')], default='OK', max_length=50)),
                ('date_time', models.DateTimeField(auto_now=True)),
                ('image', models.ImageField(upload_to='memories_photo')),
                ('special_comments', models.TextField(blank=True)),
            ],
            options={
                'verbose_name': 'Memory',
                'verbose_name_plural': 'Memories',
            },
        ),
    ]
