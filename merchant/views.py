from rest_framework.generics import ListAPIView
from .models import Merchant
from .serializers import MerchantSerializer
from rest_framework.pagination import PageNumberPagination

class CustomPaginationStyleOne(PageNumberPagination):
    # If this style is applied, Django will apply below 'page_size' for 
    # the specific 'api'or 'class' and ignore 'global-page-size' (set in settings.py)
    page_size = 2    

class CustomPaginationStyleTwo(PageNumberPagination):
    # If this style is applied, Django will ask you to set 'limit' by yourself, if nothing told by you
    # Django will go for 'global-page-size' (set in settings.py)
    page_size_query_param = 'limit'

class CustomPaginationStyleThree(PageNumberPagination):
    # If this style is applied, Django will apply below 'page_size'. However, you have flexibility to choose 
    # 'limit' from front-end if necessary, Your chosen option will override the below 'page-size'
    page_size = 2 
    page_size_query_param = 'limit'

# creating view here
class MerchantList(ListAPIView):
    queryset = Merchant.objects.all()
    serializer_class = MerchantSerializer
    pagination_class = CustomPaginationStyleThree
    