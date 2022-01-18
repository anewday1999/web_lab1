from logging import exception
from django.http.response import JsonResponse
from django.shortcuts import redirect, render
from .models import findtutorpost, subs_fintutor
from django.contrib.auth import get_user_model
from django.views.decorators.csrf import csrf_exempt
from PIL import Image
from django.core.paginator import Paginator
import time
from django.core.mail import send_mail
from django.conf import settings

#payment
from cloudipsp import Api, Checkout
# Create your views here.
User = get_user_model()

def FindTutor(request):
    current_page = request.GET.get('page')
    print(current_page)
    paginator = Paginator(findtutorpost.objects.all().order_by('-date_posted'), 7)
    if current_page != None and current_page != '':
        if int(current_page) <= int(paginator.num_pages):
            context = {
                'nav' : 'findtutor',
                'postsFindTutor' : paginator.get_page(int(current_page)),
                'pages': paginator.num_pages
            }
    else:
        context = {
            'nav' : 'findtutor',
            'postsFindTutor' : paginator.get_page(1),
            'pages': paginator.num_pages
        }
    return render(request, 'tutor/findtutor.html', context)

def FindTutorMypost(request):
    current_page = request.GET.get('page')
    print(current_page)
    all_post = findtutorpost.objects.all().filter(author = request.user)
    paginator = Paginator(all_post.order_by('-date_posted'), 7)
    if current_page != None:
        if int(current_page) <= int(paginator.num_pages):
            context = {
                'nav' : 'findtutor',
                'postsFindTutor' : paginator.get_page(int(current_page)),
                'pages': paginator.num_pages
            }
    else:
        context = {
            'nav' : 'findtutor',
            'postsFindTutor' : paginator.get_page(1),
            'pages': paginator.num_pages
        }
    return render(request, 'tutor/findtutor_mypost.html', context)

'''@csrf_exempt
def get_page(request):
    paginator = Paginator(findtutorpost.objects.all().order_by('-date_posted'), 7)

    current_page = request.POST['page']
    where = request.POST['where']

    paginator.get_page(current_page)

    if where == 'next' and paginator.get_page(current_page).has_next():
        context = {
        'nav' : 'findtutor',
        'postsFindTutor' : paginator.get_page(int(current_page) + 1),
        'pages': paginator.num_pages
        }
    print(context)
    return render(request, 'findtutor.html', context)'''

@csrf_exempt
def report_post(request):
    if request.user.is_authenticated:
        user = request.user
        if request.method == 'POST':
            try:
                post_id = request.POST['id']
                post_obj = findtutorpost.objects.get(id=post_id)
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
    main_content = request.POST["main_content"]
    subject = request.POST["subject"]
    calendar = request.POST["calendar"]
    salary = request.POST["salary"]
    contact = request.POST["contact"]
    date_outdate = request.POST["date_outdate"]
    user = request.user
    post_img1 = request.FILES.get('img1')
    post_img2 = request.FILES.get('img2')
    post_img3 = request.FILES.get('img3')
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


    if is_valid == True: 
        if title and main_content and calendar and salary and contact and date_outdate and subject:   
            try:
                new_post = findtutorpost(title=title, main_content=main_content, subject=subject, calendar=calendar, salary=salary,
                                        contact = contact, date_outdate = date_outdate, author = user, post_img1 = post_img1,
                                        post_img2 = post_img2, post_img3 = post_img3)
                new_post.save()
                #send mail
                list_mail = []
                if subs_fintutor.objects.all().filter(id=1):
                    for user in subs_fintutor.objects.all().filter(id=1).first().list_user.all():
                        list_mail.append(user.email)
                else:
                    new_subs = subs_fintutor()
                    new_subs.save()
                    for user in subs_fintutor.objects.all().filter(id=1).first().list_user.all():
                        list_mail.append(user.email)
                print(list_mail)
                send_mail(
                    'TMVIETNGA.COM - Find tutor:',
                    
                    title + '\n\n' +
                    main_content + '\n\n- Subject: ' +
                    subject + '\n- Calendar: ' +
                    calendar + '\n- Salary: ' +
                    salary + '\n- Author: ' +
                    user.username +
                    f'\n\n Hãy truy cập {settings.MY_DOMAIN}/findtutor to read this new.',

                    'anewday19991@gmail.com',
                    list_mail,
                    fail_silently=False,
                )

                return_info = {"success" : True}
                return JsonResponse(return_info, safe=False)
            except Exception as e:
                print(e)
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
            post = findtutorpost.objects.all().filter(id = post_id).first()
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
            post = findtutorpost.objects.all().filter(id = post_id).first()
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
        if request.user == findtutorpost.objects.all().filter(id = post_id).first().author:
            _title = request.POST["title"]
            _main_content = request.POST["main_content"]
            _subject = request.POST["subject"]
            _calendar = request.POST["calendar"]
            _salary = request.POST["salary"]
            _contact = request.POST["contact"]
            try:
                findtutorpost.objects.all().filter(id = post_id).update(title=_title, main_content=_main_content,
                                                                        subject=_subject, calendar=_calendar, salary= _salary, contact = _contact)
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

def ImTutor(request):
    context = {
        'nav' : 'listtutor'
    }
    return render(request, 'imtutor.html', context)

#notice
@csrf_exempt
def notice(request):
    if request.user.is_authenticated:
        if not request.user.is_verified:
            post_info={"success":False, "detail":"2"}
            return JsonResponse(post_info, safe=False)
        if request.method == 'POST':
            try:
                subs = subs_fintutor.objects.get(id = 1)
            except:
                new_subs = subs_fintutor()
                new_subs.save()
                subs = subs_fintutor.objects.get(id = 1)
            if request.user in subs.list_user.all():
                post_info={"success":True, "detail":"turnoff"}
                request.user.is_sub_findtutor = False
                request.user.save()
                subs.list_user.remove(request.user)
                return JsonResponse(post_info, safe=False)
            else:
                post_info={"success":True, "detail":"turnon"}
                request.user.is_sub_findtutor = True
                request.user.save()
                subs.list_user.add(request.user)
                return JsonResponse(post_info, safe=False)
    else:
        #Đăng nhập để thực hiện thao tác.
        post_info={"success":False, "detail":"1"}
        return JsonResponse(post_info, safe=False)
#payment
def fondy_payment(request):
    api = Api(merchant_id=1485885,
          secret_key='test')
    checkout = Checkout(api=api)
    data = {
        "currency": "RUB",
        "amount": 10000
    }
    url = checkout.url(data).get('checkout_url')
    return redirect(url)