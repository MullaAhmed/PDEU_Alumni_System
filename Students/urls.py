from django.urls import  path
from . import views

urlpatterns = [
    path("",views.student_home,name="Student Home"),
    path("about/",views.about,name="About"),
    path("alumni/",views.alumni,name="Alumni"),
    path("Announcements/",views.announcement,name="Announcements"),
    path("chat_box/",views.chat_box,name="ChatBox"),
    path("contact/",views.contact,name="Contact"),

    #login & signup
    path("login/",views.login_attempt,name="Login"),
    path('logout/' , views.logout_attempt , name="logout"),
   
    #Profile
    path("profile_show/",views.profile_show,name="Profile"),
    path("profile_form/",views.profile_form,name="Profile Form"),
    

]
