from django.urls import path
from .views import MerchantList
# Create your views here.
urlpatterns = [
    path('get-merchant-list', MerchantList.as_view())
]