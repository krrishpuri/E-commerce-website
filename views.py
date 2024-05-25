# from django.db.models import Count
# from django.conf import settings
# from django.shortcuts import render
# from django.views import View
# # from urllib import request
# # from django.http import HttpResponse
# from .models import Product,Cart
# from .forms import CustomerProfileForm,CustomerRegistrationForm
# from django.contrib import messages
# from django.shortcuts import redirect
# from django.shortcuts import get_object_or_404, redirect
# from django.http import HttpResponseBadRequest
# from django.contrib.auth.decorators import login_required
from django.db.models import Count
from django.conf import settings
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.http import HttpResponseBadRequest
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Product, Cart
from .forms import CustomerProfileForm, CustomerRegistrationForm
from django.contrib.auth.decorators import login_required
def home(request):
    return render(request, "app/index.html")


def about(request):
    return render(request, "app/about.html")


def contact(request):
    return render(request, "app/contact.html")


# class CategoryView(View):
#     def get(self,request,val):
#         product=Product.objects.filter(category=val)
#         title=Product.objects.filter(category=val).values('title').annotate(total=Count('title'))
#         return render(request ,"app/category.html",locals())


class CategoryView(View):
    def get(self, request, val):
        product = Product.objects.filter(category=val)
        title = Product.objects.filter(category=val).values('title').annotate(total=Count('title'))
        print("Product:", product)
        print("Title:", title)
        return render(request, "app/category.html", locals())

class ProductDetail(View):
    def get(self,request,pk):
        product=Product.objects.get(pk=pk)
        return render(request,"app/productdetail.html",locals())


class CustomerRegistrationView(View):
    def get(self, request):
        form = CustomerRegistrationForm()
        return render(request, 'app/customerregistration.html',locals())

    def post(self, request):
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Congratulations! User registered successfully")
            
        else:
            messages.warning(request, "Invalid input data")
        
        return render(request, 'app/customerregistration.html', locals()) 

class ProfileView(View):
    def get(self, request):
        form = CustomerProfileForm()
        return render(request, 'app/profile.html', locals())

    def post(self, request):
        form = CustomerProfileForm(request.POST)
        if form.is_valid():
            user = request.user
            name = form.cleaned_data["name"]
            locality = form.cleaned_data["locality"]
            city = form.cleaned_data["city"]
            mobile = form.cleaned_data["mobile"]
            state = form.cleaned_data['state']
            zipcode = form.cleaned_data['zipcode']
            reg = customer(user=user, name=name, locality=locality, mobile=mobile, city=city, state=state, zipcode=zipcode)
            reg.save()
            messages.success(request, "Congratulations! Profile Saved Successfully")
        else:
            messages.warning(request, "Invalid Input Data")
        return render(request, 'app/profile.html', locals())

    def address(self, request):
        add = Customer.objects.filter(user=request.user)
        return render(request, 'app/address.html', locals())


class UpdateAddress(View):
    def get(self, request, pk):
        add=Customer.objects.get(pk=pk)
        form = CustomerProfileForm()
        return render(request, 'app/updateAddress.html', locals())

    def post(self, request, pk):
        form = CustomerProfileForm(request.POST)
        return render(request, 'app/updateAddress.html', locals())
    
@login_required   
def add_to_cart(request):
    # user=request.user
    # product_id=request.GET.get('prod_id')
    # product =Product.objects.get(id=product_id)
    # cart
    
    
    user = request.user
    product_id = request.GET.get('prod_id')
    
    # Print the value of product_id
    print("Product ID:", product_id)

    try:
        product = Product.objects.get(id=product_id)
    except Product.DoesNotExist:
        # Handle the case where the product does not exist
        return HttpResponse("Product does not exist", status=404)

    cart
    return redirect("/cart")

# def add_to_cart(request):
#     product_id = request.GET.get('prod_id')

#     if not product_id:
#         return HttpResponseBadRequest('Product ID is required.')

#     try:
#         # Clean the product_id by removing any trailing slashes
#         product_id = product_id.rstrip('/')
#         product_id = int(product_id)
#     except ValueError:
#         return HttpResponseBadRequest('Invalid product ID.')

#     product = get_object_or_404(Product, id=product_id)

#     # Ensure a Cart object exists for the user
#     cart, created = Cart.objects.get_or_create(user=request.user)
#     cart.products.add(product)
#     cart.save()

#     return redirect('/cart')
def show_cart(request):
    user=request.user
    cart=Cart.objects.filter(user=user)
    amount=0
    for p in cart:
        value=p.quantity=p.product.discounted_price
        amount=amount+value
    totalamount=amount+40
    return render(request, 'app/addtocart.html',locals())


# def checkout(request):
#     return render(request, 'app/checkout.html')
