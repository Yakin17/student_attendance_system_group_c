from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .EmailBackEnd import  EmailBackEnd
from django.contrib import messages
# Create your views here.
def showDemoPage(request):
    return render(request,"demo.html")

def FLoginPage(request):
    return render(request,"login_page.html")

def doLogin(request):
    if request.method!="POST":
        return HttpResponse("<h2>Method not allowed</h2>")
    else:
        user=EmailBackEnd.authenticate(request,username=request.POST.get("email"),password=request.POST.get("password"))
        if user!=None:
            login(request,user) #La fonction login(user) (de Django) est appelée pour établir une session pour l'utilisateur authentifié.
            if user.user_type=="1":
                return HttpResponseRedirect("/admin_home")
            elif user.user_type=="2":
                return HttpResponseRedirect(reverse("faculty_member_home"))
            elif user.user_type=="3":
                return HttpResponseRedirect(reverse("student_home"))
            else:
                return HttpResponseRedirect("/")

        else:
            messages.error(request,"Invalid Login Details")
            return HttpResponseRedirect("/")

def GetUserDetails(request):
    if request.user!=None:
        return HttpResponse("User: "+request.user.email+" usertype: "+request.user.user_type)
    else:
        return HttpResponse("Please Login First")

def logout_user(request):
    logout(request)
    return HttpResponseRedirect("/")

