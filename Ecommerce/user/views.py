from pyexpat.errors import messages
from django.shortcuts import render,redirect
from user.models import Profile
from user.forms import UserForm,ProfileForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,logout,login as auth_login
from django.contrib.auth.decorators import login_required



# Create your views here.
def home(request):
    return render(request,'user/sample.html')
def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            try:
                profile = Profile.objects.get(user=user)
            except Profile.DoesNotExist:
                # Handle the case where the profile does not exist
                profile = None
                messages.error(request, "Profile does not exist for this user.")
                return redirect('user:login')

            auth_login(request, user)
            if profile.consumer:
                return redirect('website:homepage')
            else:
                return redirect('product:sellerview')
        else:
            messages.error(request, "Invalid username or password.")
            return redirect('user:login')
    else:

        return render(request,'user/login.html')


def signup(request):
    if request.method=="POST":
        userform=UserForm(request.POST)
        profileform=ProfileForm(request.POST)
        if userform.is_valid() and profileform.is_valid():
            username = userform.cleaned_data['username']
            email = userform.cleaned_data['email']
            password = userform.cleaned_data['password']
            consumer = profileform.cleaned_data['consumer']
            seller = profileform.cleaned_data['seller']

            if User.objects.filter(username=username).exists():
                return render(request, 'signup.html', {'error': 'Username already exists.', 'user_form': user_form, 'profile_form': profile_form})

            user = User.objects.create_user(username=username, email=email, password=password)
            profile = Profile.objects.create(user=user, consumer=consumer, seller=seller)
            auth_login(request, user)
            return redirect('user:login')

    else:
        userform=UserForm(request.POST)
        profileform=ProfileForm(request.POST)
    return render(request,'user/signup.html',{'userform':userform,'profileform':profileform})

@login_required
def logout_view(request):
    logout(request)
    return redirect('user:login')