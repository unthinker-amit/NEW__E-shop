from django.urls import path
from .views import index,sign_up,login
from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [
    path('',index,name="homepage"),
    path('sign_up/',sign_up.as_view()),
    path('login/',login.as_view(),name='login')
    # path('sign_up/',sign_up)



]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
