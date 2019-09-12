from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User, auth
from home.models import Attendance, Subjects
# Create your views here.
def index(request):
    users = User.objects.all()
    return render(request, 'login_bagl.html', {'users' : users})

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        firstname = request.POST['first_name']

        user = User.objects.create_user(username = username, password= password, email= email, first_name = firstname)
        user.save()
        return redirect('/')

    else:
        return render(request, 'register_bagl.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username = username, password = password)

        if user is not None:
            auth.login(request, user)
            
            user = User.objects.get(username = username)
            attendance = Attendance.objects.filter(student_id = user.id)
            return render(request, 'profile.html', {'user' : user, 'attendance' : attendance})

        else:
            return redirect('/')

    else:
        return render(request, 'login_bagl.html')

def faculty_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username = username, password = password)

        if user is not None:
            auth.login(request, user)
            
            user = User.objects.get(username = username)
            return render(request, 'faculty_profile.html')

        else:
            return redirect('/')

    else:
        return render(request, 'index.html')


def attend(request):
    if request.method == 'GET':
        username = request.POST.get('username')
        print(username)
        user = User.objects.get(username = str(username))
        attendance = Attendance.objects.filter(student_id = user.id)
        return render(request, 'profile_attendance.html',{'user' : user, 'attendance' : attendance})

