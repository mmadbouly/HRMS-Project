from django.shortcuts import render

# Create your views here.

from .models import EmployeeInfo


def employee_info_page(request,employee_id):

    obj = EmployeeInfo.objects.get(pk=employee_id) #query -> database -> get some data -> django renders it
    template_name = 'employee_info.html'
    context = {"object": obj} # badal ma afdal ageb hna kol 7aga men el obj b obj.PER_PersonID maslan la agebo kolo w fel html hatala3 elly ana 3ayzo
    return render(request, template_name, context)