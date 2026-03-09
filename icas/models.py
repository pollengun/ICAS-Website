from django.db import models


class ResearchArea(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    icon = models.CharField(max_length=100, default='bi-microscope')
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title


class TeamMember(models.Model):
    ROLE_CHOICES = [
        ('president', 'President'),
        ('director', 'Director'),
        ('faculty', 'Faculty Researcher'),
        ('researcher', 'Researcher'),
        ('student', 'Graduate Student'),
    ]
    name = models.CharField(max_length=200)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, blank=True)
    designation = models.CharField(max_length=200, blank=True)
    department = models.CharField(max_length=200, blank=True)
    qualification = models.CharField(max_length=200, blank=True)
    university = models.CharField(max_length=200, blank=True)
    bio = models.TextField(blank=True)
    photo = models.ImageField(upload_to='team/', blank=True, null=True)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=100, blank=True)
    linkedin = models.URLField(blank=True)
    google_scholar = models.URLField(blank=True)
    show_on_contact_page = models.BooleanField(default=False)
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order', 'name']

    def __str__(self):
        return self.name


class Publication(models.Model):
    TYPE_CHOICES = [
        ('journal', 'Journal Article'),
        ('conference', 'Conference Paper'),
        ('book', 'Book Chapter'),
        ('report', 'Technical Report'),
    ]
    title = models.CharField(max_length=500)
    authors = models.CharField(max_length=500)
    pub_type = models.CharField(max_length=20, choices=TYPE_CHOICES, default='journal')
    journal_or_venue = models.CharField(max_length=300, blank=True)
    year = models.IntegerField()
    doi = models.CharField(max_length=200, blank=True)
    abstract = models.TextField(blank=True)
    pdf_link = models.URLField(blank=True)

    class Meta:
        ordering = ['-year', 'title']

    def __str__(self):
        return self.title


class Project(models.Model):
    STATUS_CHOICES = [
        ('ongoing', 'Ongoing'),
        ('completed', 'Completed'),
        ('upcoming', 'Upcoming'),
    ]
    title = models.CharField(max_length=300)
    description = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='ongoing')
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    funding_agency = models.CharField(max_length=200, blank=True)
    budget = models.CharField(max_length=100, blank=True)
    principal_investigator = models.ForeignKey(
        TeamMember, on_delete=models.SET_NULL, null=True, blank=True
    )
    image = models.ImageField(upload_to='projects/', blank=True, null=True)

    class Meta:
        ordering = ['-start_date']

    def __str__(self):
        return self.title


class Event(models.Model):
    TYPE_CHOICES = [
        ('seminar', 'Seminar'),
        ('workshop', 'Workshop'),
        ('conference', 'Conference'),
        ('webinar', 'Webinar'),
        ('training', 'Training'),
    ]
    title = models.CharField(max_length=300)
    event_type = models.CharField(max_length=20, choices=TYPE_CHOICES, default='seminar')
    description = models.TextField()
    date = models.DateField()
    time = models.TimeField(blank=True, null=True)
    venue = models.CharField(max_length=300)
    image = models.ImageField(upload_to='events/', blank=True, null=True)
    registration_link = models.URLField(blank=True)
    is_featured = models.BooleanField(default=False)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return self.title


class News(models.Model):
    title = models.CharField(max_length=300)
    content = models.TextField()
    date_posted = models.DateField(auto_now_add=True)
    image = models.ImageField(upload_to='news/', blank=True, null=True)
    is_featured = models.BooleanField(default=False)

    class Meta:
        ordering = ['-date_posted']
        verbose_name_plural = 'News'

    def __str__(self):
        return self.title


class ContactMessage(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    subject = models.CharField(max_length=300)
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} - {self.subject}"


class Activity(models.Model):
    title = models.CharField(max_length=300)
    description = models.TextField()
    image = models.ImageField(upload_to='activities/', blank=True, null=True)
    date = models.DateField()
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order', '-date']
        verbose_name_plural = 'Activities'

    def __str__(self):
        return self.title


class Partner(models.Model):
    name = models.CharField(max_length=200)
    logo = models.ImageField(upload_to='partners/', blank=True, null=True)
    website = models.URLField(blank=True)
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.name
