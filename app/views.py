from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django_daraja.mpesa.core import MpesaClient
from django_daraja.models import AccessToken
from django.contrib import messages

def index(request):
    if request.method == 'POST':
        if 'phone_number' in request.POST and 'amount' in request.POST:
            # Handle the "Support Me" form submission
            phone_number = request.POST.get('phone_number')
            amount_str = request.POST.get('amount')
            
            try:
                amount = int(amount_str)
            except ValueError:
                return HttpResponse("Invalid amount. Amount must be a valid integer.")
            
            account_reference = 'reference'
            transaction_desc = 'Description'
            callback_url = 'https://your-callback-url.com'
            cl = MpesaClient()
            
            try:
                access_tokens = AccessToken.objects.all()
                response = cl.stk_push(phone_number, amount, account_reference, transaction_desc, callback_url)
                # Add a success message
                messages.success(request, 'Thanks Check you phone to enter Mpesa-Pin.')
            except Exception as e:
                # Display a "Poor Internet Connection" message
                messages.error(request, 'Poor Internet Connection')
        
        elif 'rating' in request.POST:
            # Handle the "Rate Me" form submission
            rating = request.POST.get('rating')
            messages.success(request, 'Thank rated')
            return render(request, "index.html")

    return render(request, 'index.html')

    
def stk_push_callback(request):
        data = request.body
        
        return HttpResponse("STK Push in Django👋")


# Create your views here.
