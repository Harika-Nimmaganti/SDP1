from django.shortcuts import render, redirect
from .models import Employee

# Create your views here.

def insert_emp(request):
    if request.method == "POST":
        EmpId = request.POST['EmpId']
        EmpName = request.POST['EmpName']
        EmpGender = request.POST['EmpGender']
        EmpEmail = request.POST['EmpEmail']
        EmpDesignation = request.POST['EmpDesignation']
        data = Employee(EmpId=EmpId, EmpName=EmpName, EmpGender=EmpGender, EmpEmail=EmpEmail,
                        EmpDesignation=EmpDesignation)
        data.save()

        return redirect('show-emp')
    else:
        return render(request, 'insert.html')

def show_emp(request):
    employees = Employee.objects.all()
    return render(request, 'show.html', {'employees': employees})


from django.shortcuts import render, redirect, get_object_or_404
from .models import Employee

def edit_emp(request, pk):
    try:
        employee = Employee.objects.get(id=pk)

        if request.method == 'POST':
            employee.EmpName = request.POST.get('EmpName')
            employee.EmpGender = request.POST.get('EmpGender')
            employee.EmpEmail = request.POST.get('EmpEmail')
            employee.EmpDesignation = request.POST.get('EmpDesignation')
            employee.save()
            return redirect('show-emp')

        context = {
            'employee': employee,
        }
        return render(request, 'edit.html', context)

    except Employee.DoesNotExist:
        return render(request, 'error.html', {'message': 'Employee not found'})

#Delete Employee
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from .models import Employee

def remove_emp(request, pk):
    employee = get_object_or_404(Employee, id=pk)

    if request.method == 'POST':
        employee.delete()
        return redirect('show-emp')

    return render(request, 'delete.html', {'employee': employee})
