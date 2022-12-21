from django.shortcuts import render
from .models import Course, Professor, Rating, Profile, User
from .forms import RatingForm
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

def home(request):
    return render(request, 'professors/home.html')

def course_ratings(request, course_id):
    if Course.objects.filter(id=course_id).first() is not None:
        course = Course.objects.get(id=course_id)
    else:
        return redirect('not_found')
    similarCourses = Course.objects.exclude(id=course_id).filter(subject=course.subject).filter(course_number=course.course_number)
    context = {
        'professor': course.professor.name,
        'school': course.school.name,
        'course': course.subject + course.course_number,
        'ratings': course.rating_set.all(),
        'similarCourses': similarCourses,
        'avgRating': course.getAverageRate()
    }
    return render(request, 'professors/course_ratings.html', context=context)

def search_prof(request, prof_name):
    profs = Professor.objects.filter(name__contains=prof_name)
    context = {'search_term': prof_name, 'results': profs}
    return render(request, 'professors/search_prof.html', context=context)

def search_course(request, subject, course_number):
    courses = Course.objects.filter(subject=subject).filter(course_number=course_number)
    return render(request, 'professors/search_course.html', context={'results': courses})

def search_subject(request, subject):
    courses = Course.objects.filter(subject=subject)
    return render(request, 'professors/search_course.html', context={'results': courses})

def prof_course(request, prof_id):
    if Professor.objects.filter(id=prof_id).first() is not None:
        professor = Professor.objects.get(id=prof_id)
    else:
        return redirect('not_found')
    professor = Professor.objects.get(id=prof_id)
    courses = Course.objects.filter(professor=professor)
    return render(request, 'professors/search_course.html', context={'results': courses})

def rating(request, course_id):
    if Course.objects.filter(id=course_id).first() is not None:
        course = Course.objects.get(id=course_id)
    else:
        return redirect('not_found')
    result = ''
    if request.method == "POST":
        form = RatingForm(request.POST)
        if form.is_valid():
            user = Profile.objects.get(user=request.user)
            Rating.objects.create(course=course, semester=request.POST['semester'], author=user, rate=request.POST['rate'], 
                                attendance=request.POST['attendance'], grade=request.POST['grade'], comment=request.POST['comment'])
            return redirect('course_ratings', course_id=course_id)
    grades = ['A+', 'A', 'A-', 'B+', 'B', 'B-', 'C+', 'C', 'C-', 'D', 'F', 'N', 'Other']
    
    context = {
        'course': course,
        'grades': grades,
        'result': result
    }
    return render(request, 'professors/rating.html', context=context)


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request,user)
                m = 'successfully logged in as ' + user.username
                messages.success(request, m)
                return redirect('home')
            else:
                messages.error(request, "Your account is disabled, try another account")
                return redirect('login')
        else:
            messages.error(request, "Sorry, we can't find your account. Please try again.")
            return redirect('login')
    return render(request, 'professors/login.html')

def signup(request):
    if request.method == "POST":
        name = request.POST['username']
        if User.objects.get(username=name) is None:
            user = User.objects.create(username=name, password=request.POST['password'])
            login(request, user)
            m = 'successfully signed in as ' + user.username
            messages.success(request, m)
            return redirect('home')
        else:
            m = 'username "' + name + '" is already used.'
            messages.error(request, m)
            return redirect('signup')
    
    return render(request, 'professors/signup.html')

def logout_view(request):
    logout(request)
    messages.info(request, 'You are logged out.')
    return redirect('home')
    

def profile(request, user_id):
    return render(request, 'professors/profile.html')

def profile_setting(request):
    return render(request, 'professors/profile_setting.html')


def signup_redirect(request):
    messages.error(request, "Something wrong here, it may be that you already have an account!")
    return redirect('home')


def not_found(request):
    return render(request, 'professors/notfound.html')