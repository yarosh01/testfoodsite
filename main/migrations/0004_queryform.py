# Generated by Django 3.1.3 on 2020-11-21 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_delete_gallery'),
    ]

    operations = [
        migrations.CreateModel(
            name='QueryForm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('query', models.CharField(max_length=100)),
            ],
        ),
    ]
