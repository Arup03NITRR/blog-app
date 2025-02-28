# Generated by Django 5.1.6 on 2025-02-28 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0002_alter_category_options_blogs'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blogs',
            options={'verbose_name_plural': 'Blogs'},
        ),
        migrations.AlterField(
            model_name='blogs',
            name='status',
            field=models.CharField(choices=[('draft', 'Drafted'), ('public', 'Published')], default='draft', max_length=100),
        ),
    ]
