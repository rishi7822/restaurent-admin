from django.shortcuts import render
from .models import MainCategoryFood,Tables,Waiters,bookorder_1
# Create your views here.

def index(request):
    return render(request,'index.html')


def add_mf(request):
    name1 = request.POST['fd']
    name2 = request.POST['sfd']
    m_obj = MainCategoryFood(mainStreamFoodName=name1,subCategoryFoodCharge=name2)
    m_obj.save()

    str1 = name1 + "  "+ name2
    return render(request,'index.html',{'obj_f':str1})

def add_tab(request):
    name1 = request.POST['tab']
    m_obj = Tables(tablename = name1)
    m_obj.save()
    return render(request,'index.html',{'obj_tab':name1})

def add_wait(request):
    name1 = request.POST['wait']
    m_obj = Waiters(WaiterName=name1)
    m_obj.save()
    return render(request,'index.html',{'obj_waiter':name1})

def add(request):
    return render(request,'index.html')


def book(request):
    return render(request,'book.html')


def add_order(request):
    pass

def book(request):
    obj1 = MainCategoryFood.objects.all()
    obj2 = Tables.objects.all()
    obj3 = Waiters.objects.all()
    return render(request,'book.html',{'foo':obj1,'tab':obj2,'waiter':obj3})

def book1(request):
    obj1 = Tables.objects.all()
    return render(request,'book.html',{'tab':obj1})

def person_add(request):
    name1 = request.POST["pname"]
    Mobile = request.POST["Mobno"]
    Address = request.POST["Addr"]
    print(name1,Mobile,Address)
    
    p_obj = bookorder_1(foodName=name1,foodPrice='##',nameOfTable=Mobile,nameOfWaiter=Address)
    p_obj.save()

    return render(request,'book.html',{'msg':"Data Saved Successfully"})