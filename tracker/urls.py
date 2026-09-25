from django.urls import path
from .views import *
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import ObtainAuthToken


router=DefaultRouter()
router.register('register',RegisterViewSet,basename='register')
router.register('exp',ExpenseViewset,basename='exp')


urlpatterns = [

    path('login/',ObtainAuthToken.as_view()),
    path('summery/',SummeryApiView.as_view())
    
   
] + router.urls
