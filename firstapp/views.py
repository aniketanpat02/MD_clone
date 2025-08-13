from http.client import responses

from django.http import HttpResponse , JsonResponse
from django.shortcuts import render
from firstapp.models import Center, Customer, Collection
from django.views.decorators.csrf import csrf_exempt
import json
from django.views import View
from django.utils.decorators import method_decorator
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet
from django.http import JsonResponse
from .models import Center
import json

from .serializer import CenterSerializer


# Create your views here.

def Centerdata(request):
    Centers = Center.objects.all()
    context = {
        'Centers': Centers
    }
    return render(request,'centerdata.html',context)
    

def index(request):
    context = {
        'filename':HttpResponse.status_code,
        'name':'First and Last name',
        'address':'Actual address'
    }
    #return HttpResponse("welcome to homepage")
    return render(request, 'index.html',context)
def viaserialize(request):
    try:
        id = request.GET.get('id')
        center= Center.objects.get(id=id)
        print(type(center))
        center_seri = CenterSerializer(center)
        print(type(center_seri))
        return JsonResponse(center_seri.data)
    except Center.DoesNotExist:
        return JsonResponse({"status":"nothing"})

def contact(request):
    return HttpResponse("This is Your Contact Page")
def about(request):
    return HttpResponse("This is Your About Page")
def services(request):
    return HttpResponse("You want our services :) :) :)")
def list1(request):
    return HttpResponse("THIS is YOUR List page")
def cow(request):
    return HttpResponse("This is cow page")
def buffelo(request):
    return HttpResponse("this is buffelo page")
def tryy(request):
    return render(request,'tryadmin.py')
def centerr(request):
    Centers = Center.objects.all()
    context = {
        'Centers': Centers
    }
    return render(request,'centerdata.html',context)


def get_center(request):
    print(request.body)
    if request.method == 'GET':
        centers = Center.objects.filter(status=2).values()
        print(request.user)
        centerlist= list(centers)
        return JsonResponse(list(centers), safe=False)
#this retrieve all list i want 1 index record#write postman json to post data in database


@csrf_exempt
def create_center(request):
    print("demo",request.method)
    print(request.body)
    if request.method =='POST':

        data = json.loads(request.body)


        for keys,value in data.items():
            if value is None or value=="":
                print("AAA")
                return JsonResponse({'MMM':'missing '} ,status=403)
            else:

                print(type(data))
                print(type(request.body))

                center = Center.objects.create(
                    code=data['code'],
                    short_name=data['shortname'],
                    name=data['name'],
                    phone=data['phone'],
                    village=data['village']
                )
                print(center.short_name)

                return JsonResponse({'created_id': center.id})
    else:
        return JsonResponse({'Status':'Enter valid Method'})

@csrf_exempt
def update_center(request , id):

    if request.method =='PUT':
        center = Center.objects.get(pk=id)
        print(type(center))
        data = json.loads(request.body)
        print(data)
        print(center)
        center.code = data['code']
        center.short_name = data['shortname']
        center.name = data['name']
        center.phone = data['phone']
        center.village = data['village']
        center.save()
        return JsonResponse({'Status :': 'updated'})

    else:
        return JsonResponse({'Status': 'Enter valid Method'})

@csrf_exempt
def single_update(request, id):
    print(request.body)
    if request.method == 'PATCH':
        center = Center.objects.get(pk=id)
        data = json.loads(request.body)
        center.code = data.get('code', center.code)
        center.short_name = data.get('shortname', center.short_name)
        center.name = data.get('name', center.name)
        center.phone = data.get('phone', center.phone)
        center.village = data.get('village', center.village)
        center.save()
        return JsonResponse({'message': 'Center updated successfully'})
    else:
        return JsonResponse({'Status': 'Enter valid Method'})


@csrf_exempt
def delete_center(request,id):
    if request.method=='DELETE':
        try:
            center = Center.objects.get(pk=id)
            if center.status==2 or center.status==1:
                center.status= 3
                center.save()
                print(center.id)
                return JsonResponse({'Status':'Record deleted'})
            else:
                return JsonResponse({'Status':'Record Not Available'})

        except Center.DoesNotExist:
            return JsonResponse({'Status':'Please Enter valid id'})
    else:
        return JsonResponse({'Status':'Enter valid Method'})

def gett(request,code):
    if request.method=='GET':
        centers = Center.objects.filter(code=code,status=2).values()
        context = {
            'centers': centers
        }
        return render(request,'getuser.html',context)
