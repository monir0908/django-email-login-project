from .models import Supplier
from .serializers import SupplierSerializer
from .views import SupplierList

from django.urls import path
urlpatterns = [
    path('get-supplier-list', SupplierList.as_view()),
]
