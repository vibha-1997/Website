# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import get_object_or_404, render

from django.shortcuts import render
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from website.forms import UserForm, UserProfileForm
from website.tokens import account_activation_token
from .models import room_category,room_category_size,product_category,products,selection
from django.http import HttpResponse,HttpResponseRedirect
from django.views.decorators.cache import cache_control
from django.conf import settings
# Create your views here.

def welcome(request):
    return render(request,'welcome.html')

@login_required
def  welcome2(request):
    return render(request,'welcome2.html')

@login_required
def create_design(request):
    latest_category_list = room_category.objects.all()
    product_cat=product_category.objects.all()
    product_ids=products.objects.all()
    context = {'latest_category_list': latest_category_list,'product_cat':product_cat,'product_ids':product_ids}
    return render(request, 'create_design.html',context)

@login_required
def selected_products(request,u_pk,p_pk,c_pk):
    #return HttpResponse('p is hit')
    p=selection(u_pk,p_pk,c_pk)
    q=selection.objects.filter(product_cat=c_pk)
    r=q.count()
    if(r>=1):
        q.delete()
        
        p.save()
    else:
        p.save()

    return HttpResponseRedirect('/user')
    
    
#def home(request):
#    latest_category_list = room_category.objects.all()
#    context = {'latest_category_list': latest_category_list}
#    return render(request, 'welcome.html',context)

    
@login_required
def details(request,pc_name_id):
    product_cat_list=product_category.objects.all()
    products_list=products.objects.all()
    context={'products_list':products_list}




@login_required
def get_cart(request,u_pk):
    r=selected_productss.objects.filter(u_pk=u_pk)
    context=[]
    for pro in r:
        q=products.objects.filter(id=r[0].id)
        context.append(q[0].product_name)
    context={'user_products':context}
    return render(request,'cart.html',context)


def register(request):
    #registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save(commit=False)
            user.set_password(user.password)
            user.is_active = False
            user.save()

            profile = profile_form.save()
            profile.user = user
            profile.save()

            current_site = get_current_site(request)
            subject = 'activate your account'
            message = render_to_string('registration/account_activation_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            user.email_user(subject, message)
            return redirect('account_activation_sent')
         #   registered = True
          #  user_form = UserForm()
           # profile_form = UserProfileForm()
        else:
            print user_form.errors, profile_form.errors

    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    return render(request, 'registration/registration_form.html', {'user_form':user_form, 'profile_form': profile_form})

def account_activation_sent(request):
    return render(request, 'registration/account_activation_sent.html')

def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.profile.email_confirmed = True
        user.save()
        login(request, user)
        return redirect('activation_complete')
    else:
        return render(request, 'registration/account_activation_invalid.html')

def activation_complete(request):
    return render(request, 'registration/activation_complete.html')
