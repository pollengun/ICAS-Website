from django.contrib import admin
from .models import (
    ResearchArea, TeamMember, Publication, Project,
    Event, News, ContactMessage, Partner, Activity
)


@admin.register(ResearchArea)
class ResearchAreaAdmin(admin.ModelAdmin):
    list_display = ['title', 'order']
    ordering = ['order']


@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ['name', 'role', 'designation', 'phone', 'show_on_contact_page', 'order']
    list_filter = ['role', 'show_on_contact_page']
    search_fields = ['name', 'designation', 'department', 'email']
    filter_horizontal = ['research_areas']
    ordering = ['order', 'name']


@admin.register(Publication)
class PublicationAdmin(admin.ModelAdmin):
    list_display = ['title', 'authors', 'pub_type', 'year']
    list_filter = ['pub_type', 'year', 'research_areas']
    search_fields = ['title', 'authors']
    filter_horizontal = ['team_members', 'research_areas', 'projects']


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'status', 'principal_investigator', 'start_date', 'funding_agency']
    list_filter = ['status', 'research_areas', 'partners']
    search_fields = ['title', 'description', 'funding_agency']
    autocomplete_fields = ['principal_investigator']
    filter_horizontal = ['research_areas', 'team_members', 'partners']


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ['title', 'event_type', 'date', 'venue', 'is_featured']
    list_filter = ['event_type', 'is_featured', 'research_areas']
    search_fields = ['title', 'description', 'venue']
    filter_horizontal = ['organizers', 'related_projects', 'research_areas']


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['title', 'date_posted', 'is_featured']
    list_filter = ['is_featured', 'date_posted']
    search_fields = ['title', 'content']
    filter_horizontal = ['related_projects', 'related_events', 'related_publications']


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject', 'related_project', 'assigned_to', 'submitted_at', 'is_read']
    list_filter = ['is_read', 'submitted_at']
    search_fields = ['name', 'email', 'subject', 'message']
    autocomplete_fields = ['related_project', 'assigned_to']
    readonly_fields = ['name', 'email', 'subject', 'message', 'submitted_at']


@admin.register(Partner)
class PartnerAdmin(admin.ModelAdmin):
    list_display = ['name', 'website', 'order']
    search_fields = ['name', 'website']

@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = ['title', 'date', 'related_project', 'related_event', 'order']
    search_fields = ['title', 'description']
    autocomplete_fields = ['related_project', 'related_event']
    filter_horizontal = ['participants']
    ordering = ['order', '-date']
    
admin.site.site_header = "ICAS Administration"
admin.site.site_title = "ICAS Admin"
admin.site.index_title = "Welcome to ICAS Admin Panel"
