from django.shortcuts import render, redirect
from django.conf import settings
from .forms import CreditCardForm
import stripe

stripe.api_key = settings.STRIPE_SECRET_KEY

# Create your views here.
def make_payment(request):
    if request.method == "POST":
        card_form = CreditCardForm(request.POST)
        if card_form.is_valid():
            token=card_form.cleaned_data['stripe_id']
            charge = stripe.Charge.create(
                amount=2000,
                currency='EUR',
                description=request.user.email,
                card=token,
                )
            request.user.profile.paid = True
            request.user.profile.save()
            return redirect("profile")
    else:
        form = CreditCardForm()
        return render(request, "billing/make_payment.html", {'form': form, 'publishable': settings.STRIPE_PUBLISHABLE_KEY})
        
        
        
def remove_credit_card(request):
    request.user.profile.stripe_id = ""
    request.user.profile.card_ending = ""
    request.user.profile.save()
    return redirect("profile")
    
    
def x(request):
    amount = int(request.POST['amount'])
    total_in_cent = amount * 100
    
    charge = stripe.Charge.create(
            amount=total_in_cent,
            currency='EUR',
            customer=request.user.profile.stripe_id,
            )

    return redirect("profile")
    

