from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import FileResponse, Http404
from .models import UploadedFile, UserProfile
from .forms import UploadFileForm, SignupForm
from django.contrib.auth.models import User


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            if User.objects.filter(username=form.cleaned_data['username']).exists():
                return render(request, 'core/signup.html', {'form': form, 'error': 'Username already exists'})
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            role = form.cleaned_data['role']
            UserProfile.objects.create(user=user, role=role)
            return redirect('login')
    else:
        form = SignupForm()
    return render(request, 'core/signup.html', {'form': form})


def custom_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            profile = UserProfile.objects.get(user=user)
            if profile.role == 'admin':
                return redirect('file_list')
            else:
                return redirect('upload')
        else:
            return render(request, 'core/login.html', {'error': 'Invalid credentials'})
    return render(request, 'core/login.html')

@login_required
def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_file = form.save(commit=False)
            uploaded_file.user = request.user
            uploaded_file.save()
            return redirect('upload')
    else:
        form = UploadFileForm()
    return render(request, 'core/upload.html', {'form': form})

@login_required
def file_list(request):
    files = UploadedFile.objects.all()
    return render(request, 'core/file_list.html', {'files': files})

@login_required
def download_file(request, file_id):
    try:
        uploaded_file = UploadedFile.objects.get(id=file_id)
        return FileResponse(uploaded_file.file.open(), as_attachment=True)
    except UploadedFile.DoesNotExist:
        raise Http404
