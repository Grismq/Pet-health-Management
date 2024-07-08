from django.shortcuts import render,redirect
from User.models import PetHealthMonitoring
# Create your views here.
def login(request):
    if request.method == "POST":
        if request.method == "POST":
            usid = request.POST['uname']
            pswd = request.POST['psw']
            if usid == 'admin' and pswd == 'admin':
                return redirect('adminhome')

    return render(request,'adminlogin.html')

def adminhome(request):
    pet=PetHealthMonitoring.objects.all()
    return render(request,"adminhome.html",{"pet":pet})