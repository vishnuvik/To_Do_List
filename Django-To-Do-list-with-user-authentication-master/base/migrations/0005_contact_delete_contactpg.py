# Generated by Django 4.1.1 on 2022-10-21 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_contactpg'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=200, null=True)),
                ('query', models.CharField(max_length=400, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='contactpg',
        ),
    ]
