# Generated by Django 2.2.1 on 2019-11-11 04:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0033_auto_20191111_0817'),
    ]

    operations = [
        migrations.CreateModel(
            name='codecheck',
            fields=[
                ('detail_id', models.IntegerField(primary_key=True, serialize=False)),
                ('Code_id', models.CharField(max_length=100)),
            ],
        ),
    ]