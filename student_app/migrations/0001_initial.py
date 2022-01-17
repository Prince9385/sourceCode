# Generated by Django 4.0 on 2022-01-13 05:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StudentInfo',
            fields=[
                ('Rollno', models.IntegerField(primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=150)),
                ('Class', models.CharField(max_length=150)),
                ('School', models.CharField(max_length=150)),
                ('Mobile', models.IntegerField()),
                ('Address', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='StudentAcademics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Maths', models.IntegerField()),
                ('Physics', models.IntegerField()),
                ('Chemistry', models.IntegerField()),
                ('Biology', models.IntegerField()),
                ('English', models.IntegerField()),
                ('Rollno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student_app.studentinfo')),
            ],
        ),
    ]
