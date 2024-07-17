from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .forms import UploadFileForm
from .models import UploadedFile

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('upload_file')
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    return render(request, 'login.html')

@login_required
def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_file = UploadedFile(file=request.FILES['file'])
            uploaded_file.save()
            return render(request, 'upload.html', {'success': 'File uploaded successfully'})
    else:
        form = UploadFileForm()
    return render(request, 'upload.html', {'form': form})
