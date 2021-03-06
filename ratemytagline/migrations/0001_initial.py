# Generated by Django 2.0.5 on 2018-05-03 10:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='tagLine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('taglineObject', models.CharField(max_length=200)),
                ('numberOfVotes', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='upvotes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('taglineObject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ratemytagline.tagLine')),
            ],
        ),
        migrations.CreateModel(
            name='userModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='upvotes',
            name='userObject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ratemytagline.userModel'),
        ),
        migrations.AddField(
            model_name='tagline',
            name='userObject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ratemytagline.userModel'),
        ),
    ]
