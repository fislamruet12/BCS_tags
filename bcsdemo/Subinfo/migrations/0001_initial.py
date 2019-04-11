# Generated by Django 2.0 on 2019-04-04 12:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='contcatagory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contentlist', models.CharField(max_length=100)),
                ('cata_pic', models.ImageField(default='cata_folder/None/no-img.jpg', upload_to='cata_folder/')),
            ],
        ),
        migrations.CreateModel(
            name='contentelement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('content', models.CharField(max_length=45000)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('contcatagory_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Subinfo.contcatagory')),
            ],
        ),
        migrations.CreateModel(
            name='contentelementimage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content_pic', models.ImageField(default='content_folder/None/no-img.jpg', upload_to='content_folder/')),
                ('contentelement_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Subinfo.contentelement')),
            ],
        ),
        migrations.CreateModel(
            name='contenttableinfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tl1', models.CharField(max_length=450)),
                ('tl2', models.CharField(max_length=450)),
                ('tl3', models.CharField(max_length=450)),
                ('tl4', models.CharField(max_length=450)),
                ('tl5', models.CharField(max_length=450)),
                ('tl6', models.CharField(max_length=450)),
            ],
        ),
        migrations.CreateModel(
            name='contenttabletitle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('cl1', models.CharField(max_length=50)),
                ('cl2', models.CharField(max_length=50)),
                ('cl3', models.CharField(max_length=50)),
                ('cl4', models.CharField(max_length=50)),
                ('cl5', models.CharField(max_length=50)),
                ('cl6', models.CharField(max_length=50)),
                ('contenttable_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Subinfo.contentelement')),
            ],
        ),
        migrations.CreateModel(
            name='question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('que_pic', models.ImageField(default='que_folder/None/no-img.jpg', upload_to='que_folder/')),
                ('op1', models.CharField(max_length=200)),
                ('op2', models.CharField(max_length=200)),
                ('op3', models.CharField(max_length=200)),
                ('op4', models.CharField(max_length=200)),
                ('ans', models.IntegerField()),
                ('explain', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='subcatagory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('catalist', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='subjects',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('bio', models.CharField(max_length=100)),
                ('model_pic', models.ImageField(default='pic_folder/None/no-img.jpg', upload_to='pic_folder/')),
            ],
        ),
        migrations.CreateModel(
            name='types',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('types_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Subinfo.contentelement')),
            ],
        ),
        migrations.AddField(
            model_name='subcatagory',
            name='subject_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Subinfo.subjects'),
        ),
        migrations.AddField(
            model_name='question',
            name='question_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Subinfo.types'),
        ),
        migrations.AddField(
            model_name='contenttableinfo',
            name='contenttabletitle_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Subinfo.contenttabletitle'),
        ),
        migrations.AddField(
            model_name='contcatagory',
            name='subcatagory_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Subinfo.subcatagory'),
        ),
    ]
