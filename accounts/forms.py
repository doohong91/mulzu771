from django import forms
from .models import UserInfo

class UserInfoForm(forms.modelform):
    class Meta:
        model = UserInfo
        fields = '__all__'