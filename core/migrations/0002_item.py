# Generated by Django 4.1.5 on 2023-03-01 19:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('list', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.list')),
            ],
        ),
    ]
