# Generated by Django 4.0.3 on 2022-03-14 04:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SubscriptionPlan',
            fields=[
                ('Id', models.AutoField(db_column='Id', primary_key=True, serialize=False)),
                ('SubscriptionName', models.CharField(db_column='AppName', max_length=225)),
                ('Description', models.TextField(db_column='Description', default=None)),
                ('RegisterDate', models.DateTimeField(db_column='RegisterDate')),
            ],
            options={
                'db_table': 'SubscriptionPlan',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('Id', models.AutoField(db_column='Id', primary_key=True, serialize=False)),
                ('UserName', models.CharField(db_column='UserName', max_length=225)),
                ('Email', models.CharField(db_column='Email', max_length=225)),
                ('Password', models.CharField(db_column='Password', max_length=20)),
                ('AuthentiationCode', models.CharField(db_column='AuthentiationCode', max_length=52)),
                ('RegisterDate', models.DateTimeField(db_column='RegisterDate')),
            ],
            options={
                'db_table': 'User',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='APP',
            fields=[
                ('Id', models.AutoField(db_column='Id', primary_key=True, serialize=False)),
                ('AppName', models.CharField(db_column='AppName', max_length=225)),
                ('Description', models.TextField(db_column='Description', default=None)),
                ('SubscriptionName', models.CharField(db_column='SubscriptionName', default='Free', max_length=225)),
                ('SubscriptionPrice', models.FloatField(db_column='SubscriptionPrice', default=0)),
                ('active', models.CharField(db_column='active', default=True, max_length=225)),
                ('CreatedDate', models.DateTimeField(db_column='CreatedDate')),
                ('EndDate', models.DateTimeField(db_column='EndDate')),
                ('UserId', models.ForeignKey(db_column='UserId', on_delete=django.db.models.deletion.CASCADE, to='CoreApp.user')),
            ],
            options={
                'db_table': 'APP',
                'managed': True,
            },
        ),
    ]