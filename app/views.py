from django.shortcuts import render
from app.models import Student
from django.http import HttpResponse
# Create your views here.

def welcome(request):
    return render(request,'welcome.html')

def register(request):
    if request.method == 'POST':
        name = request.POST['name']
        age = request.POST['age']
        email = request.POST['email']
        phone = request.POST['phone']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password != confirm_password:
            return HttpResponse("Passwords do not match")

        stu = Student()
        stu.name = name
        stu.age = age
        stu.email = email
        stu.phone = phone
        stu.password = password 
        stu.save()

        return render(request, 'success.html', {'name': name})

    return render(request, 'register.html')