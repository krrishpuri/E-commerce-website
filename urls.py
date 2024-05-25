from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_view
from .forms import LoginForm, MyPasswordResetForm, PasswordChangeForm

from django.contrib.auth.views import LogoutView



urlpatterns = [
    path("", views.home),
    path("about/", views.about,name="about"),
    path("contact/",views.contact,name="contact"),
    path("category/<slug:val>",views.CategoryView.as_view(),name="category"),

    path('product/<int:pk>/', views.ProductDetail.as_view(), name='product_detail'),
    path("profile/",views.ProfileView.as_view(),name='profile'),
    path("address/",views.ProfileView.as_view(),name='address'),
    path("updatedAddress/<int:pk>", views.UpdateAddress.as_view(), name='updatedAddress'),
    
    path("add-to-cart/", views.add_to_cart, name="add-to-cart"),
    path("cart/", views.show_cart, name="showcart"),
    path("checkout/", views.show_cart, name="checkout"),
    
    
    
    path("registration/",views.CustomerRegistrationView.as_view(),name='customerregistration'),
    path("account/login/",auth_view.LoginView.as_view(template_name='app/login.html',authentication_form=LoginForm),name='login'),
    path("password-reset/",auth_view.PasswordResetView.as_view(template_name='app/password_reset.html',form_class=MyPasswordResetForm),name='password_reset'),
    path("passwordchange/", auth_view.PasswordChangeView.as_view(template_name='app/changepassword.html', form_class=PasswordChangeForm, success_url='/passwordchangedone'), name='passwordchange'),
    path("passwordchangedone/", auth_view.PasswordChangeDoneView.as_view(template_name='app/passwordchangedone.html'),  name='passwordchangedone'),
    # path('logout/', LogoutView.as_view(next_page="login"), name='logout'),





]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
