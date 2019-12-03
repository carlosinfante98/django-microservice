# Generated by Django 2.2 on 2019-11-30 22:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('clients', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_price', models.FloatField(default=0.0)),
                ('purchase_date', models.DateTimeField(null=True, verbose_name='date purchased')),
                ('delivery_date', models.DateTimeField(null=True, verbose_name='delivery date')),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='clients.Client')),
            ],
        ),
        migrations.AddConstraint(
            model_name='purchase',
            constraint=models.CheckConstraint(check=models.Q(total_price__gte=0), name='positive_price'),
        ),
        migrations.AddConstraint(
            model_name='purchase',
            constraint=models.UniqueConstraint(fields=('owner', 'purchase_date'), name='unique_purchase_owner'),
        ),
    ]