"""
def get_user(request,code,name):
    if request.method=='GET':
        centers = Center.objects.filter(code=code,name=name,status=2).values()

        centerlist=list(centers)
        return JsonResponse(centerlist,safe=False)
        
        
        
        print(type(data))
        print(type(request.body))

        center = Center.objects.create(
            code=data['code'],
            short_name=data['shortname'],

            name=data['name'],
            phone=data['phone'],
            village=data['village']
            )
        print(center.short_name)
        return JsonResponse({'created_id': center.id})
"""
def get_user(request):
    print(request.body,request.method=='GET')
    if request.method == 'GET':
        code = request.GET.get('code')
        print(code)
        name = request.GET.get('name')
        print(name)
        centers = Center.objects.filter(status=2)
        #print(centers)
        if code:
            centers = centers.filter(code=code)
            print(centers)
        if name:
            centers = centers.filter(name=name)
            print(centers)
        #centers = Center.objects.filter(code=code, name=name, status=2).values() or Center.objects.filter(code=code, status=2).values() or Center.objects.filter(name=name, status=2).values()
        centerlist = list(centers.values())
        return JsonResponse(centerlist, safe=False)



#-----------------------------------------||||---------------------------------------------
"""

def center_all(request,id):
    if request.method == 'GET':
        centers = Center.objects.filter(status=2).values()
        print(request.user)
        centerlist= list(centers)
        return JsonResponse(list(centers), safe=False)
    if request.method =='POST':

        data = json.loads(request.body)


        for keys,value in data.items():
            if value is None or value=="":
                print("AAA")
                return JsonResponse({'MMM':'missing '} ,status=403)
            else:

                print(type(data))
                print(type(request.body))

                center = Center.objects.create(
                    code=data['code'],
                    short_name=data['shortname'],
                    name=data['name'],
                    phone=data['phone'],
                    village=data['village']
                )
                print(center.short_name)

                return JsonResponse({'created_id': center.id})
    if request.method =='PUT':
        center = Center.objects.get(pk=id)
        print(type(center))
        data = json.loads(request.body)
        print(data)
        print(center)
        center.code = data['code']
        center.short_name = data['shortname']
        center.name = data['name']
        center.phone = data['phone']
        center.village = data['village']
        center.save()
        return JsonResponse({'Status :': 'updated'})
    if request.method == 'PATCH':
        center = Center.objects.get(pk=id)
        data = json.loads(request.body)
        center.code = data.get('code', center.code)
        center.short_name = data.get('shortname', center.short_name)
        center.name = data.get('name', center.name)
        center.phone = data.get('phone', center.phone)
        center.village = data.get('village', center.village)
        center.save()
        return JsonResponse({'message': 'Center updated successfully'})
    if request.method == 'DELETE':
        try:
            center = Center.objects.get(pk=id)
            if center.status == 2 or center.status == 1:
                center.status = 3
                center.save()
                print(center.id)
                return JsonResponse({'Status': 'Record deleted'})
            else:
                return JsonResponse({'Status': 'Record Not Available'})

        except Center.DoesNotExist:
            return JsonResponse({'Status': 'Please Enter valid id'})

"""
@csrf_exempt
def get_customer(request):
    if request.method =='GET':
        customers = Customer.objects.all().values()
        customerlist=list(customers)
        return JsonResponse(customerlist,safe=False)
    if request.method =='POST':
        print(request.method)
        data = json.loads(request.body)
        print(data)
        customer = Customer.objects.create(
            number=data['number'],
            number_prefix=data['number_prefix'],
            first_name= data['first_name'],
            last_name= data['last_name'],
            gender=data['gender'],
            dob = data['dob'],
            mobile=data['mobile']
        )
        print(customer.mobile)
        return JsonResponse({'Id created at':customer.id} )
@csrf_exempt
def get_customer1(request,id):
    print(request.method)
    if request.method=='PUT':
        data = json.loads(request.body)

        print(data)
        try:
            customer= Customer.objects.get(pk=id)
            customer.number = data['number']
            customer.number_prefix = data['number_prefix']
            customer.first_name = data['first_name']
            customer.last_name = data['last_name']
            customer.gender= data['gender']
            customer.dob = data['dob']
            customer.mobile = data['mobile']
            customer.save()
            print(customer.mobile)
            return JsonResponse({'Status':'record updated'})
        except Customer.DoesNotExist:
            return JsonResponse({'status': 'id not exists'}, status=404)

    if request.method=='PATCH':
        data = json.loads(request.body)
        try:
            customer = Customer.objects.get(pk=id)
            customer.number= data.get('number', customer.number)
            customer.number_prefix= data.get('number_prefix' , customer.number_prefix)
            customer.first_name= data.get('first_name', customer.first_name)
            customer.last_name= data.get('last_name', customer.last_name)
            customer.gender= data.get('gender', customer.gender)
            customer.dob= data.get('dob', customer.dob)
            customer.mobile = data.get('mobile', customer.mobile)
            customer.save()
            return JsonResponse({'Small record Status':'updated'})
        except Customer.DoesNotExist:
            return JsonResponse({'status':'id not exists'},status=404)

    if request.method=='DELETE':
        try:
            customer = Customer.objects.get(pk=id)
            if customer.status==1 or customer.status==2:
                customer.status=3
                customer.save()
                return JsonResponse({'status':'Record deleted'})
            else:
                return JsonResponse({'Status':'id does not exist'})
        except Customer.DoesNotExist:
            return JsonResponse({'status':'id not exists'},status=404)

