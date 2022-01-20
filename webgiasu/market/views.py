from logging import exception
from django.http.response import JsonResponse
from django.shortcuts import redirect, render
from .models import marketpost, subs_market
from django.contrib.auth import get_user_model
from django.views.decorators.csrf import csrf_exempt
from PIL import Image
from django.core.paginator import Paginator
import time
from django.core.mail import send_mail
from django.conf import settings

#Web
from rest_framework import generics
from myapi.serializers import marketpostSerializer
#payment
from cloudipsp import Api, Checkout
# Create your views here.
User = get_user_model()

class APIAllPost(generics.ListCreateAPIView):
    serializer_class = marketpostSerializer
    def get_queryset(self):
        return marketpost.objects.all()
    

def Market(request):
    current_page = request.GET.get('page')
    print(current_page)
    paginator = Paginator(marketpost.objects.all().order_by('-date_posted'), 7)
    if current_page != None and current_page != '':
        if int(current_page) <= int(paginator.num_pages):
            context = {
                'nav' : 'market',
                'postsMarket' : paginator.get_page(int(current_page)),
                'pages': paginator.num_pages
            }
    else:
        context = {
            'nav' : 'market',
            'postsMarket' : paginator.get_page(1),
            'pages': paginator.num_pages
        }
    return render(request, 'market/market.html', context)

def MarketMypost(request):
    current_page = request.GET.get('page')
    print(current_page)
    all_post = marketpost.objects.all().filter(author = request.user)
    paginator = Paginator(all_post.order_by('-date_posted'), 7)
    if current_page != None:
        if int(current_page) <= int(paginator.num_pages):
            context = {
                'nav' : 'market',
                'postsMarket' : paginator.get_page(int(current_page)),
                'pages': paginator.num_pages
            }
    else:
        context = {
            'nav' : 'market',
            'postsMarket' : paginator.get_page(1),
            'pages': paginator.num_pages
        }
    return render(request, 'market/market_mypost.html', context)

@csrf_exempt
def report_post(request):
    if request.user.is_authenticated:
        user = request.user
        if request.method == 'POST':
            try:
                post_id = request.POST['id']
                post_obj = marketpost.objects.get(id=post_id)
                if user in post_obj.report.all():
                    post_obj.report.remove(user)
                    return_info = {"success" : True, "detail": "unlike", 'num': post_obj.num_report}
                    return JsonResponse(return_info, safe=False)
                else:
                    post_obj.report.add(user)
                    return_info = {"success" : True, "detail": "like", 'num': post_obj.num_report}
                    return JsonResponse(return_info, safe=False)
            except:
                return_info = {"success" : False, "detail": "0"}
                return JsonResponse(return_info, safe=False)
    else:
        #Đăng nhập để thực hiện thao tác.
        post_info={"success":False, "detail":"1"}
        return JsonResponse(post_info, safe=False)


@csrf_exempt
def get_post_post(request):
    title = request.POST["title"]
    describe = request.POST["describe"]
    address = request.POST["address"]
    contact = request.POST["contact"]
    price = request.POST["price"]
    date_outdate = request.POST["date_outdate"]
    user = request.user
    post_img1 = request.FILES.get('img1')
    post_img2 = request.FILES.get('img2')
    post_img3 = request.FILES.get('img3')
    post_img4 = request.FILES.get('img4')
    post_img5 = request.FILES.get('img5')
    is_valid = True
    #image1
    try:
        if post_img1 != None:
            im=Image.open(post_img1)
        else:
            pass
    except IOError:
        is_valid = False
        post_img1 = None
    #image2
    try:
        if post_img2 != None:
            im=Image.open(post_img2)
        else:
            pass
    except IOError:
        is_valid = False
        post_img2 = None
    #image3
    try:
        if post_img3 != None:
            im=Image.open(post_img3)
        else:
            pass
    except IOError:
        is_valid = False
        post_img3 = None
    #image4
    try:
        if post_img4 != None:
            im=Image.open(post_img4)
        else:
            pass
    except IOError:
        is_valid = False
        post_img4 = None
    #image5
    try:
        if post_img5 != None:
            im=Image.open(post_img5)
        else:
            pass
    except IOError:
        is_valid = False
        post_img5 = None


    if is_valid == True:
        if title and describe and address and contact and price and date_outdate:
            try:
                new_post = marketpost(title=title, describe=describe, address=address,
                                        contact = contact, price=price, date_outdate = date_outdate, author = user, post_img1 = post_img1,
                                        post_img2 = post_img2, post_img3 = post_img3, post_img4 = post_img4, post_img5 = post_img5)
                new_post.save()
                
                #send mail
                list_mail = []
                if subs_market.objects.all().filter(id=1):
                    for user in subs_market.objects.all().filter(id=1).first().list_user.all():
                        list_mail.append(user.email)
                else:
                    new_subs = subs_market()
                    new_subs.save()
                    for user in subs_market.objects.all().filter(id=1).first().list_user.all():
                        list_mail.append(user.email)
                print(list_mail)
                send_mail(
                    'TMVIETNGA.COM - Market has posted:',
                    
                    title + '\n\n' +
                    describe + '\n\n- Address: ' +
                    address + '\n- Price: ' +
                    price + '\n- Author: ' +
                    user.username +
                    f'\n\n Click {settings.MY_DOMAIN}/market to read more.',

                    'anewday19991@gmail.com',
                    list_mail,
                    fail_silently=False,
                )

                return_info = {"success" : True}
                return JsonResponse(return_info, safe=False)
            except:
                print('error')
                return_info = {"success" : False, "detail":"Không thể lưu dữ liệu, có vẻ như bạn đã đăng xuất."}
                return JsonResponse(return_info, safe=False)
        else:
            return_info = {"success" : False, "detail":"Lỗi các trường văn bản."}
            return JsonResponse(return_info, safe=False)
    else:
        return_info = {"success" : False, "detail": "File không phù hợp."}
        return JsonResponse(return_info, safe=False)


