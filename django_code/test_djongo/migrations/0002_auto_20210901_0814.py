# Generated by Django 3.2.6 on 2021-09-01 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test_djongo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book_Author_Emaill',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('emaill', models.EmailField(max_length=254)),
            ],
        ),
        migrations.AlterField(
            model_name='book',
            name='hoot_book',
            field=models.BooleanField(null=True),
        ),
    ]
