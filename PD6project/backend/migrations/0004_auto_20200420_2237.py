# Generated by Django 3.0.5 on 2020-04-20 22:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0003_performancedata'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='certificate',
            options={'ordering': ['report_number']},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['product_name']},
        ),
        migrations.AlterModelOptions(
            name='service',
            options={'ordering': ['service_name']},
        ),
    ]