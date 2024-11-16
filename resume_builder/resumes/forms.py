from django import forms
from .models import Resume
from django.contrib.auth.models import User

# Signup Form
class SignupForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password != confirm_password:
            raise forms.ValidationError("Passwords do not match!")
        return cleaned_data

# Login Form
class LoginForm(forms.Form):
    username = forms.CharField(max_length=150, required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)

# Resume Form
class ResumeForm(forms.ModelForm):
    class Meta:
        model = Resume
        fields = [
            "first_name",
            "surname",
            "profession",
            "city",
            "country",
            "postal_code",
            "phone",
            "email", 
            "linkedin_url",
            "github_url",
            "experience",
            "recent_company",
            "recent_duration",
            "school_name",
            "school_marks",
            "school_passing_year",
            "college_name",
            "college_marks",
            "college_passing_year",
            "skills",
            "certifications",
            "languages",
            "hobbies",
        ]
        widgets = {
            "experience": forms.Select(
                attrs={
                    "id": "experience",
                    "class": "form-control",
                }
            ),
        }

    def clean_skills(self):
        skills = self.cleaned_data.get("skills")
        if isinstance(skills, str):
            return [skills]
        return skills

    def clean_certifications(self):
        certifications = self.cleaned_data.get("certifications")
        if isinstance(certifications, str):
            return [certifications]
        return certifications

    def clean_languages(self):
        languages = self.cleaned_data.get("languages")
        if isinstance(languages, str):
            return [languages]
        return languages

    def clean_hobbies(self):
        hobbies = self.cleaned_data.get("hobbies")
        if isinstance(hobbies, str):
            return [hobbies]
        return hobbies

    # Override to use widget attributes like 'required' and 'multiple input fields'.
    skills = forms.CharField(
        widget=forms.TextInput(attrs={"class": "skill"}), required=True
    )
    certifications = forms.CharField(
        widget=forms.TextInput(attrs={"class": "certification"}), required=True
    )
    languages = forms.CharField(
        widget=forms.TextInput(attrs={"class": "language"}), required=True
    )
    hobbies = forms.CharField(
        widget=forms.TextInput(attrs={"class": "hobby"}), required=True
    )

    def __init__(self, *args, **kwargs):
        super(ResumeForm, self).__init__(*args, **kwargs)
        self.fields["school_name"].label = "School Name (12th)"
        self.fields["school_marks"].label = "Marks"
        self.fields["school_passing_year"].label = "Year of Graduation"
        self.fields["college_passing_year"].label = "Year of Graduation"
        self.fields["college_name"].label = "College Name (Grad)"
        self.fields["college_marks"].label = "Marks"
        self.fields["first_name"].widget.attrs.update({"id": "first-name"})
        self.fields["surname"].widget.attrs.update({"id": "surname"})
        self.fields["profession"].widget.attrs.update({"id": "profession"})
        self.fields["city"].widget.attrs.update({"id": "city"})
        self.fields["country"].widget.attrs.update({"id": "country"})
        self.fields["postal_code"].widget.attrs.update({"id": "postal-code"})
        self.fields["phone"].widget.attrs.update({"id": "phone"})
        self.fields["email"].widget.attrs.update({"id": "email"})
        self.fields["linkedin_url"].widget.attrs.update({"id": "linkedin-url"})
        self.fields["github_url"].widget.attrs.update({"id": "github-url"})
        self.fields["experience"].widget.attrs.update({"id": "experience"})
        self.fields["recent_company"].widget.attrs.update({"id": "recent-company"})
        self.fields["recent_duration"].widget.attrs.update({"id": "recent-duration"})
        self.fields["school_name"].widget.attrs.update({"id": "school-name"})
        self.fields["school_marks"].widget.attrs.update({"id": "school-marks"})
        self.fields["school_passing_year"].widget.attrs.update({"id": "school-year"})
        self.fields["college_name"].widget.attrs.update({"id": "college-name"})
        self.fields["college_marks"].widget.attrs.update({"id": "college-marks"})
        self.fields["college_passing_year"].widget.attrs.update({"id": "college-year"})
        self.fields["skills"].widget.attrs.update(
            {
                "placeholder": "Enter your skills",
                "class": "skill",
                "id": "skill",
                "name": "skills[]",
            }
        )
        self.fields["certifications"].widget.attrs.update(
            {
                "placeholder": "Enter your certifications",
                "class": "certification",
                "id": "certification",
                "name": "certifications[]",
            }
        )
        self.fields["languages"].widget.attrs.update(
            {
                "placeholder": "Enter languages you know",
                "class": "language",
                "id": "language",
                "name": "languages[]",
            }
        )
        self.fields["hobbies"].widget.attrs.update(
            {
                "placeholder": "Enter your hobbies",
                "class": "hobby",
                "id": "hobby",
                "name": "hobbies[]",
            }
        )
