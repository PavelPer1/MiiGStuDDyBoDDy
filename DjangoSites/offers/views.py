from django.shortcuts import render
from users.models import HelpMe, Profile
from .models import CreateOffers


def page_offer(request, offer):
    inform_offer = HelpMe.objects.get(id=offer)
    users_profile = Profile.objects.get(user_id=inform_offer.user_id)

    if 'response' in request.POST:
        user = request.user.id
        user_offer = inform_offer.user_id
        his_offer = inform_offer

        of = CreateOffers(
            user_id=user,
            user_offer_id=user_offer,
            offer=his_offer
        )

        of.save()

    context = {
        'inform_offer': inform_offer,
        'users_profile': users_profile
    }

    return render(request, 'page_offer.html', context)