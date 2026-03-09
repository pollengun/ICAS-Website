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
    ordering = ['order', 'name']


@admin.register(Publication)
class PublicationAdmin(admin.ModelAdmin):
    list_display = ['title', 'authors', 'pub_type', 'year']
    list_filter = ['pub_type', 'year']
    search_fields = ['title', 'authors']


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'status', 'start_date', 'funding_agency']
    list_filter = ['status']
    search_fields = ['title']


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ['title', 'event_type', 'date', 'venue', 'is_featured']
    list_filter = ['event_type', 'is_featured']


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['title', 'date_posted', 'is_featured']
    list_filter = ['is_featured']


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject', 'submitted_at', 'is_read']
    list_filter = ['is_read']
    readonly_fields = ['name', 'email', 'subject', 'message', 'submitted_at']


@admin.register(Partner)
class PartnerAdmin(admin.ModelAdmin):
    list_display = ['name', 'website', 'order']

@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = ['title', 'date', 'order']
    ordering = ['order', '-date']
    
admin.site.site_header = "ICAS Administration"
admin.site.site_title = "ICAS Admin"
admin.site.index_title = "Welcome to ICAS Admin Panel"
