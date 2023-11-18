from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from .forms import NewUserForm
from django.contrib.auth import login
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render
from .models import Files
from django.shortcuts import render, redirect

# Create your views here.
def sus(request):
    return render(request, 'main/index.html')

def Login(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return render(request, 'main/profile.html')
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="main/login.html", context={"login_form":form})

def register(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return render(request, 'main/Main.html')
        else:
            return render(request, 'main/registration.html', {'register_form': form})
    form = NewUserForm()
    return render(request, 'main/registration.html', {'register_form': form})


def upload_file(request):
	if request.method == 'POST' and request.FILES['myfile']:
		file = request.FILEs['documents']
		fileSystem = FileSystemStorage()
		filename = fileSystem.save(file.name, file)
		file_url = fileSystem.url(filename)
		return render(request, 'main/index.html', {'file_url':file_url})
	return render(request, 'main/index.html')

def file_show(request):
	object_list = Files.objects.all()
	return render(request, 'main/show.html', {'object_list': object_list})

# def thanks_page(request):
# 	name = request.GET['name']
# 	phone = request.get['phone']
# 	return render(request, './thanks_page.html', {'name': name, 'phone': phone})