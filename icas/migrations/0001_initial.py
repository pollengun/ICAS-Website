from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ResearchArea',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('icon', models.CharField(default='bi-microscope', max_length=100)),
                ('order', models.IntegerField(default=0)),
            ],
            options={'ordering': ['order']},
        ),
        migrations.CreateModel(
            name='Partner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('logo', models.ImageField(blank=True, null=True, upload_to='partners/')),
                ('website', models.URLField(blank=True)),
                ('order', models.IntegerField(default=0)),
            ],
            options={'ordering': ['order']},
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('content', models.TextField()),
                ('date_posted', models.DateField(auto_now_add=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='news/')),
                ('is_featured', models.BooleanField(default=False)),
            ],
            options={'ordering': ['-date_posted'], 'verbose_name_plural': 'News'},
        ),
        migrations.CreateModel(
            name='ContactMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField()),
                ('subject', models.CharField(max_length=300)),
                ('message', models.TextField()),
                ('submitted_at', models.DateTimeField(auto_now_add=True)),
                ('is_read', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='TeamMember',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('role', models.CharField(choices=[('director', 'Director'), ('faculty', 'Faculty Researcher'), ('researcher', 'Researcher'), ('student', 'Graduate Student')], max_length=20)),
                ('designation', models.CharField(max_length=200)),
                ('bio', models.TextField(blank=True)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='team/')),
                ('email', models.EmailField(blank=True)),
                ('linkedin', models.URLField(blank=True)),
                ('google_scholar', models.URLField(blank=True)),
                ('order', models.IntegerField(default=0)),
            ],
            options={'ordering': ['order', 'name']},
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('description', models.TextField()),
                ('status', models.CharField(choices=[('ongoing', 'Ongoing'), ('completed', 'Completed'), ('upcoming', 'Upcoming')], default='ongoing', max_length=20)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField(blank=True, null=True)),
                ('funding_agency', models.CharField(blank=True, max_length=200)),
                ('budget', models.CharField(blank=True, max_length=100)),
                ('image', models.ImageField(blank=True, null=True, upload_to='projects/')),
                ('principal_investigator', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='icas.teammember')),
            ],
            options={'ordering': ['-start_date']},
        ),
        migrations.CreateModel(
            name='Publication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('authors', models.CharField(max_length=500)),
                ('pub_type', models.CharField(choices=[('journal', 'Journal Article'), ('conference', 'Conference Paper'), ('book', 'Book Chapter'), ('report', 'Technical Report')], default='journal', max_length=20)),
                ('journal_or_venue', models.CharField(blank=True, max_length=300)),
                ('year', models.IntegerField()),
                ('doi', models.CharField(blank=True, max_length=200)),
                ('abstract', models.TextField(blank=True)),
                ('pdf_link', models.URLField(blank=True)),
            ],
            options={'ordering': ['-year', 'title']},
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('event_type', models.CharField(choices=[('seminar', 'Seminar'), ('workshop', 'Workshop'), ('conference', 'Conference'), ('webinar', 'Webinar'), ('training', 'Training')], default='seminar', max_length=20)),
                ('description', models.TextField()),
                ('date', models.DateField()),
                ('time', models.TimeField(blank=True, null=True)),
                ('venue', models.CharField(max_length=300)),
                ('image', models.ImageField(blank=True, null=True, upload_to='events/')),
                ('registration_link', models.URLField(blank=True)),
                ('is_featured', models.BooleanField(default=False)),
            ],
            options={'ordering': ['-date']},
        ),
    ]
