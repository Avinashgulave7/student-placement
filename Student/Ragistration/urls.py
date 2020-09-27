from django.urls import path

from . import views
from .views import signup, signup


urlpatterns =[path("",views.index,name="index"),
              path("apply",views.apply,name="apply"),
              path("welcome",views.welcome,name="welcome"),

              path("signup",views.signup,name="signup"),
              path("signin",views.signin,name="signin"),
              path("about",views.about,name="about"),
              path("contact",views.contact,name="contact"),
              path("logout",views.logout,name="logout"),
              path("thanks",views.thanks,name="thanks"),
              
    ]