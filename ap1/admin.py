from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display=("name","description")
    search_fields=("name",)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display=("name","description")
    search_fields=("name",)

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display=("name","duration")
    search_fields=("name","duration")

@admin.register(Achievement)
class AchievementAdmin(admin.ModelAdmin):
    list_display=("id","image",)

@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display=("name","description")
    search_fields=("name","description")

@admin.register(Notice)
class NoticeAdmin(admin.ModelAdmin):
    list_display = ("title", "date","description")
    search_fields = ("title",)
    list_filter = ("date",)

@admin.register(Certification)
class CertificationAdmin(admin.ModelAdmin):
    list_display = ("name", "description")
    search_fields = ("name",)

@admin.register(Patent)
class PatentAdmin(admin.ModelAdmin):
    list_display = ("name","description")
    search_fields = ("name",)

@admin.register(Founder)
class FounderAdmin(admin.ModelAdmin):
    list_display = ("name", "role","bio")
    search_fields = ("name", "role")

@admin.register(CoreTeam)
class CoreTeamAdmin(admin.ModelAdmin):
    list_display = ("name", "role","bio")
    search_fields = ("name", "role")

@admin.register(TechTeam)
class TechTeamAdmin(admin.ModelAdmin):
    list_display = ("name", "role","bio")
    search_fields = ("name", "role")

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "phone", "submitted_at")
    search_fields = ("name", "email", "phone")
    list_filter = ("submitted_at",)



@admin.register(JobOpening)
class JobOpeningAdmin(admin.ModelAdmin):
    list_display = ("title", "posted_at","description")
    search_fields = ("title",)
    list_filter = ("posted_at",)



@admin.register(JobApplication)
class JobApplicationAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "job", "submitted_at")
    search_fields = ("name", "email",)
    list_filter = ("submitted_at", "job")