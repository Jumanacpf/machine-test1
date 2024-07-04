from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Register
from .models import Product

# Create your views here.
def pregister(request):
        if request.method == 'POST':
            first_name = request.POST['first_name']
            last_name=request.POST['last_name']
            email = request.POST['email']
            address = request.POST['address']
            phone = request.POST['phone']
            details = Register.objects.create(
                first_name=first_name,
                last_name=last_name,
                email=email,
                address=address,
                phone=phone,)
            details.save()
            return redirect(plogin)

        else:
            return render(request, 'register.html')




def plogin(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        data = Register.objects.get(username=username)
        if data.password == password:
            request.session['id'] = data.id

        else:
            return HttpResponse("invalid credential")
    else:
        return render(request,'login.html')

def addproduct(request):
    if request.method=='POST':
        productname=request.POST['productname']
        price=request.POST['price']
        descriprion=request.POST['category']
        data=Product.objects.create(
            prdct_name=productname,
            price=price,
            descriprion=descriprion)
        data.save()
        return redirect(viewproduct)
    else:
        return render(request,'addprdct.html')


def viewproduct(request):
    products=Product.objects.all()
    return render(request,'viewprdct.html',{'products':products})







