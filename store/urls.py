from django.urls import path
from views import index,Sign_up,Login
from django.conf.urls.static import static
from django.conf import settings




urlpatterns = [
    path('',index,name="homepage"),
    path('sign_up/',Sign_up.as_view(),name='signup'),
    path('login/',Login.as_view(),name='login'),




]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
