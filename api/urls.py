from django.conf.urls import include, url
from django.urls import path
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.routers import DefaultRouter

#from api.accounts.viewsets import AccountsViewSet
from . import views

app_name = 'api'

router = DefaultRouter()

#router.register('accounts', AccountsViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
