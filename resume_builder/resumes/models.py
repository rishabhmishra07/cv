from django.contrib.auth.models import User
from django.db import models
from django.core.validators import RegexValidator, EmailValidator
from django.utils.timezone import now


class Resume(models.Model):
    EXPERIENCE_CHOICES = [
        ("fresher", "Fresher"),
        ("1", "1 Year"),
        ("2", "2 Years"),
        ("3", "3 Years"),
        ("4", "4 Years"),
        ("5plus", "5+ Years"),
    ]

    # Link to the built-in User model
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)


    # Personal Information
    first_name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100, blank=True, null=True)
    profession = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=10, default="00000")  # or any other default value

    
    phone = models.CharField(
        max_length=15,
        validators=[RegexValidator(r'^\+?1?\d{9,15}$', message="Enter a valid phone number.")],
    )
    email = models.EmailField(
        validators=[EmailValidator(message="Enter a valid email address.")]
    )
    linkedin_url = models.URLField(blank=True, null=True)
    github_url = models.URLField(blank=True, null=True)

    # Experience and Education
    experience = models.CharField(max_length=20, choices=EXPERIENCE_CHOICES)
    recent_company = models.CharField(max_length=100, blank=True, null=True)
    recent_duration = models.CharField(max_length=50, blank=True, null=True)
    school_name = models.CharField(max_length=100)
    school_marks = models.CharField(
        max_length=10,
        validators=[RegexValidator(r'^\d+(\.\d+)?$', message="Enter valid marks.")]
    )
    school_passing_year = models.CharField(
        max_length=4,
        validators=[RegexValidator(r'^\d{4}$', message="Enter a valid year.")],
    )
    college_name = models.CharField(max_length=100)
    college_marks = models.CharField(
        max_length=10,
        validators=[RegexValidator(r'^\d+(\.\d+)?$', message="Enter valid marks.")]
    )
    college_passing_year = models.CharField(
        max_length=4,
        validators=[RegexValidator(r'^\d{4}$', message="Enter a valid year.")],
    )

    # Skills and Other Details
    skills = models.JSONField(default=list)  # Store skills as a list
    certifications = models.JSONField(default=list)  # Store certifications as a list
    languages = models.JSONField(default=list)  # Store languages as a list
    hobbies = models.JSONField(default=list)  # Store hobbies as a list

    # Timestamps
    created_at = models.DateTimeField(default=now, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.surname} - {self.profession}"
