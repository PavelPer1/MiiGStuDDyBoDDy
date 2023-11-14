from django.shortcuts import render
from users.models import HelpMe, IcanHelp


def get_home(request):
    my_offer_cards = [x.items for x in IcanHelp.objects.filter(user_id=request.user.id)]
    all_offer_cards = [item for item in HelpMe.objects.all() if (item.item in my_offer_cards) and
                       (item.user_id != request.user.id)]
    context = {
        'my_offer_cards': my_offer_cards,
        'all_offer_cards': all_offer_cards

    }
    return render(request, 'home.html', context)
