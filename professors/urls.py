from django.urls import path
from . import views

urlpatterns = [
    path('social/signup/', views.signup_redirect, name='signup_redirect'),
    path('', views.home, name='home'),
    path('courseid=<int:course_id>/', views.course_ratings, name='course_ratings'),
    path('search/prof=<str:prof_name>/', views.search_prof, name='search_prof'),
    path('search/subject=<str:subject>/number=<str:course_number>/', views.search_course, name='search_course'),
    path('search/subject=<str:subject>/', views.search_subject, name='search_subject'),
    path('course/profid=<int:prof_id>/', views.prof_course, name='prof_course'),
    path('rating/courseid=<str:course_id>/', views.rating, name='rating'),
    path('delete/<int:id>/', views.delete_rating, name='delete_rating'),
    path('edit/<int:id>/', views.edit_rating, name='edit_rating'),
    
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/<str:username>/', views.profile, name='profile'),
]
