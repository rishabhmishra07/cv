from django.contrib import admin
from .models import Resume

# Custom Admin for Resume model
class ResumeAdmin(admin.ModelAdmin):
    list_display = [
        'first_name', 'surname', 'profession', 'city', 'country', 'postal_code', 'phone', 'email', 'linkedin_url',
        'github_url', 'experience', 'recent_company', 'recent_duration', 'school_name', 'school_marks',
        'school_passing_year', 'college_name', 'college_marks', 'college_passing_year', 'skills',
        'certifications', 'languages', 'hobbies', 'created_at', 'updated_at'
    ]

admin.site.register(Resume, ResumeAdmin)

