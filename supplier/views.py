from .models import Supplier
from rest_framework.generics import ListAPIView
from .serializers import SupplierSerializer

# Create your views here.
class SupplierList(ListAPIView):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer
    