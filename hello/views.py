from django.shortcuts import render, render_to_response, redirect
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpRequest
from django.template import loader
from hello.models import Publisher
from hello.forms import PublisherForm


# Create your views here.
def hello(request, a):
    # print(isinstance(request,HttpRequest))
    # print(request.path)
    # print(request.method)
    # print(request.POST.get('key'))
    # print(request.get_full_path())
    # print(a)
    user_list = User.objects.all()
    print(user_list.query)
    # return render(request, 'table.html', {'user_list': user_list})
    # return render_to_response('table.html', {'user_list': user_list})
    # t = loader.get_template('table.html')
    # c = {'user_list': user_list}
    # response = HttpResponse(t.render(c, request), content_type='text/html')
    # return response
    # return redirect("test/22/aaaaa")
    athlete = '0'
    athlete_list = [1, 2, 3, 4, 5, 6]
    return render(request, 'table.html', locals())


def test(request, id, key):
    print(id, key)
    user_list = User.objects.all()
    print(locals())
    return render(request, 'table.html', locals())


def add_publisher(request):
    if request.method == 'POST':
        # 如果为post提交，去接收用户提交过来的数据
        # name = request.POST.get('name')
        # address = request.POST['address']
        # city = request.POST['city']
        # country = request.POST['country']
        # state_province = request.POST['state_province']
        # website = request.POST['website']
        # Publisher.objects.create(
        #     name=name,
        #     address=address,
        #     city=city,
        #     country=country,
        #     state_province=state_province,
        #     website=website,
        # )
        # return HttpResponse("添加出版社信息成功！")

        #使用Django Form的情况
        # publisher_form = PublisherForm(request.POST)
        # if publisher_form.is_valid():
        #     Publisher.objects.create(
        #         name = publisher_form.cleaned_data['name'],
        #         address = publisher_form.cleaned_data['address'],
        #         city = publisher_form.cleaned_data['city'],
        #         country = publisher_form.cleaned_data['country'],
        #         state_province = publisher_form.cleaned_data['state_province'],
        #         website = publisher_form.cleaned_data['website']
        #     )
        #     return HttpResponse("添加出版社信息成功！")

        #使用Django ModelForm的情况
        publisher_form = PublisherForm(request.POST)
        if publisher_form.is_valid():
            publisher_form.save()
            return HttpResponse("添加出版社信息成功！")
    else:
        publisher_form = PublisherForm()
    return render(request, 'add_publisher.html', locals())
