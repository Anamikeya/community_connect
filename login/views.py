from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth
from .models import posts,Selective_abortion_and_female_infanticide,Sexual_harassment, Dowry_and_Bride_burning,Disparity_in_education,Domestic_violence,Child_Marriages,Inadequate_Nutrition,Low_status_in_the_family,Inferiority,Status_of_widows
import smtplib
# Create your views here.
def start(request):
    return render(request,'home.html')
def login(request):
    if request.method=="POST":
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect("topics")
        else:
            messages.info(request,'invalid credentials')
            return redirect("login")
    else:
        return render(request,'login.html')


def register(request):
    if request.method == "POST":
        first_name=request.POST['first_name']
        last_name =request.POST['last_name']
        username=request.POST['username']
        password=request.POST['password']
        confirm_password=request.POST['confirm_password']
        email=request.POST['email']

        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'email taken')
                return redirect('register')
            else:

                user= User.objects.create_user(username=username,password=password,email=email,first_name=first_name,last_name=last_name)
                user.save();
                to = email
                content = "Hey!\n"+str(first_name)+"Thanks for registering with Familia lets have a happy drive towards future."
                servers = smtplib.SMTP('smtp.gmail.com',587)
                servers.ehlo()
                servers.starttls()
                servers.login('nayakpearl2@gmail.com','anamika05')
                servers.sendmail('nayakpearl2@gmail.com',to,content)
                servers.close()
                messages.info(request,"user created")
                return redirect('login')

            
        else:
            print("password didn't match")
            return redirect('register')
        return redirect('/')
    else:
        return render(request,'register.html')

def logout(request):
    auth.logout(request)
    return redirect("/")

def post(request):
    if request.method == 'POST':
        post = posts()
        post.Name = request.POST.get('name')
        post.About = request.POST.get('about')
        post.Body = request.POST.get('body')
        post.save()
        messages.info(request,"posted successfully")
        return redirect('post')
    else:

        return render(request,'post.html')

def public(request):
    cont = posts.objects.all()
    return render(request,"public2.html",{'cont':cont})

def topics(request):
    return render(request,'topics.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

def childMarriage(request):
    cm = Child_Marriages.objects.all()
    return render(request,"Child Marriages.html",{'cm':cm})

def DesparityinEducation(request):
    de = Disparity_in_education.objects.all()
    return render(request,"Desparity in Education.html",{'de':de})

def DomesticVoilence(request):
    dv = Domestic_violence.objects.all()
    return render(request,"Domestic Violence.html",{'dv':dv})

def DowryandBride(request):
    dabb = Dowry_and_Bride_burning.objects.all()
    return render(request,"Dowry and Bride Burning.html",{'dabb':dabb})

def FemaleInfanticide(request):
    fi =Selective_abortion_and_female_infanticide.objects.all()
    return render(request,"Selective abortion and female infanticide.html",{'fi':fi})

def Inferiority(request):
    inf = Inferiority.objects.all()
    return render(request,"inferiority.html",{'inf':inf})

def InadequateNutrition(request):
    nutrition = Inadequate_Nutrition.objects.all()
    return render(request,"Inadequate Nutrition.html",{'nutrition':nutrition})

def LowStatusInFamily(request):
    lsif = Low_status_in_the_family.objects.all()
    return render(request,"Low status in the family.html",{'lsif':lsif})

def SexualHarrasment(request):
    sh = Sexual_harassment.objects.all()
    return render(request,"sexual harassment.html",{'sh':sh})

def StatusOfWidow(request):
    sow= Status_of_widows.objects.all()
    return render(request,"Status of widows.html",{'sow':sow})

def post(request):
    if request.method == 'POST':
        post = posts()
        post.Name = request.POST.get('name')
        post.About = request.POST.get('about')
        post.Body = request.POST.get('body')
        post.save()
        messages.info(request,"posted successfully")
        return redirect('post')
    else:

        return render(request,'post.html')

def post(request):
    if request.method == 'POST':
        post = posts()
        post.Name = request.POST.get('name')
        post.About = request.POST.get('about')
        post.Body = request.POST.get('body')
        post.save()
        messages.info(request,"posted successfully")
        return redirect('post')
    else:

        return render(request,'post.html')

def fipost(request):
    if request.method == 'POST':
        post = posts()
        post.Name = request.POST.get('name')
        post.About = request.POST.get('about')
        post.Body = request.POST.get('body')
        post.save()
        messages.info(request,"posted successfully")
        return redirect('post')
    else:

        return render(request,'post.html')

def shpost(request):
    if request.method == 'POST':
        post = posts()
        post.Name = request.POST.get('name')
        post.About = request.POST.get('about')
        post.Body = request.POST.get('body')
        post.save()
        messages.info(request,"posted successfully")
        return redirect('post')
    else:

        return render(request,'post.html')

def dabbpost(request):
    if request.method == 'POST':
        post = posts()
        post.Name = request.POST.get('name')
        post.About = request.POST.get('about')
        post.Body = request.POST.get('body')
        post.save()
        messages.info(request,"posted successfully")
        return redirect('post')
    else:

        return render(request,'post.html')

def depost(request):
    if request.method == 'POST':
        post = posts()
        post.Name = request.POST.get('name')
        post.About = request.POST.get('about')
        post.Body = request.POST.get('body')
        post.save()
        messages.info(request,"posted successfully")
        return redirect('post')
    else:

        return render(request,'post.html')

def dvpost(request):
    if request.method == 'POST':
        post = posts()
        post.Name = request.POST.get('name')
        post.About = request.POST.get('about')
        post.Body = request.POST.get('body')
        post.save()
        messages.info(request,"posted successfully")
        return redirect('post')
    else:

        return render(request,'post.html')

def cmpost(request):
    if request.method == 'POST':
        post = posts()
        post.Name = request.POST.get('name')
        post.About = request.POST.get('about')
        post.Body = request.POST.get('body')
        post.save()
        messages.info(request,"posted successfully")
        return redirect('post')
    else:

        return render(request,'post.html')

def nutritionpost(request):
    if request.method == 'POST':
        post = posts()
        post.Name = request.POST.get('name')
        post.About = request.POST.get('about')
        post.Body = request.POST.get('body')
        post.save()
        messages.info(request,"posted successfully")
        return redirect('post')
    else:

        return render(request,'post.html')

def lsifpost(request):
    if request.method == 'POST':
        post = posts()
        post.Name = request.POST.get('name')
        post.About = request.POST.get('about')
        post.Body = request.POST.get('body')
        post.save()
        messages.info(request,"posted successfully")
        return redirect('post')
    else:

        return render(request,'post.html')

def infpost(request):
    if request.method == 'POST':
        post = posts()
        post.Name = request.POST.get('name')
        post.About = request.POST.get('about')
        post.Body = request.POST.get('body')
        post.save()
        messages.info(request,"posted successfully")
        return redirect('post')
    else:

        return render(request,'post.html')

def sowpost(request):
    if request.method == 'POST':
        post = posts()
        post.Name = request.POST.get('name')
        post.About = request.POST.get('about')
        post.Body = request.POST.get('body')
        post.save()
        messages.info(request,"posted successfully")
        return redirect('post')
    else:

        return render(request,'post.html')