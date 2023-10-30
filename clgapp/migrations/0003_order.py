# Generated by Django 4.2.5 on 2023-10-27 13:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clgapp', '0002_courses'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('dob', models.DateField()),
                ('age', models.IntegerField()),
                ('gender', models.CharField(max_length=10)),
                ('phone_number', models.CharField(max_length=15)),
                ('mail_id', models.EmailField(max_length=254)),
                ('address', models.TextField()),
                ('purpose', models.CharField(max_length=20)),
                ('materials_provided', models.CharField(max_length=255)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clgapp.courses')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clgapp.department')),
            ],
        ),
    ]