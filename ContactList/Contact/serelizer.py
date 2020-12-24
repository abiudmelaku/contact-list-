from rest_framework import  serializers
from .models import contact_lst , Account
class contact_serilazers(serializers.ModelSerializer):
    class Meta:
        model = contact_lst
        fields = ['id', 'first_name' , 'last_name','phone_num']
    def update(self , instance):
        instance.first_name = self.validated_data['first_name']
        instance.last_name = self.validated_data['last_name']
        instance.phone_num = self.validated_data['phone_num']
        instance.save()
        return instance;
        
class Account_contact_serilazers(serializers.ModelSerializer):
    password2 = serializers.CharField(style={"input_type":"password"} , write_only= True)
    class Meta:
        model = Account
        fields = ['id','email', 'username', 'password' , 'password2']
        extra_kwargs = {
            'password':{"write_only":True}
        }
    
    def save(self):
        if self.validated_data['password'] != self.validated_data['password2']:
            raise serializers.ValidationError({'password':"Passwords must match"})
        acc = Account(email= self.validated_data['email'] , username = self.validated_data['username'],
        password = self.validated_data['password'])
        acc.save()
    