# Generated by Django 3.2.8 on 2021-10-17 16:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('houseplants_api', '0004_alter_waterschedule_plant'),
    ]

    operations = [
        migrations.CreateModel(
            name='WateringLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('water_date', models.DateField(auto_now_add=True)),
                ('next_suggested_date', models.DateField()),
                ('plant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='houseplants_api.plant')),
            ],
        ),
        migrations.DeleteModel(
            name='WaterPlan',
        ),
    ]
