# Generated by Django 3.1.1 on 2020-09-26 11:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Equipments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eqi_name', models.CharField(max_length=200)),
                ('Price', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='ngo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ngo_name', models.CharField(max_length=50)),
                ('ngo_email', models.EmailField(max_length=254, unique=True)),
                ('ngo_phone', models.IntegerField(unique=True)),
                ('ngo_pass', models.CharField(max_length=25)),
                ('Address', models.TextField(max_length=300)),
                ('Country', models.CharField(max_length=50)),
                ('pincode', models.IntegerField()),
                ('weblink', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=30)),
                ('lname', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone', models.IntegerField(unique=True)),
                ('password', models.CharField(max_length=25)),
                ('Address', models.TextField(max_length=300)),
                ('country', models.CharField(max_length=50)),
                ('pincode', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Requirements',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Quantity', models.IntegerField()),
                ('eqi_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.equipments')),
                ('ngo_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.ngo')),
            ],
        ),
        migrations.CreateModel(
            name='Donations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Quantity', models.IntegerField()),
                ('eqi_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.equipments')),
                ('ngo_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.ngo')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.user')),
            ],
        ),
    ]
