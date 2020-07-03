# Generated by Django 3.0.8 on 2020-07-02 06:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bank',
            fields=[
                ('Name', models.CharField(default='', max_length=50)),
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Branches',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ifsc', models.CharField(default='', max_length=255)),
                ('branch', models.CharField(default='', max_length=255)),
                ('address', models.CharField(default='', max_length=255)),
                ('city', models.CharField(default='', max_length=255)),
                ('district', models.CharField(default='', max_length=255)),
                ('state', models.CharField(default='', max_length=255)),
                ('bank_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Test.Bank')),
            ],
        ),
    ]