@csrf_exempt
def get_collections(request):
    print(request.method)
    if request.method=='GET':
        collection= Collection.objects.all().values()
        print(collection)
        collectionlist= list(collection)
        return JsonResponse(collectionlist,safe=False)

    if request.method=='POST':
        data = json.loads(request.body)
        collection = Collection.objects.create(
            date = data['date'],
            type = data['type'],
            shift = data['shift'],
            quantity = data['quantity'],
            snf = data['snf'],
            fat = data['fat'],
            rate = data['rate']
        )
        return JsonResponse({'Data insserted at':collection.id})

@csrf_exempt
def get_collection1(request,id):
   if  request.method=='PUT':
       data = json.loads(request.body)
       collection = Collection.objects.get(pk=id)
       collection.date= data['date']
       collection.type = data ['type']
       collection.shift = data ['shift']
       collection.quantity = data['quantity']
       collection.snf= data['snf']
       collection.fat=data['fat']
       collection.rate = data['rate']
       collection.save()
       return JsonResponse({'status':'record  Updated'})
   if request.method=='PATCH':
        data = json.loads(request.body)
        try:
            collection = Collection.objects.get(pk=id)
            collection.number= data.get('number', collection.number)
            collection.number_prefix= data.get('number_prefix' , collection.number_prefix)
            collection.first_name= data.get('first_name', collection.first_name)
            collection.last_name= data.get('last_name', collection.last_name)
            collection.gender= data.get('gender', collection.gender)
            collection.dob= data.get('dob', collection.dob)
            collection.mobile = data.get('mobile', collection.mobile)
            collection.save()
            return JsonResponse({'Small record Status':'updated'})
        except Collection.DoesNotExist:
            return JsonResponse({'status':'id not exists'},status=404)

   if request.method=='DELETE':
        try:
            collection = Collection.objects.get(pk=id)
            if collection.status==1 or collection.status==2:
                collection.status=3
                collection.save()
                return JsonResponse({'status':'Record deleted'})
            else:
                return JsonResponse({'Status':'id does not exist'})
        except Collection.DoesNotExist:
            return JsonResponse({'status':'id not exists'},status=404)




@method_decorator(csrf_exempt, name='dispatch')
class CenterView(View):

    def get(self, request):
        centers = Center.objects.all().values()
        centerlist = list(centers)
        return JsonResponse(centerlist, safe=False, status=200)

    def post(self, request):
        data = json.loads(request.body)
        center = Center.objects.create(
            code=data['code'],
            short_name=data['short_name'],
            name=data['name'],
            phone=data['phone'],
            village=data['village']
        )
        return JsonResponse({'id': center.id, 'message': 'Center created successfully'}, status=201)
    def put(self,request):
        try:
            id= request.GET.get('id')
            if not id:
                return JsonResponse({'status':'missing mandatory field'})
            #here i need to upload from url not from body
            data = json.loads(request.body)
            center = Center.objects.get(pk=id)
            center.code = data['code']
            center.short_name = data['short_name']
            center.name = data['name']
            center.phone = data['phone']
            center.village = data['village']
            center.save()
        except Center.DoesNotExist:
            return JsonResponse({'status':'id not fount'})
        return JsonResponse({'id updated at': id})

#-------------------------------------------------------------------------------------------

# API view


#@method_decorator(csrf_exempt, name='dispatch')
class CustomerAPIView(APIView):
    print("A")
    def get(self, request):
        print("a")
        customer = list(Customer.objects.all().values())
        print(customer)
        return JsonResponse(customer,safe=False, status=200)
    def post(self,request):
        print(request.method)
        data = request.data
        print(data)
        customer = Customer.objects.create(
            number=data['number'],
            number_prefix=data['number_prefix'],
            first_name= data['first_name'],
            last_name= data['last_name'],
            gender=data['gender'],
            dob = data['dob'],
            mobile=data['mobile']
        )
        print(customer.mobile)
        return JsonResponse({'Id created at':customer.id} )
        #return JsonResponse({'id created ':center.id})

    def put(self,request):
        data = request.data
        sdate= request.GET.get('startdate')
        edate = request.GET.get('edate')
        id = request.GET.get('id')
        try:
            #customer = Customer.objects.filter
            customer = Customer.objects.get(pk=id)
            customer.number= data.get('number', customer.number)
            customer.number_prefix= data.get('number_prefix' , customer.number_prefix)
            customer.first_name= data.get('first_name', customer.first_name)
            customer.last_name= data.get('last_name', customer.last_name)
            customer.gender= data.get('gender', customer.gender)
            customer.dob= data.get('dob', customer.dob)
            customer.mobile = data.get('mobile', customer.mobile)
            customer.save()
            return JsonResponse({'record Status':'updated'})
        except Customer.DoesNotExist:
            return JsonResponse({'status':'id not exists'},status=404)

    def delete(self,request):
        try:
            id = request.GET.get('id')
            customer = Customer.objects.get(pk=id)
            if customer.status == 1 or customer.status == 2:
                customer.status = 3
                customer.save()
                return JsonResponse({'status': 'Record deleted'})
            else:
                return JsonResponse({'Status': 'id does not exist'})
        except Customer.DoesNotExist:
            return JsonResponse({'status': 'id not exists'}, status=404)

