from django.shortcuts import render, redirect
from django.contrib import auth


def login(request):
    if request.method == "POST":
        user = auth.authenticate(username=request.POST['email'], password=request.POST['password'])
        if user is not None:
            auth.login(request, user)
            return redirect('home')

        else:
            return render(request, 'accounts/login.html', {'error': str(type(user))})

    else:
        return render(request, 'accounts/login.html')

