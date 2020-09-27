from django.shortcuts import render,redirect
from .models import Apply
from django.contrib.auth.models import User,auth
from .models import Signup1
from .models import Post
from .models import Contact

from django.db import IntegrityError



from django.shortcuts import render
from .forms import Signup1form,Loginform
from django.contrib.auth.forms import AuthenticationForm 

from django.contrib.auth.models import User,auth
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
# Create your views here.

def index(request):
    return render(request,"index.html")

def apply(request):
    
    app=Apply.objects.all()
    paginator = Paginator(app, 4)
    page_number = request.GET.get('page')
    try:
        app = paginator.page(page_number)
    except PageNotAnInteger:
        app = paginator.page(1)
    except EmptyPage:
        app = paginator.page(paginator.num_pages)

    return render(request,"apply.html",{'app': app})

def welcome(request):
    count= Post.objects.all().count()
    
    
    
    app1 = Signup1.objects.filter(user=request.user)
    

    if request.method == 'POST':
        try:
            post = Post()
            post.title = request.POST.get('title')
            post.save()
            messages.info(request,' Apply Successfully!')

            return render(request, 'thanks.html',{'count': count})  

        except IntegrityError as e:
            e = 'You Allready Apply'
            return render(request, "thanks.html",context={ 'e': e,'count': count})



       
        
     

    
    
    
     
    return render(request, 'welcome.html',{'app1': app1})

def thanks(request):
        
    
    return render(request, 'thanks.html')

    


def signup(request):
    username=''
    first_name=''
    last_name=''

    password1=''
    password2=''
    date=''
    gender=''
    college=''
    qualification=''
    email=''
    mobile=''
    city=''
    address=''

    
    form= Signup1form(request.POST or None)
    if form.is_valid():
        fs= form.save(commit=False)
        username= form.cleaned_data.get("username")
        first_name= form.cleaned_data.get("first_name")
        last_name= form.cleaned_data.get("last_name")

        password1= form.cleaned_data.get("password1")
        password2= form.cleaned_data.get("password2")
        Birth_date= form.cleaned_data.get("Birth_date")
        gender= form.cleaned_data.get("gender")
        college= form.cleaned_data.get("college")
        qualification= form.cleaned_data.get("qualification")
        email= form.cleaned_data.get("email")
        mobile= form.cleaned_data.get("mobile")
        city= form.cleaned_data.get("city")
        address= form.cleaned_data.get("address")

        if password1==password2:
            try:
                user= User.objects.get(username=username) #if able to get, user exists and must try another username
                context= {'form': form, 'error':'The username you entered has already been taken. Please try another username.'}
                return render(request, 'signup.html', context)
            except User.DoesNotExist:
                user= User.objects.create_user(username, password= password1,first_name=first_name,last_name=last_name,
                                           email=email)
                user1=Signup1(username=username, password1= password1,password2=password2,first_name=first_name,last_name=last_name,email=email,mobile=mobile,college=college,qualification=qualification,address=address,gender=gender,city=city,Birth_date=Birth_date,user=user)
                user1.save()
                

                
                auth.login(request,user)

                context= {'form': form}
                messages.info(request, 'save successfully')
                return render(request, 'signup.html', context)
               
            
        else:
            context= {'form': form, 'error':'The passwords that you provided don\'t match'}
            return render(request, 'signup.html', context)
        

    else:
        context= {'form': form}
        return render(request, 'signup.html', context)






def signin(request):
    if request.method == 'POST': 
   
        # AuthenticationForm_can_also_be_used__ 
   
        username = request.POST['username'] 
        password = request.POST['password'] 

        user = auth.authenticate(username=username,password=password) 
        if user is not None: 
            auth.login(request, user)
            
            return redirect('/') 
        else: 
            messages.info(request,'Invalid ') 
            return redirect('signin')
    else:
        return render(request,'signin.html')
    
def logout(request):
    auth.logout(request)
    return redirect('/') 

def about(request):
    return render(request,"about.html")

def contact(request):
    
    if request.method == 'POST':
            if request.POST.get('name') and request.POST.get('email') and request.POST.get('mobile') and request.POST.get('college') and request.POST.get('subject') and request.POST.get('feedback'):
                post=Contact()
                post.name= request.POST.get('name')
                post.email= request.POST.get('email')
                post.mobile= request.POST.get('mobile')
                post.college= request.POST.get('college')

                post.subject= request.POST.get('subject')
                post.feedback= request.POST.get('feedback')

                post.save()
                
                messages.info(request,'Thank you for your feedback  ') 

                return render(request, 'contact.html')  

    else:
                return render(request,"contact.html")

    
    



