# Django class
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import (
    authenticate,
    login,
    logout
)

# models django
from django.contrib.auth.models import User
from django.db.utils import IntegrityError

# my models
from users.models import myUser


def login_view(request):
    """ view for user log in the app
    """
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user:
            login(request, user)
            request.session['user'] = user.get_full_name()
            request.session['id'] = user.id
            # import pdb; pdb.set_trace()
            return redirect('post')
        else:
            return render(request,
                          'users/login.html',
                          {'error': 'Invalid username or password'})

    return render(request, 'users/login.html')


def signup_view(request):
    """ view and check some info for users
    can be register within app
    """
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['passwd']
        passwd_confirmation = request.POST['passwd_confirmation']

        if password != passwd_confirmation:
            return render(request,
                          'users/signup.html',
                          {'error': 'password confirmation doesn\'t match'})
        try:
            user = User.objects.create_user(username=username,
                                            password=password)
        except IntegrityError:
            return render(request,
                          'users/signup.html',
                          {'error': 'Username already exists'})

        user.first_name = request.POST['first_name']
        user.last_name = request.POST['last_name']
        user.email = request.POST['email']
        user.save()
        author = myUser(user=user)
        admin = request.POST.get('admin', False)
        if admin == 'on':
            author.is_admin = True
        author.save()

        return redirect('login')

    return render(request, 'users/signup.html')

@login_required(login_url='/login/')
def logout_view(request):
    """ Logout to user
    """
    logout(request)
    return redirect('login')
