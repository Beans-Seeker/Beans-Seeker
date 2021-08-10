from django.contrib import auth, messages
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

def login_view(request):
    if request.method == 'POST': # 입력이 들어오는 경우
        id = request.POST['id']
        password = request.POST['password']
        user = authenticate(request=request, username=id, password=password)
        if user is not None: # 유저가 있는 경우
            login(request, user)
        else: # 유저가 없는 경우 에러 메세지 띄우기
            return render(request, 'login.html', {'error':'true'})
            # messages.warning(request, '사용자 정보가 없습니다')
        return render(request, 'main.html', {'user':user})
    else: 
        return render(request, 'login.html')

def register_view(request):
    if request.method == 'POST':  
        id = request.POST['id']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1 == password2 :
            new_user = User.objects.create_user(username = id, password=password1)
            auth.login(request, new_user)
        else: # 비밀번호 확인에서 오류 난 경우
            return render(request, 'register.html', {'error':'true'})
        return render(request, 'main.html', {'user':new_user})
    else:
        return render(request, 'register.html')

def logout_view(request):
    logout(request)
    return render(request, 'main.html')

