# Generated by Django 2.2.4 on 2019-10-08 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ragistration', '0016_auto_20191008_1840'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ragister',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
            ],
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(error_messages={'unique': 'You are allready apply'}, max_length=300, unique=True),
        ),
    ]
