# Generated by Django 2.2 on 2021-09-04 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BankAccount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.CharField(max_length=250, unique=True, verbose_name='UUID')),
                ('full_name', models.CharField(max_length=250, verbose_name='ФИО')),
                ('current_balance', models.IntegerField(blank=True, null=True, verbose_name='Текущий баланс')),
                ('hold', models.IntegerField(blank=True, null=True, verbose_name='Резерв')),
                ('account_status', models.BooleanField(default=True, verbose_name='Статус счета')),
            ],
            options={
                'verbose_name': 'Счет абонента',
                'verbose_name_plural': 'Счета абонентов',
                'db_table': 'bank_accounts',
            },
        ),
    ]
