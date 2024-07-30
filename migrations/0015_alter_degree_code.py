# Generated by Django 4.1.5 on 2024-07-30 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shell', '0014_alter_residence_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='degree',
            name='code',
            field=models.CharField(choices=[('btech', 'B.Tech. - Bachelor of Technology'), ('idd', 'Int. M.Tech. - Integrated Dual Degree'), ('bsc', 'B.Sc. - Bachelor of Science'), ('barch', 'B.Arch. - Bachelor of Architecture'), ('imsc', 'Int. M.Sc. - Integrated Master of Science'), ('imt', 'Int. M.Tech - Integrated Master of Technology'), ('bsms', 'BS-MS - Bachelor of Science - Master of Science'), ('bdes', 'B.Des. - Bachelor of Design'), ('mtech', 'M.Tech. - Master of Technology'), ('msc', 'M.Sc. - Master of Science'), ('march', 'M.Arch. - Master of Architecture'), ('murp', 'M.U.R.P - Master of Urban and Regional Planning'), ('pgdip', 'P.G. Dip. - Post-graduate Diploma'), ('mba', 'M.B.A. - Master of Business Administration'), ('mca', 'M.C.A. - Master of Computer Applications'), ('mdes', 'M.Des. - Master of Design'), ('mim', 'Master in Innovation Management'), ('phd', 'Ph.D. - Doctor of Philosophy'), ('pdoc', 'Post Doc. - Post-doctorate')], max_length=7, unique=True),
        ),
    ]
