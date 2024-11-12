from django.shortcuts import render,redirect
from . forms import rgisterForm,update_profile
from django.contrib import messages,auth
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm,SetPasswordForm
from django.contrib.auth.decorators import login_required
# Create your views here.
def home(request):
    return render(request,'home.html')

#User Register method
def register(request):
    if request.method=="POST":
       form=rgisterForm(request.POST)
       if form.is_valid():
           form.save()
           messages.success(request,"Account Created Successfully")
           return redirect('login')
       else:
           messages.warning(request,"Something went wrong, Please try again")
           return redirect('register')

    form=rgisterForm()
    return render(request,'register.html',{'form':form, 'type':'Register'})

#User Login Method
def login(request):
    if request.method=="POST":
        form=AuthenticationForm(request,request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            user=auth.authenticate(username=username,password=password)
            if user is not None:
                auth.login(request,user)
                messages.success(request,"login Successfully")
                return redirect('profile')
            else:
                messages.warning(request,"Information Wrong. Try Again")
    form=AuthenticationForm()
    return render(request,'register.html',{'form':form, 'type':'Login'})
#user Logout Method
def  logout(request):
    auth.logout(request)
    messages.success(request,"Logout Successfully")
    return redirect('home')

#User profile Page
@login_required(login_url='/login/')
def profile(request):
    user=request.user
    return render(request,'profile.html',{'user':user})

#password Change with old Password
@login_required(login_url='/login/')
def change_pass(request):
    if request.method=="POST":
        form =PasswordChangeForm(request.user,request.POST)
        if form.is_valid():
            form.save()
            auth.update_session_auth_hash(request,form.user)
            messages.success(request,"Password Updated Successfully")
            return redirect('profile')
        else:
            messages.warning(request,"Something went wrong, Try again")
            return redirect('change_pass')
    form =PasswordChangeForm(request.user)
    return render(request,'register.html',{'form':form, 'type':'Password Change'})

#Change password without old password
@login_required(login_url='/login/')
def reset_pass(request):
    if request.method=="POST":
        form=SetPasswordForm(request.user,request.POST)
        if form.is_valid():
            form.save()
            auth.update_session_auth_hash(request,form.user)
            messages.success(request,"Password Updated Successfully")
            return redirect('profile')
        else:
             messages.warning(request,"Something went wrong, Try again")
             return redirect('reset_pass')

    form=SetPasswordForm(request.user)
    return render(request,'register.html',{'form':form, 'type':'Reset Password'})

#update profile
@login_required(login_url='/login/')
def edit_profile(request):
    if request.method=="POST":
        form=update_profile(request.POST,instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request,"Profile Updated Successfully")
            return redirect('profile')
        else:
            messages.warning(request,"Something went wrong, Try again")
            return redirect('edit_profile')
    form=update_profile(instance=request.user)
    return render(request,'register.html',{'form':form, 'type':'Edit Profile'})