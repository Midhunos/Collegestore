from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import OrderForm
from .models import Department, Order


# Create your views here.
def index(request):
    departments = Department.objects.all()
    return render (request,"index.html",{"departments":departments})
def index2(request):
    departments = Department.objects.all()
    return render (request,"index2.html",{"departments":departments})

def order_form(request):
    if request.method == 'POST':
        form = OrderForm(request.POST,request.FILES)
        if form.is_valid():
            name = form.cleaned_data['name']
            dob = form.cleaned_data['dob']
            age = form.cleaned_data['age']
            gender = form.cleaned_data['gender']
            phone_number = form.cleaned_data['phone_number']
            mail_id = form.cleaned_data['mail_id']
            address = form.cleaned_data['address']
            department = form.cleaned_data['department']
            course = form.cleaned_data['courses']
            purpose = form.cleaned_data['purpose']
            materials_provided = form.cleaned_data['materials_provided']


            order = Order(
                name=name,
                dob=dob,
                age=age,
                gender=gender,
                phone_number=phone_number,
                mail_id=mail_id,
                address=address,
                department=department,
                course=course,
                purpose=purpose,
                materials_provided=', '.join(materials_provided),
            )
            order.save()
            messages.info(request, "Thank you we will get back you soon")
            return redirect("order_form")


    else:
        form = OrderForm()
    return render(request,'forms.html',{'form': form})
