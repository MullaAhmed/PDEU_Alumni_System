from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import logout, login
# Create your views here.
from Students.models import *
from Students.forms import *
import uuid

# Create your views here.


def student_home(request):
      return render(request,"student_home.html")

def about(request):
      return render(request,"about.html")

def alumni(request):
      alumni1=Profile.objects.all()
      return render(request,"alumni.html",{"alumni":alumni1})

def announcement(request):
      announcement1=Announcements.objects.all()
      Placement1=Placements.objects.all()
      return render(request,"Announcements.html",{"announcements":announcement1,"placements":Placement1})

def contact(request):
      return render(request,"contact.html")
def chat_box(request):
      chatbox=ChatBox.objects.all()
      form=sendmessage(request.POST)
      if request.method == "POST":
            
            if form.is_valid():
                  n=form.cleaned_data["name"]
                  b=form.cleaned_data["body"]

                  a=ChatBox(name=n,body=b)
                  a.save()
            
                  return render(request,"chat_box.html",{"form":form,"chatbox":chatbox})
            else:
                  return render(request,"chat_box.html",{"form":form,"chatbox":chatbox})
      else:
            return render(request,"chat_box.html",{"form":form,"chatbox":chatbox})

@csrf_exempt
def login_attempt(request):
      if request.method == 'POST':
            #Sign UP
            email = request.POST.get('email_s')
            name = request.POST.get('name_s')
            password1 = request.POST.get('password1_s')
            number=request.POST.get('number_s')

         
            
            check_user = User.objects.filter(email = email).first()
                  
            if check_user :
                        context = {'message' : 'User already exists' , 'class' : 'danger' }
                        return render(request,'login.html' , context)

                  
            user = User(username=("user_"+uuid.uuid4().hex[:6]),email = email , first_name = name.split()[0],last_name = name.split()[-1],password = password1)
            user.save()
            profile = Profile(user = user,email = email , full_name = name,password = password1,number=number)
            profile.save()
            login(request,user)
            request.session['email'] = email
            return render(request,"student_home.html")
            
            #login
            # elif email_login!="":
        
            #       check_user = User.objects.filter(email = email_login).first()

            #       if check_user :
            #             context = {'message' : 'User doesnt exists' , 'class' : 'danger' }
            #             return render(request,'login.html' , context)

            #       elif password==check_user.password:
            #             login(request,check_user)
            #       request.session['email'] = email_login
            #       return render(request,"student_home.html")

      return render(request,"login.html")
      
def profile_show(request):
      if request.user.is_authenticated:
            email = request.session['email']

            profile=Profile.objects.filter(email =email).first()
            details={   
            'Quote' : profile.quote,    
            'Email':profile.email,
            'Name':profile.full_name,
      #Contact Details
            'Mobile':profile.number,
            'WhatsApp':profile.whatsapp_number,
            'Address':profile. address,
      
      #Other Details
            'About_Me':profile.about_me,
            'Graduation_Year':profile.graduation_year,

            'Designation':profile.designation,
            'Company':profile.company_name,
            'Tools_and_Techonologies':profile.tools_and_techonologies,
            }
            return render(request,"profile/profile_show.html",details)
      else:
            return redirect("Login")

def check_change(new,old):
      if new !=old and new!="" and new!=" ":
            return new
      else:
            print("yesss")
            return old

@csrf_exempt     
def profile_form(request):
         #Login Details
    email=request.session['email']
      
      #Find profile to be changed
    profile=Profile.objects.filter(email=email).first()
    full_name = profile.full_name

    if request.method == 'POST':

    #Contact Details
        number = request.POST.get('number')
        whatsapp_number=request.POST.get('whatsapp')
        address=request.POST.get('address')
    
    #Other Details
        quote=request.POST.get('quote')
        about_me=request.POST.get('about_me')
        graduation_year=request.POST.get('graduation_year')

        designation=request.POST.get('designation')
        company_name=request.POST.get('company')
        tools_and_techonologies=request.POST.get('tools_and_techonologies')
        proof= request.POST.get('proof')
        offer_letter=request.POST.get('offer_letter')

        linkedin= request.POST.get('linkedin')
        socials = request.POST.get('socials')
        
        #Accepts changes
       
        print(company_name)
        print(type(quote))
        profile.number = check_change(number,profile.number)
        profile.whatsapp_number=check_change(whatsapp_number,profile.whatsapp_number)
        profile.address=check_change(address,profile.address)
        profile.quote= check_change(quote,profile.quote)
        profile.about_me=check_change(about_me,profile.about_me)
        profile.graduation_year=check_change(graduation_year,profile.graduation_year)
        profile.designation=check_change(designation,profile.designation)
        profile.company_name= check_change(company_name,profile.company_name)
        profile.tools_and_techonologies=check_change(tools_and_techonologies,profile.tools_and_techonologies)
        profile.linkedin=  check_change(linkedin,profile.linkedin)
        profile.socials =  check_change(socials,profile.socials)
        
        profile.save()
        return redirect('Profile')

    return render(request,"profile/profile_form.html",{'name':full_name,'email':email})




def logout_attempt(request):
    logout(request)
    return render(request,"student_home.html")