
from django.shortcuts import render,redirect
from django.contrib import messages
from django.shortcuts import HttpResponse
from . models import Register
from . forms import RegisterForm,LoginForm 


from app7.forms import RegisterForm
# Create your views here.
def hello (request):
    return HttpResponse ("Welcome to Django")
def index(request):
    name = 'Junaid'
    return render(request,'index.html',{'content': name})
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST or None,request.FILES or None)
        if form.is_valid():
            name=form.cleaned_data['Name']
            age=form.cleaned_data['Age']
            place=form.cleaned_data['Place']
            email=form.cleaned_data['Email']
            photo = form.cleaned_data["Photo"]
            password=form.cleaned_data['Password']
            cpassword=form.cleaned_data['ConfirmPassword']
            
            user=Register.objects.filter(Email=email).exists()
            if user:
                messages.warning(request,"Email already exists...")
                return redirect('/register')
            elif password!=cpassword:
                messages.warning(request,"Password mismatch")
                return redirect('/register')
            else:
                tab=Register(Name=name,Age=age,Place=place,Photo = photo,Email=email,Password=password)
                tab.save()
                messages.success(request, "Your response have been recorded")
                return redirect('/')
    else :
        form = RegisterForm()
    return render(request,'register.html',{'data': form })
def login(request):
    if request.method =="POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['Email']
            password = form.cleaned_data['Password']
            
            user = Register.objects.get(Email = email)
            if not user:
                messages.warning(request,"user does not exists")
                return redirect('/login')
            elif password!=user.Password:
                messages.warning(request,"incorrect password")
                return redirect('/login')
            else:
                messages.success(request,"login successfull")
                return redirect('/home/%s' % user.id)
    else :
        form = LoginForm()
    return render(request,'login.html',{'data': form })
            
def home(request,id):
      data=Register.objects.get(id=id)
      return render(request,'home.html',{'data':data})      