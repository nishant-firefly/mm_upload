from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required, user_passes_test
from .forms import UploadFileForm
from .models import UploadedFile

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            if user.is_staff:
                login(request, user)
                return redirect('upload_file')
            else:
                return render(request, 'fileupload_app/login.html', {'error': 'You do not have staff access.'})
        else:
            return render(request, 'fileupload_app/login.html', {'error': 'Invalid credentials'})
    return render(request, 'fileupload_app/login.html')

@login_required
@user_passes_test(lambda u: u.is_staff)
def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_file = UploadedFile(file=request.FILES['file'])
            uploaded_file.save()
            return redirect('upload_file')  # Redirect to avoid resubmission
    else:
        form = UploadFileForm()
    
    uploaded_files = UploadedFile.objects.all()
    return render(request, 'fileupload_app/upload.html', {'form': form, 'uploaded_files': uploaded_files})
