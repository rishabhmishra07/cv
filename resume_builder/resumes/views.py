from django.shortcuts import render, redirect
from .forms import ResumeForm, SignupForm, LoginForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Resume

# Home View
def home(request):
    return render(request, "index.html")

# Signup View
def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()  # Save the user to the database
            messages.success(request, "Account created successfully!")
            return redirect('login')  # Redirect to login page
    else:
        form = SignupForm()
    return render(request, 'accounts/signup.html', {'form': form})

# Custom Login View







# Logout View
def user_logout(request):
    logout(request)
    return redirect('login')  # Redirect to login page after logout

# Resume Builder View
@login_required
def resume_build(request):
    return render(request, "resume_build")

# Resume Form View
@login_required 
def resume_form(request):
    template = request.GET.get("template", "template1")  # Defaults to template1 if not specified

    if request.method == "POST":
        form = ResumeForm(request.POST)
        if form.is_valid():
            resume = form.save(commit=False)
            resume.user = request.user  # Associate resume with the logged-in user
            resume.save()
            data = form.cleaned_data
            name = (form.cleaned_data["first_name"] + " " + form.cleaned_data["surname"]).title()
            skills = request.POST.getlist("skills")
            certifications = request.POST.getlist("certifications")
            languages = request.POST.getlist("languages")
            hobbies = request.POST.getlist("hobbies")

            return render(
                request,
                f"resume_templates/{template}.html",  # Adjusted directory name
                context={
                    "name": name,
                    "data": data,
                    "skills": skills,
                    "certifications": certifications,
                    "languages": languages,
                    "hobbies": hobbies,
                },
            )
    else:
        form = ResumeForm()
    return render(request, "resume_form.html", {"form": form})

def choose_template(request):
    # Get the selected template from the query parameter
    selected_template = request.GET.get('template', 'default_template')

    # Validate the selected template
    allowed_templates = [
        'template1', 'template2', 'template3', 'template4', 
        'template5', 'template6', 'template7', 'template8',
        'template9', 'template10', 'template11', 'template12',
        'template13', 'template14', 'template15'
    ]
    if selected_template not in allowed_templates:
        return redirect('fallback_view')  # Replace with a fallback or error view

    # Fetch user resume data (assuming logged-in user)
    user_resume = Resume.objects.filter(user=request.user).first()
    if not user_resume:
        return redirect('create_resume_view')  # Redirect to a page to create resume if none exists

    # Dynamically render the selected template
    return render(request, f'resume_templates/{selected_template}.html', {'resume': user_resume})
