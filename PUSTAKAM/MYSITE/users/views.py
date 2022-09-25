from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm,UserUpdateForm,ProfileUpdateForm
from django.template import loader
from django.contrib.auth.decorators import login_required
from .forms import FeedbackForm
from .models import feedback
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods



def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f'Congratulations {username} ! Your account has been created. Now you can log in.')
            return redirect('login')
    else:
        form =UserRegisterForm()
            
    return render(request, 'users/register.html', {'form': form})

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'users/profile.html', context)


def review(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            First_Name = form.cleaned_data.get('First_Name')
            messages.success(request,f'Congratulations {First_Name} ! Your Feedback has been accepted.')
            return redirect('thankyou')
    else:
        form =FeedbackForm()
    return render(request, 'users/cust_review.html', {'form': form})


def thankyou(request):
     return render(request, 'users/thankyou.html')



    
    
def showfeedback(request):
	feedbacks=feedback.objects.all()#fetches all feedback from table
	return render(request,'users/showfeedbacks.html',{'feedbacks':feedbacks})
    
