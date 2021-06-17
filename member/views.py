from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import UserRegisterForm


# User register view
def user_register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, 'Account successfully created for ' + username + ' !')
            return redirect('radio:index')
    else:
        form = UserRegisterForm()
    return render(request, 'registration/register.html', {'form': form})




