from django.shortcuts import render
from testapp.models import Employee
# Create your views here.
def empdata_view(request):
    emp_list=Employee.objects.all()
    print(emp_list)
    my_dict={'emp_list':emp_list}
    return render(request,'testapp/emp.html',context=my_dict)
