from django.shortcuts import render,redirect
from App1.LoginForms import Login,Signup,User
from App1.models import SignupModels,UserModels
from django.contrib.auth import get_user_model

# Create your views here.
def home(request):
    return render(request,"home.html")

def login(request):
    title = "Login"
    txt = ""
    forms = Login(request.POST or None)
    if request.method == "POST":
        forms = Login(request.POST)
        if forms.is_valid():
            email = forms.cleaned_data["email"]
            password = forms.cleaned_data["password"]
            query = SignupModels.objects.filter(memail = email)
            if query.exists():
                query = SignupModels.objects.filter(memail = email, mpassword = password)
                if query.exists():
                    request.session['email'] = email
                    return redirect('user_home')
                else:
                    txt = "Incorrect Password"
                    return render(request,"txt.html",{"txt":txt,"title":title})
            else:
                txt = "You are not Registered here"
                return render(request,"sign.html",{"txt":txt})
    return render(request,"login.html",{"forms":forms})

def signup(request):
    title  = "Signup"
    txt = ""
    forms = Signup(request.POST or None)
    if request.method == "POST":
        forms = Signup(request.POST)
        if forms.is_valid():
            email = forms.cleaned_data["email"]
            pass1 = forms.cleaned_data["pass1"]
            pass2 = forms.cleaned_data["pass2"]
            if (pass1==pass2):
                m = SignupModels(memail = email, mpassword = pass1)
                m.save()
                txt = "Registered Successfully"
            else:
                txt = "Incorrect Password"
    return render(request,"signup.html",{"forms":forms,"txt":txt,"title":title})

def user(request):
    email = request.session.get('email')
    query = UserModels.objects.filter(memail = email)
    if query.exists():
        return render(request,"userhome.html",{"query":query})
    else:
        forms = User(request.POST or None)
        if request.method == "POST":
            forms = User(request.POST)
            if forms.is_valid():
                txt = "Saved the Details"
                name = forms.cleaned_data["name"]
                age = forms.cleaned_data["age"]
                gender = forms.cleaned_data["gender"]
                country = forms.cleaned_data["country"]
                phone = forms.cleaned_data["phone"]
                m = UserModels(memail=email,mname=name,mage=age,mgender=gender,mcountry=country,mphone=phone)
                m.save()
                return render(request,"txt.html",{"txt":txt})
        return render(request,"user.html",{"forms":forms})
