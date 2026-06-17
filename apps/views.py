from django.contrib import messages
from django.shortcuts import render , redirect
from django.views.generic import View
from .forms import *

def home(request):
    return render(request,'code/home.html')
class Signup(View):
    def get(self,request):
        fm = signupform()
        return render(request,"code/signup.html",{'form':fm})
    def post(self, request):
        fm = signupform(request.POST)

        if fm.is_valid():
            user = fm.save()
            messages.success(request, "Account created successfully!")
            return redirect('/signup')

           
           
        else:
            for field, errors in fm.errors.items():
                for error in errors:
                    messages.error(request, f"{field}: {error}")
            return render(request, "code/signup.html", {"form": fm})





