# Generated by Django 3.2.4 on 2022-09-21 11:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BannerAreas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Images', models.ImageField(upload_to='media/banner_imgs')),
                ('Discount_Deal', models.CharField(max_length=100)),
                ('Quote', models.CharField(max_length=200)),
                ('Discount', models.IntegerField()),
                ('Link', models.CharField(max_length=500, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Catagory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='MainCatagory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='slider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Image', models.ImageField(upload_to='media/slider_imgs')),
                ('Discount_Deal', models.CharField(choices=[('HOT DEALS', 'HOT DEALS'), ('NEW ARRAIVELS', 'NEW ARRAIVELS')], max_length=100)),
                ('SALE', models.IntegerField()),
                ('Brand_Name', models.CharField(max_length=200)),
                ('Discount', models.IntegerField()),
                ('Link', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='SubCatagory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('Catagory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.catagory')),
            ],
        ),
        migrations.AddField(
            model_name='catagory',
            name='MainCatagory',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.maincatagory'),
        ),
    ]
