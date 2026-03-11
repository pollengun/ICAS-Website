from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import (
    ResearchArea, TeamMember, Publication, Project,
    Event, News, ContactMessage, Partner, Activity
)
from .forms import ContactForm
import datetime


def home(request):
    research_areas = ResearchArea.objects.all()[:6]
    team_leaders = TeamMember.objects.filter(role__in=['director', 'faculty'])[:4]
    recent_publications = Publication.objects.all()[:4]
    ongoing_projects = Project.objects.filter(status='ongoing')[:3]
    featured_events = Event.objects.filter(date__gte=datetime.date.today())[:3]
    recent_news = News.objects.filter(is_featured=True)[:3]
    partners = Partner.objects.all()

    default_objectives = [
        {'title': 'Academic Excellence', 'text': 'Highest standards of academic integrity in research, consulting, and teaching.', 'icon': 'bi-mortarboard'},
        {'title': 'Innovation & Creativity', 'text': 'Fostering innovative culture within the company and the broader educational sector.', 'icon': 'bi-lightbulb'},
        {'title': 'Sustainable Development', 'text': 'Research in environmental sciences, renewable energy, and social development.', 'icon': 'bi-tree'},
        {'title': 'Global Impact', 'text': 'Cross-border research collaborations and international partnership programmes.', 'icon': 'bi-globe2'},
    ]

    context = {
        'research_areas': research_areas,
        'team_leaders': team_leaders,
        'recent_publications': recent_publications,
        'ongoing_projects': ongoing_projects,
        'featured_events': featured_events,
        'recent_news': recent_news,
        'partners': partners,
        'default_objectives': default_objectives,
        'stats': {
            'publications': Publication.objects.count(),
            'projects': Project.objects.count(),
            'team_members': TeamMember.objects.count(),
            'events': Event.objects.count(),
        }
    }
    return render(request, 'icas/home.html', context)


def about(request):
    default_objectives = [
        {'title': 'Academic Excellence', 'text': 'Upholding the highest standards of academic integrity and quality across all endeavours including research, consulting, and teaching.'},
        {'title': 'Innovation and Creativity', 'text': 'Fostering an innovative and creative culture within the company as well as in the larger business and educational sectors.'},
        {'title': 'Sustainable Development', 'text': 'Research and consultancy in environmental sciences, renewable energy, and social development that support sustainable practices.'},
        {'title': 'Empowering People', 'text': 'Through excellent educational programs, training sessions, seminars, and consulting services to improve knowledge, skills, and capabilities.'},
        {'title': 'Interdisciplinary Collaboration', 'text': 'Promoting cooperation amongst different sectors, industry, and academic disciplines for comprehensive solutions.'},
        {'title': 'Seeking Global Impact', 'text': 'Actively participating in cross-border research collaborations and working with international partners.'},
        {'title': 'Ethical and Social Responsibility', 'text': 'Integrity, openness, and a dedication to the well-being of society are key components of all research and consulting practices.'},
        {'title': 'Learning and Improvement', 'text': 'Fostering a culture of continuous improvement, modification, and learning incorporating best practices into daily operations.'},
    ]
    context = {
        'page_title': 'About ICAS',
        'default_objectives': default_objectives,
    }
    return render(request, 'icas/about.html', context)


def research(request):
    areas = ResearchArea.objects.all()
    ongoing = Project.objects.filter(status='ongoing')
    completed = Project.objects.filter(status='completed')
    context = {
        'page_title': 'Research',
        'areas': areas,
        'ongoing_projects': ongoing,
        'completed_projects': completed,
    }
    return render(request, 'icas/research.html', context)


def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    context = {
        'page_title': project.title,
        'project': project,
    }
    return render(request, 'icas/project_detail.html', context)


