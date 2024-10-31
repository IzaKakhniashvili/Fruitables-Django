from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required

@login_required
class CartView(TemplateView):
    template_name = 'cart.html'

class CheckoutView(TemplateView):
    template_name = 'checkout.html'
