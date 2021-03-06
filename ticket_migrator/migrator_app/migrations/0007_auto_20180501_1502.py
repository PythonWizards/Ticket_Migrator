# Generated by Django 2.0.4 on 2018-05-01 15:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('migrator_app', '0006_auto_20180427_1050'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sprint_Issues',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('issue_id', models.IntegerField()),
                ('priority', models.IntegerField()),
            ],
        ),
        migrations.RemoveField(
            model_name='backlog_issues',
            name='backlog',
        ),
        migrations.RenameModel(
            old_name='Backlog',
            new_name='Sprint',
        ),
        migrations.DeleteModel(
            name='Backlog_Issues',
        ),
        migrations.AddField(
            model_name='sprint_issues',
            name='sprint',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='migrator_app.Sprint'),
        ),
    ]
