from django.shortcuts import render


# Create your views here.
import csv, io
from django.shortcuts import render
from django.contrib import messages
from csvapp.models import Employee
from django.core.mail import send_mail
def csv_upload(request):
    data = Employee.objects.all()
    if request.method == "GET":
        post=False
        return render(request, 'csvapp/upload.html')
    print(request.FILES,"uuuuuuuuuuuuuuuuuuuuuuuu")
    csv_file = request.FILES['file']
    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'THIS IS NOT A CSV FILE')
    data_set = csv_file.read().decode('UTF-8')
    # spliting file data into ,separted values,
    data=data_set.split('\r\n')
    data=','.join(data)
    data=data.split(',')
    L=['name','email','phone','city','country']
    for x in range(5):
        print(data[x])
        if data[x]==L[x]:
            pass
        else:
            # If CSV formate wrong
            context={'invalid':True}
            return render(request, 'csvapp/invalidcsv.html', context)
    x=5
    try:
        # Storing csv data into database
        while x<=(len(data)):
            Emp=Employee(name=data[x],email=data[x+1],phone=data[x+2],city=data[x+3],country=data[x+4])
            Emp.save()
            x+=5
    except:
        pass
    finally:
        # Displayiong tabular formate
        post=True
        obj=Employee.objects.all()
    context = {'post':post,'obj':obj}
    return render(request, 'csvapp/upload.html',context)