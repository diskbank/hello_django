from django import forms
from hello.models import Publisher

class PublisherForm(forms.ModelForm):
    # name = forms.CharField(label='姓名', error_messages={"required": "这个项必须填写"})
    # address = forms.CharField(label="地址")
    # city = forms.CharField(label="城市")
    # state_province = forms.CharField(label="省份")
    # country = forms.CharField(label="国家")
    # website = forms.URLField(label="网址")

    class Meta:
        model = Publisher
        exclude = ("id",)