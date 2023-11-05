from django.shortcuts import render,redirect
from . models import *
from django.contrib import messages
from shops.form import CustomUserForm
from django.http import JsonResponse
from django.contrib.auth import authenticate,login,logout
import json

def home(request):
    products=Product.objects.filter(trending=1)
    return render(request,"shops/index.html",{"products": products})
def favviewpage(request):
    if request.user.is_authenticated:
      fav=Favourite.objects.filter(user=request.user)
      return render(request,"shops/fav.html",{'fav':fav})
    else:
      return redirect("/")

def logout_page(request):
   if request. user.is_authenticated:
      logout(request)
      messages.success(request,"logged out successfully")
   return redirect("/")

def login_page(request):
   if request.user.is_authenticated:
      return redirect("/")
   else:
      if request.method=="POST":
         name=request.POST.get("username")
         pwd=request.POST.get("password")
         user=authenticate(request,username=name,password=pwd)
         if user is not None:
            login(request,user)
            messages.success(request,"logged in successfully")
            return redirect("/")
         else:
            messages.error(request,"invalid  user name or password")
      return  render(request,"shops/login.html")
   
   
def register(request):
    form= CustomUserForm()
    if request.method=="POST":
       form=CustomUserForm(request.POST)
       if form.is_valid():
          form.save()
          messages.success(request,"registartion  success you can login")
          return redirect('/login')
    return render(request,"shops/register.html",{'form':form})


def collections(request):
    catagory=Catagory.objects.filter(status=0)
    return render(request,"shops/collections.html",{ "catagory": catagory})
def collectionsview(request,name):
    if(Catagory.objects.filter(name=name,status=0)):
        products=Product.objects.filter(catagory__name=name)
        return render(request,"shops/products/index.html",{ "products": products,"catagory_name":name})
    else:
        messages.warning(request,"no such catagory found")
        return redirect('collections')
def product_details(request,pname,cname):
    if(Catagory.objects.filter(name=cname,status=0)):
      if(Product.objects.filter(name=pname,status=0)):
        products=Product.objects.filter(name=pname,status=0).first()
        return render(request,'shops/products/product_details.html',{"products":products})
      else:
        messages.error(request,"no such catagory found")
        return redirect('collections')
    else:
      messages.error(request,"no such catagory found")
      return redirect('collections')
def add_to_cart(request):
   if request.headers.get('x-requested-with')=='XMLHttpRequest':
    if request.user.is_authenticated:
      data=json.load(request)
      product_qty=data['product_qty']
      product_id=data['pid']
      #print(request.user.id)
      product_status=Product.objects.get(id=product_id)
      if product_status:
        if Cart.objects.filter(user=request.user.id,product_id=product_id):
          return JsonResponse({'status':'Product Already in Cart'}, status=200)
        else:
          if product_status.quantity>=product_qty:
            Cart.objects.create(user=request.user,product_id=product_id,product_qty=product_qty)
            return JsonResponse({'status':'Product Added to Cart'}, status=200)
          else:
            return JsonResponse({'status':'Product Stock Not Available'}, status=200)
    else:
      return JsonResponse({'status':'Login to Add Cart'}, status=200)
   else:
    return JsonResponse({'status':'Invalid Access'}, status=200)
"""def add_to_cart(request) :
    if request.headers.get('x-requested-with')=='XMLHttpRequest':
       if request.user.is_authenticated:
         data=json.load(request)
         product_id=data['pid']
         product_qty=data['product_qty']
         product_status=Product.objects.get(id=product_id)
         if product_status:
            if Cart.objects.filter(user=request.user.id,product_id=product_id):
               return JsonResponse({'status' :'product Already in cart'},status=200)
         else:
            if product_status.quantity>=product_qty:
               Cart.objects.create(user=request.user,product_id=product_id,product_qty=product_qty)
               return JsonResponse({'status':'product added to cart is success'},status=200)
            else:
               return JsonResponse({'status':'product stock is not available'},status=200)
       else:
          return JsonResponse({'status':'login to add cart'},status=200)
    else:
       return JsonResponse({"status":'invalid access'},status=200)"""
    
def cart_page(request):
   if request.user.is_authenticated:
      cart=Cart.objects.filter(user=request.user)
      return render(request,"shops/cart.html",{'cart':cart})
   else:
      return redirect("/")
   
def remove_cart(request,cid):
   cartitem=Cart.objects.get(id=cid)
   cartitem.delete()
   return redirect("/cart")
def remove_fav(request,fid):
   cartite=Favourite.objects.get(id=fid)
   cartite.delete()
   return redirect("/favviewpage")
def fav_page(request):
    if request.headers.get('x-requested-with')=='XMLHttpRequest':
       if request.user.is_authenticated:
          data=json.load(request)
          product_id=data['pid']
          product_status=Product.objects.get(id=product_id)
          if product_status:
            if Favourite.objects.filter(user=request.user.id,product_id=product_id):
               return JsonResponse({'status' :'product Already in favourite'},status=200)
            else:
               Favourite.objects.create(user=request.user,product_id=product_id)
               return JsonResponse({'status':'favourite added successfully'}, status=200)
       else:
          return JsonResponse({'status':'Login to add to favourite'}, status=200)
    else:
       return JsonResponse({'status':'Invalid Access'}, status=200)
   
   


    
          


    