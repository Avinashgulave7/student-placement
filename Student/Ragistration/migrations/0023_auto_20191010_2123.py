# Generated by Django 2.2.4 on 2019-10-10 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ragistration', '0022_auto_20191010_2120'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='feedback',
            field=models.TextField(),
        ),
    ]