@csrf_exempt
def get_user_info(request):
    if request.user.is_authenticated:
        user_id = request.POST["id"]
        try:
            user = User.objects.all().filter(id = user_id).first()
            user_info={"success":'True',
                        "full_name": user.full_name,
                        "school": user.school,
                        "specialize": user.specialize,
                        "yearofschool": user.yearofschool,
                        "sexs": user.sexs,
                        "years_of_birth": user.years_of_birth,
                        "more": user.more,
                        "last_login": user.last_login}
        except exception as e:
            print(e)
            post_info={"success":'False', "detail":"0"}
        
        return JsonResponse(user_info, safe=False)
    else:
        #Đăng nhập để thực hiện thao tác.
        post_info={"success":'False', "detail":"1"}
        return JsonResponse(post_info, safe=False)

@csrf_exempt
def get_post_contact(request):
    if request.user.is_authenticated:
        post_id = request.POST["id"]
        try:
            post = marketpost.objects.all().filter(id = post_id).first()
            post_info={"success":'True',
                        "contact": post.contact,
                        }
        except exception as e:
            print(e)
            #Không tìm thấy dữ liệu.
            post_info={"success":'False', "detail":"0"}
        
        return JsonResponse(post_info, safe=False)
    else:
        #Đăng nhập để thực hiện thao tác.
        post_info={"success":'False', "detail":"1"}
        return JsonResponse(post_info, safe=False)

@csrf_exempt
def delete_post(request):
    if request.user.is_authenticated:
        post_id = request.POST["id"]
        try:
            post = marketpost.objects.all().filter(id = post_id).first()
            if post.author == request.user:
                post_info={"success":True,
                            "detail": "deleted",
                            }
                if (post.post_img1 and post.post_img1.url):
                    post.post_img1.delete()
                if (post.post_img2 and post.post_img2.url):
                    post.post_img2.delete()
                if (post.post_img3 and post.post_img3.url):
                    post.post_img3.delete()
                if (post.post_img5 and post.post_img5.url):
                    post.post_img5.delete()
                if (post.post_img4 and post.post_img4.url):
                    post.post_img4.delete()
                post.delete()
            else:
                post_info={"success":False,
                            "detail": "Your are not own.",
                            }
        except exception as e:
            print(e)
            #Không tìm thấy dữ liệu.
            post_info={"success":False, "detail":"0"}
        
        return JsonResponse(post_info, safe=False)
    else:
        #Đăng nhập để thực hiện thao tác.
        post_info={"success":False, "detail":"1"}
        return JsonResponse(post_info, safe=False)

@csrf_exempt
def edit_post(request):
    if request.user.is_authenticated:
        post_id = request.POST["id"]
        if request.user == marketpost.objects.all().filter(id = post_id).first().author:
            _title = request.POST["title"]
            _describe = request.POST["describe"]
            _address = request.POST["address"]
            _contact = request.POST["contact"]
            _price = request.POST["price"]
            try:
                marketpost.objects.all().filter(id = post_id).update(title=_title, describe=_describe,
                                                                        address=_address, contact = _contact, price=_price)
                #oke
                post_info={"success":True, "detail":"Đã cập nhật."}
                return JsonResponse(post_info, safe=False)
            except:
                #cant update
                post_info={"success":False, "detail":"2"}
                return JsonResponse(post_info, safe=False)
        else:
            #not owner
            post_info={"success":False, "detail":"0"}
            return JsonResponse(post_info, safe=False)
    else:
        #Đăng nhập để thực hiện thao tác.
        post_info={"success":False, "detail":"1"}
        return JsonResponse(post_info, safe=False)
#forWeb
def patch_post(request):
    post_id = request.POST["id"]
    _title = request.POST["title"]
    _describe = request.POST["describe"]
    _address = request.POST["address"]
    _contact = request.POST["contact"]
    _price = request.POST["price"]
    try:
        marketpost.objects.all().filter(id = post_id).update(title=_title, describe=_describe,
                                                                address=_address, contact = _contact, price=_price)
        #oke
        post_info={"success":True, "detail":"Đã cập nhật."}
        return JsonResponse(post_info, safe=False)
    except:
        #cant update
        post_info={"success":False, "detail":"2"}
        return JsonResponse(post_info, safe=False)


#notice
@csrf_exempt
def notice(request):
    if request.user.is_authenticated:
        if not request.user.is_verified:
            post_info={"success":False, "detail":"2"}
            return JsonResponse(post_info, safe=False)
        if request.method == 'POST':
            try:
                subs = subs_market.objects.get(id = 1)
            except:
                new_subs = subs_market()
                new_subs.save()
                subs = subs_market.objects.get(id = 1)
            if request.user in subs.list_user.all():
                post_info={"success":True, "detail":"turnoff"}
                request.user.is_sub_market = False
                request.user.save()
                subs.list_user.remove(request.user)
                return JsonResponse(post_info, safe=False)
            else:
                post_info={"success":True, "detail":"turnon"}
                request.user.is_sub_market = True
                request.user.save()
                subs.list_user.add(request.user)
                return JsonResponse(post_info, safe=False)
    else:
        #Đăng nhập để thực hiện thao tác.
        post_info={"success":False, "detail":"1"}
        return JsonResponse(post_info, safe=False)

    pass