from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
#import stripe

#stripe.api_key = settings.STRIPE_SECRET_KEY
# Create your views here.

# intent = stripe.PaymentIntent.create(
#    amount=1099,
#    currency='usd',
#    # Verify your integration in this guide by including this parameter
#    metadata={'integration_check': 'accept_a_payment'},
# )
