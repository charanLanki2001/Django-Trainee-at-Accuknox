# event_horizon/views.py


from django.shortcuts import render
from .models import Payment
from .signals import payment_confirmed

def process_payment(request):
    # Simulating payment processing
    payment = Payment.objects.create(amount=1000)
    
    # Trigger the signal
    print("Triggering signal...")
    payment_confirmed.send(sender=Payment, payment=payment)
    print("Signal triggered.")
    
    return render(request, 'payment_success.html', {'payment': payment})
