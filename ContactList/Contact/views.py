from django.shortcuts import render
from django.http import HttpResponse
import _json
import logging
from .serelizer import contact_serilazers , Account_contact_serilazers
from .models import contact_lst,Account
from rest_framework.response import  Response
from rest_framework import viewsets , status
from rest_framework.decorators import api_view , action
my_loger = logging.getLogger("my_logger")

# Create your views here.
def home(request):
    return HttpResponse("Wellcome the my first ec2 hompage !!!")
class handle_contact_crud(viewsets.ModelViewSet):
    serializer_class =  contact_serilazers
    queryset = contact_lst.objects.all()
    def create(self , request , *args , **kwargs):
        data = request.data
        ser = contact_serilazers(data= data)
        if ser.is_valid():
            ser.save()
            my_loger.info("Contact Created !!!")
            return  Response(ser.data , status= status.HTTP_200_OK)
        return Response(ser.errors)
    def update(self , request , *args , **kwargs):
        id = kwargs['pk']
        print(kwargs , request.data)

        update_query = contact_lst.objects.get(id = id )
        if update_query:
            update_json = dict()
            update_json['first_name'] = request.data['first_name']
            update_json['last_name'] = request.data['last_name']
            update_json['phone_num'] = request.data['phone_num']
            ser = contact_serilazers(data = update_json)
            if ser.is_valid():
                updated_contact = ser.update(update_query)
                x = contact_serilazers(updated_contact , many = False)
                print(x.data)
                return Response(x.data , status= status.HTTP_200_OK)
                my_loger.info("Contact updated !!!")
            return Response({} , status= status.HTTP_200_OK);
        else:
            res = {"message": "Sorry Something went wrong =("}
            return Response(res ,status= status.HTTP_200_OK )
            

        
       
    def destroy(self , request , *args , **kwargs):
        res = None;
        del_id = kwargs['pk']
        del_query = contact_lst.objects.get(id = del_id)
        if del_query:
            del_query.delete()
            my_loger.info("Contact deleted Successfully")
            res = {"message":"Deletion Successfull"}
        else:
            res = {"message": "Sorry Something went wrong =("}

        
        return Response(res , status= status.HTTP_200_OK)
@api_view(['GET'],)
def get_Accounts(request):
    print("yessssss")
    qs = Account.objects.all().values();
    ser = Account_contact_serilazers(qs , many = True);
    return Response(ser , status= status.HTTP_200_OK)
@api_view(['POST'],)
def create_Account(request):
    data = request.data
    ser = Account_contact_serilazers(data=data)
    if ser.is_valid():
        print("isvalid")
        ser.save()
        res = {"message":"Account Created!!!"}
        return Response(res , status=status.HTTP_200_OK)
    return Response(ser.errors)




            
    
        
    

