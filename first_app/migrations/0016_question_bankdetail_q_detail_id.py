# Generated by Django 2.2.1 on 2019-11-03 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0015_remove_question_bankdetail_question_bankdetail_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='question_bankdetail',
            name='q_detail_id',
            field=models.CharField(default=12, max_length=6, unique=True),
            preserve_default=False,
        ),
    ]