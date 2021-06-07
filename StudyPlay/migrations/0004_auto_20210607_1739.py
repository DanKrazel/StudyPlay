# Generated by Django 2.1.15 on 2021-06-07 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('StudyPlay', '0003_auto_20210512_0943'),
    ]

    operations = [
        migrations.CreateModel(
            name='ActivityDoneModel',
            fields=[
                ('ID', models.IntegerField(db_column='ID', default=None, primary_key=True, serialize=False)),
                ('NameAct', models.CharField(db_column='NameAct', default=None, max_length=100)),
                ('PseudoC', models.CharField(db_column='PseudoC', default=None, max_length=100)),
                ('PseudoP', models.CharField(db_column='PseudoP', default=None, max_length=100)),
                ('Grade', models.CharField(db_column='Grade', default=None, max_length=100)),
                ('NumOfGame', models.IntegerField(db_column='NumOfGame', default=1)),
            ],
            options={
                'db_table': 'activityDone',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='ReviewsModel',
            fields=[
                ('ID', models.IntegerField(db_column='ID', default=None, primary_key=True, serialize=False)),
                ('Description', models.CharField(db_column='Description', default=None, max_length=100)),
                ('Ratings', models.IntegerField(db_column='Ratings')),
            ],
            options={
                'db_table': 'reviews',
                'managed': True,
            },
        ),
        migrations.RemoveField(
            model_name='activitiesmodel',
            name='id',
        ),
        migrations.RemoveField(
            model_name='countriesmodel',
            name='id',
        ),
        migrations.AddField(
            model_name='activitiesmodel',
            name='ID',
            field=models.IntegerField(db_column='ID', default=None, primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name='activitiesmodel',
            name='Link',
            field=models.CharField(db_column='Link', default=None, max_length=100),
        ),
        migrations.AddField(
            model_name='childmodel',
            name='profile_pic',
            field=models.ImageField(blank=True, default=None, upload_to='static/images/', verbose_name='profile1.png'),
        ),
        migrations.AddField(
            model_name='countriesmodel',
            name='ID',
            field=models.IntegerField(db_column='ID', default=None, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='childmodel',
            name='ParentsPseudo',
            field=models.CharField(db_column='ParentsPseudo', default=None, max_length=10),
        ),
        migrations.AlterField(
            model_name='childmodel',
            name='Password',
            field=models.CharField(db_column='Password', max_length=10),
        ),
        migrations.AlterField(
            model_name='countriesmodel',
            name='Name',
            field=models.CharField(db_column='Name', default=None, max_length=100),
        ),
        migrations.AlterField(
            model_name='parentsmodel',
            name='profile_pic',
            field=models.ImageField(blank=True, default=None, upload_to='static/images/', verbose_name='profile1.png'),
        ),
    ]
