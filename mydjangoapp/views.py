from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpRequest
from .myForm import StudentRegistration
from .forms import DetailedForm ,EditProfileForm
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, SetPasswordForm,UserChangeForm
from django.contrib.auth import authenticate, login, logout ,update_session_auth_hash
from django.contrib import messages


def signupView(request):
    if request.method == 'POST':
        form = DetailedForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/registration/')
    else:
        print(request.POST)
        form = DetailedForm()
        print('data is not saved==>')
    return render(request, 'signupform.html', {'form': form})


def loginView(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            fm = AuthenticationForm(request=request, data=request.POST)
            if fm.is_valid():
                uname = fm.cleaned_data['username']
                upass = fm.cleaned_data['password']
                user = authenticate(username=uname, password=upass)
                if user is not None:
                    login(request, user)
                    messages.success(request, 'Logged in Successfully')
                    return HttpResponseRedirect('/profile/')
        else:
            fm = AuthenticationForm()
        return render(request, 'loginFormTemplate.html', {'form': fm})
    else:
        return HttpResponseRedirect('/profile/')



def logoutView(request):
    logout(request)
    return HttpResponseRedirect('/loginform/')

def changePassView(request):
    if  request.user.is_authenticated:
        if request.method == "POST":
            fm = PasswordChangeForm(user=request.user, data=request.POST)
            if fm.is_valid():
                fm.save()
                update_session_auth_hash(request,fm.user)
                return HttpResponseRedirect('/profile/')
        else:
            fm = PasswordChangeForm(user=request.user)
        return render(request,'changePassTemplate.html',{'form':fm})
    else:
        return HttpResponseRedirect('/loginform/')    
    
# Change password without old password
# def changePassViewW(request):
#     if  request.user.is_authenticated:
#         if request.method == "POST":
#             fm = SetPasswordForm(user=request.user, data=request.POST)
#             if fm.is_valid():
#                 fm.save()
#                 update_session_auth_hash(request,fm.user)
#                 return HttpResponseRedirect('/profile/')
#         else:
#             fm = SetPasswordForm(user=request.user)
#         return render(request,'changePassTemplateW.html',{'form':fm})
#     else:
#         return HttpResponseRedirect('/loginform/')    



def user_profile(request):
    if request.user.is_authenticated:
        if  request.method == "POST":
            fm = EditProfileForm(request.POST, instance=request.user)
            if fm.is_valid():
                fm.save()
                return HttpResponseRedirect('/profile/')

        else:
            fm = EditProfileForm(instance=request.user) 
        return render(request, 'profileTemplate.html', {'name': request.user, 'editform':fm})
    else:
        return HttpResponseRedirect('/loginform/')


def hellodjango(request):
    return HttpResponse('<h2>Hello to the world of Django</h2>')


def hellocs(request):
    return HttpResponse('<h2>Hello to the world of programming</h2>')


def hellotemplate(request):
    return render(request, 'display.html')


def mydashboard(request):
    return render(request, 'dashboard.html')


def myproducts(request):
    return render(request, 'products.html')


def mymain(request):
    return render(request, 'main.html')


def mycustomers(request):
    name = 'muhammad asad ali',
    address = 'House 9/1 sheet 23 model colony',
    contact = '03152140860'
    hobbies = 'sports, cricket, reading, nasa'
    customer_info = {'nm': name, 'cn': contact, 'add': address, 'hb': hobbies}
    return render(request, 'customers.html', context=customer_info)


def myForm(request):
    fm = StudentRegistration(auto_id=True, initial={
                             'name': 'Asad', 'email': 'abc@yahoo.com'})
    fm.order_fields(field_order=['email', 'name'])
    return render(request, 'formTemplate.html', {'myform': fm})
