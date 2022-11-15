from customers.models import Customer
from customers.serializer import CustomerSerializer
from django.http import JsonResponse

def customers(request):
  #invoke serializer and return to client
  data = Customer.objects.all()
  serializer = CustomerSerializer(data, many=True)
  return JsonResponse({'customers': serializer.data})