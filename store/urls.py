from django.urls import path
from .views import Index,Sign_up,Login,Cart,Checkout,Orders
from .views.login import logout
from django.conf.urls.static import static
from django.conf import settings
from store.middlewares.auth import auth_middleware




urlpatterns = [
    path('',Index.as_view(),name="homepage"),
    path('sign_up',Sign_up.as_view(),name='signup'),
    path('login/',Login.as_view(),name='login'),
    path('logout/',logout,name='logout'),
    path('cart/',Cart.as_view(),name='cart'),
    path('checkout/',Checkout.as_view(),name='checkout'),
    path('orders/',auth_middleware(Orders.as_view()),name='orders'),




]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
