# Generated by Django 5.1.3 on 2024-11-08 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plants', '0002_alter_plant_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plant',
            name='category',
            field=models.CharField(choices=[('Flwr_plant', 'Flowering Plant'), ('non-Flowering_Plant', 'Non-Flowering Plant'), ('Tree', 'Tree'), ('Herb', 'Herb'), ('Shrub', 'Shrub'), ('aquatic_plant', 'Aquatic Plant')], max_length=56),
        ),
    ]