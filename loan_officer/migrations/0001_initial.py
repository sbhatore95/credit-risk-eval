# Generated by Django 3.0.4 on 2020-04-06 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SavedState',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stat', models.CharField(max_length=10)),
                ('ml', models.CharField(max_length=10)),
                ('statandml', models.CharField(default='false', max_length=10)),
            ],
        ),
    ]