1
#-------------------------------------------------------------------------------------------
# Collection according to filter and One to many relationship
@method_decorator(csrf_exempt, name='dispatch')
class CollectionView(View):
    print("A")
    def get(self, request):
        try:
            pk = request.GET.get('id')
            center = Center.objects.get(id=pk)
            print("A")
        except Center.DoesNotExist:
            return JsonResponse({"status":"id is missing or invalid"})
        sdate = request.GET.get('startdate')
        edate = request.GET.get('enddate')
        shift = request.GET.get('shift')
        type = request.GET.get('type')
        if pk:
            collected = Collection.objects.filter(center_id=pk)
        if not sdate or not edate:
            return JsonResponse({"Status":"Start data and End date is mandatory"},status=400)

        #if edate and not sdate:
            #return JsonResponse({"Status":"Start data and End date is mandatory"},status=400)

        print("a")
        if sdate and edate:
            collected = collected.filter(date__range=[sdate, edate])
        if shift:
            collected = collected.filter(shift=shift)
        if type:
            collected = collected.filter(type=type)
        fat=0
        quantity =0
        snf = 0
        count=0
        rate = 0
        li=[]
        for c in collected:
            name={"shift":c.shift,"date":c.date,"center name":center.name}
            li.append(name)
            print(c.date,c.shift,center.name)
            fat +=c.fat
            quantity += c.quantity
            count+=1
            snf+= c.snf
            rate+= c.rate

        #return JsonResponse(li,safe=False,status=200)
        #collectionbycenter = list(center.centers.filter(shift='M').values())
        print("Average Fat= " , fat/count," average Quantity=", quantity/count, "Average snf=", snf/count,"Average rate=",rate/count)
        afterfilter = {" Ave fat":fat/count,"Ave quantity":quantity/count,"Ave snf":snf/count,"Ave rate":rate/count}
        dict2 = {"COllections": li, "average": afterfilter}

        return JsonResponse(dict2,safe=False, status=200)
        #return JsonResponse( name, safe=False, status=200)
##-------------------------------------------------------------------------------------------
# viewset for 3 models


class CenterViewSet(ViewSet):

    def list(self,request):
        c = Center.objects.all()
        center = list(Center.objects.all().values())
        return JsonResponse(center, safe=False)
    def create(self,request):
        data = request.data
        center = Center.objects.create(
            code=data['code'],
            short_name=data['shortname'],
            name=data['name'],
            phone=data['phone'],
            village=data['village']
        )
        center.save()
        return JsonResponse({'status':center.id })

    def update(self, request):
        data = request.data
        print(data)
        id = request.GET.get('id')
        print(id)
        center = Center.objects.get(pk=id)
        center.code = data.get('code', center.code)
        center.short_name = data.get('shortname', center.short_name)
        center.name = data.get('name', center.name)
        center.phone = data.get('phone', center.phone)
        center.village = data.get('village', center.village)
        center.save()
        return JsonResponse({'message': 'Center updated successfully'})

    def destroy(self,request):
        try:
            id = request.GET.get('id')
            center = Center.objects.get(pk=id)
            if center.status == 1 or center.status == 2:
                center.status = 3
                center.save()
                return JsonResponse({'status': 'Record deleted'})
            else:
                return JsonResponse({'Status': 'id does not exist'})
        except Customer.DoesNotExist:
            return JsonResponse({'status': 'id not exists'}, status=404)





"""

2) create a api view to perform crud operation - done




def viaserialize(request):
    id = request.GET.get('id')
    try:
        center = Center.objects.get(id=id)
        center_seri = CenterSerializer(center)
        return JsonResponse(center_seri.data)  #  Return as JSONResponse
    except Center.DoesNotExist:
        return JsonResponse({"error": "Center not found"}, status=404) # Handle the case where the object doesn't exist


"""