def team(request):
    presidents = TeamMember.objects.filter(role='president')
    directors = TeamMember.objects.filter(role='director')
    faculty = TeamMember.objects.filter(role='faculty')
    researchers = TeamMember.objects.filter(role='researcher')
    students = TeamMember.objects.filter(role='student')
    context = {
        'page_title': 'Our Team',
        'presidents': presidents,
        'directors': directors,
        'faculty': faculty,
        'researchers': researchers,
        'students': students,
    }
    return render(request, 'icas/team.html', context)


def publications(request):
    pub_type = request.GET.get('type', '')
    year = request.GET.get('year', '')

    pubs = Publication.objects.all()
    if pub_type:
        pubs = pubs.filter(pub_type=pub_type)
    if year:
        pubs = pubs.filter(year=year)

    years = Publication.objects.values_list('year', flat=True).distinct().order_by('-year')
    context = {
        'page_title': 'Publications',
        'publications': pubs,
        'years': years,
        'selected_type': pub_type,
        'selected_year': year,
        'pub_types': Publication.TYPE_CHOICES,
    }
    return render(request, 'icas/publications.html', context)


def events(request):
    upcoming = Event.objects.filter(date__gte=datetime.date.today())
    past = Event.objects.filter(date__lt=datetime.date.today())
    context = {
        'page_title': 'Events',
        'upcoming_events': upcoming,
        'past_events': past,
    }
    return render(request, 'icas/events.html', context)

def event_detail(request, pk):
    event = get_object_or_404(Event, pk=pk)
    context = {'event': event}
    return render(request, 'icas/event_detail.html', context)


def news_list(request):
    all_news = News.objects.all()
    context = {
        'page_title': 'News & Updates',
        'news_list': all_news,
    }
    return render(request, 'icas/news.html', context)

def news_detail(request, pk):
    news = get_object_or_404(News, pk=pk)
    context = {'news': news}
    return render(request, 'icas/news_detail.html', context)

def activities(request):
    all_activities = Activity.objects.all()
    context = {
        'page_title': 'Work Identity (ICAS)',
        'activities': all_activities,
    }
    return render(request, 'icas/activities.html', context)

def activity_detail(request, pk):
    activity = get_object_or_404(Activity, pk=pk)
    context = {'activity': activity}
    return render(request, 'icas/activity_detail.html', context)

def contact_personnel(request):
    personnel = TeamMember.objects.filter(show_on_contact_page=True)
    context = {
        'page_title': 'Contact Personnel',
        'personnel': personnel,
    }
    return render(request, 'icas/contact_personnel.html', context)


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            ContactMessage.objects.create(
                name=form.cleaned_data['name'],
                email=form.cleaned_data['email'],
                subject=form.cleaned_data['subject'],
                message=form.cleaned_data['message'],
            )
            messages.success(request, 'Thank you! Your message has been received. We will get back to you soon.')
            return redirect('contact')
    else:
        form = ContactForm()

    context = {
        'page_title': 'Contact Us',
        'form': form,
    }
    return render(request, 'icas/contact.html', context)

# ── Authentication views ──

def staff_login(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            if user.is_staff or user.is_superuser:
                login(request, user)
                return redirect(request.GET.get('next', 'dashboard'))
            else:
                messages.error(request, 'You do not have staff access.')
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'icas/login.html')


def staff_logout(request):
    logout(request)
    messages.success(request, 'You have been logged out successfully.')
    return redirect('home')


@login_required(login_url='login')
def dashboard(request):
    context = {
        'total_publications': Publication.objects.count(),
        'total_projects': Project.objects.count(),
        'total_team': TeamMember.objects.count(),
        'total_events': Event.objects.count(),
        'total_news': News.objects.count(),
        'total_activities': Activity.objects.count(),
        'unread_messages': ContactMessage.objects.filter(is_read=False).count(),
        'recent_messages': ContactMessage.objects.order_by('-submitted_at')[:5],
        'recent_news': News.objects.order_by('-date_posted')[:5],
        'upcoming_events': Event.objects.filter(date__gte=datetime.date.today()).order_by('date')[:5],
    }
    return render(request, 'icas/dashboard.html', context)

