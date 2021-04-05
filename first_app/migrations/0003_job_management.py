# Generated by Django 2.2.1 on 2019-10-15 12:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0002_userprofileinfo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Job_Management',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_title', models.CharField(blank=True, max_length=100)),
                ('job_type', models.CharField(blank=True, max_length=100)),
                ('experience', models.CharField(blank=True, max_length=100)),
                ('department', models.CharField(blank=True, max_length=100)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='first_app.UserProfileInfo')),
            ],
        ),
    ]