# Generated by Django 2.2.4 on 2019-12-04 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('email', models.CharField(max_length=250)),
                ('phone', models.CharField(max_length=250)),
                ('nit', models.CharField(max_length=250)),
                ('city', models.CharField(max_length=250)),
                ('address', models.CharField(max_length=250)),
            ],
        ),
    ]
