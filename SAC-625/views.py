# views.py

from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# View for validating the Bajaj Allianz Group Sampoorna Jeevan Suraksha policy
def validate_policy(request):
    # retrieve the user credentials from the request
    user_credentials = request.POST.get('user_credentials')

    # Retrieve the sum assured range and tenure range selected by the Bandhan Bank sales personnel
    sum_assured_range = request.POST.get('sum_assured_range')
    tenure_range = request.POST.get('tenure_range')

    # Retrieve the product and master level values as defined for each product
    product_level = Product.objects.get(name=request.POST.get('product_level'))
    master_level = Master.objects.get(name=request.POST.get('master_level'))

    # Check if the user credentials fulfil the criteria for eligibility
    # Check if the sum assured range and tenure range selected by the Bandhan Bank sales personnel are valid
    # Check if the product and master level values as defined for each product are valid
    if user_credentials.annual_income >= 40000 and sum_assured_range in [50000, 100000, 150000, 200000] and tenure_range in [12, 15, 18, 24] and product_level.is_valid and master_level.is_valid:
        # If all criteria are fulfilled, issue the policy
        # Issue policy to the member
        policy = Policy.objects.create(user=user_credentials.user, sum_assured_range=sum_assured_range, tenure_range=tenure_range, product_level=product_level, master_level=master_level)
        # Issue policy to the member's spouse
        policy_spouse = Policy.objects.create(user=user_credentials.user.spouse, sum_assured_range=sum_assured_range, tenure_range=tenure_range, product_level=product_level, master_level=master_level)
    else:
        # If any of the criteria are not fulfilled, deny the policy
        return HttpResponse("Policy Denied")

    # Redirect the user to the policy confirmation page
    return HttpResponseRedirect(reverse('policy_confirmation'))

# View to display the policy confirmation page
def policy_confirmation(request):
    return render(request, 'policy_confirmation.html', {})