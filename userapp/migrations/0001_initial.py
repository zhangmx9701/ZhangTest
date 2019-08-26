# Generated by Django 2.0.6 on 2019-07-15 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=20)),
                ('pwd', models.CharField(max_length=20)),
                ('sex', models.CharField(max_length=5)),
                ('headpic', models.ImageField(null=True, upload_to='user')),
            ],
        ),
    ]