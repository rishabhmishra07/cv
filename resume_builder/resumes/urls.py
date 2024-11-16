
from django.urls import path
from resumes import views
from django.contrib.auth import views as auth_views  # Importing Django's auth views

urlpatterns = [
    path("", views.home, name="home"),  # Homepage
    path("signup/", views.signup, name="signup"),  # Signup view
    path("login/", auth_views.LoginView.as_view(template_name="accounts/login.html"), name="login"),  # Login view
    path("logout/", auth_views.LogoutView.as_view(next_page='login'), name="logout"),  # Logout view
    path("resume_build/", views.resume_build, name="resume_build"),  # Resume builder page
    path("resume_form/", views.resume_form, name="resume_form"),  # Form for creating resumes
    path('choose_template/', views.choose_template, name='choose_template'),
]

    


    
    







    
    


