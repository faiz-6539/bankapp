from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import User

from .models import Register


# Create your views here.
def home(request):
    if 'user' in request.session:
        current_user = request.session['user']
        param = {'current_user': current_user}
        return render(request, 'base.html', param)

    else:
        return redirect('login')
    return render(request, 'login.html')


def signup(request):
    if request.method == 'POST':
        uname = request.POST.get('uname')
        pwd = request.POST.get('pwd')
        # print(uname, pwd)
        if User.objects.filter(username=uname).count() > 0:
            return HttpResponse('Username already exists.')
        else:
            user = User(username=uname, password=pwd)
            user.save()
            return redirect('login')
    else:
        return render(request, 'signup.html')


def login(request):
    if request.method == 'POST':
        uname = request.POST.get('uname')
        pwd = request.POST.get('pwd')

        check_user = User.objects.filter(username=uname, password=pwd)
        if check_user:
            request.session['user'] = uname
            return redirect('home')
        else:
            return HttpResponse('Please enter valid Username or Password.')

    return render(request, 'login.html')


def logout(request):
    try:
        del request.session['user']
    except:
        return redirect('login')
    return redirect('login')


def register(request):
    if request.method == 'POST':
        account = Register()
        account.name = request.POST['name']
        account.dob = request.POST['dob']
        account.age = request.POST['age']
        account.gender = request.POST['gender']
        account.phone_number = request.POST['phone']
        account.email = request.POST['email']
        account.address = request.POST['address']
        account.branch = request.POST['district']
        account.district = request.POST['branch']
        account.account_type = request.POST['account_type']
        account.materials_provided = request.POST['materials']
        account.save()
        return redirect('show')
    return render(request, 'register.html')

def show(request):
    return render(request, 'show.html')


