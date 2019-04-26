from django.shortcuts import render

# Create your views here.

def home_page(request):
    my_title = "Human Resources Management System"
    context = {"title": my_title}
    if request.user.is_authenticated:
        context = {"title": my_title, "my_list": [1,2,3,4,5]}
  
    return render(request, "home.html", context)


def about_page(request):
    about_hrms = "HR Management System is responsible for collecting, managing and tracking company’s data and its employ’s data and payroll."
    return render(request, "about.html", {"title": about_hrms})




def contact_page(request):
    contact_hrms = "Please Call Me: 0123456789"
    context = {"content": contact_hrms}
    return render(request, "contact.html", context)

