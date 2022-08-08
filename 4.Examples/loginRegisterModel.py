from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
import bcrypt
from .models import User, Customer
from .utils import generate_token

def register(request):
    errors = User.objects.validator(request.POST)
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect('/')

    hashed_password = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
    user = User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], password=hashed_password, email=request.POST['email'])
    user.save()
    request.session['id'] = user.id
    return redirect('/success')

def login_user(request):
    # if (User.objects.filter(email=request.POST['login_email']).exists()):
    if (User.objects.filter(email=request.POST.get(['login_email', ""]).exists())):
        # user = User.objects.filter(email=request.POST.get(['login_email', ""]))[0]
        user = User.objects.filter(email=request.POST['login_email'])[0]
        if (bcrypt.checkpw(request.POST['login_email'].encode(), user.password.encode())):
        # if (bcrypt.checkpw(request.POST.get(['login_email', ""]).encode(), user.password.encode())):
            request.session['id'] = user.id
            return redirect('/success')
    return redirect('/')

def success(request):
    user = User.objects.get(id=request.session['id'])
    context = {
        "user": user
    }
    return render(request, 'authentication/success.html', context)


        # path('login', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    # path('logout', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
#     path('login_user/', views.login_user, name='login_user'),
#     path('logout_user/', auth.LogoutView.as_view(template_name='shop/body.html'),
#          name='logout_user'),
#     path('activate-user/<uidb64>/<token>',
#          views.activate_user, name='activate'),