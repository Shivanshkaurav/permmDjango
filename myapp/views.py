from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from .models import *
from django.contrib.auth.decorators import login_required

def index_page(request):
    return render(request, 'myapp/index.html') 

def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is None:
            return redirect('login') 
        else:
            login(request, user)
            return redirect('/home/')
        
    return render(request, 'myapp/login.html')

def signup_page(request):
    if request.method == 'POST':
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = CustomUser.objects.filter(username = username)
        if user.exists():
            return redirect('signup')
           
        user = CustomUser.objects.filter(email = email)
        if user.exists():
            return redirect('signup')
        else:
            user = CustomUser.objects.create(
                first_name = firstname,
                last_name = lastname,
                email = email,
                username = username,
            )
            user.set_password(password)
            user.save()
            return redirect('login')
        
    return render(request, 'myapp/signup.html')

@login_required
def home_page(request):
    user = request.user.first_name
    list = Student.objects.all()
    permissions = request.user.get_all_permissions()  # Get the user's permissions
    context = {
        'user': user,
        'list': list,
        'permissions': permissions,
    }
    return render(request, 'myapp/home.html', context)

@login_required
def update_page(request, id):
    student = get_object_or_404(Student, id=id)
    if request.method == 'POST':
        student.name = request.POST.get('name')
        student.roll = request.POST.get('roll')
        student.city = request.POST.get('city')
        student.profile_pic = request.FILES.get('profile_pic')
        student.save()
        return redirect('/home/')
    
    return render(request, 'myapp/update.html', {'student': student})

def delete_page(request, id):
    student = get_object_or_404(Student, id=id)
    student.delete()
    return redirect('/home/')

def logout_page(request):
    logout(request)
    return redirect('index')

def add_student(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        roll = request.POST.get('roll')
        city = request.POST.get('city')
        profile_pic = request.FILES.get('profile_pic')
        student = Student(name=name, roll=roll, city=city, profile_pic=profile_pic)
        student.save()
        print("student created")
        return redirect('/home/')

    return render(request, 'myapp/add-student.html')