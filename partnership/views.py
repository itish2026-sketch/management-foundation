from django.shortcuts import render
from .models import (
    Partner, PartnershipInfo, PartnershipBenefit,
    PartnershipTimeline, PartnershipStat,
)


def partnership_view(request):

    info = PartnershipInfo.objects.first()

    partners = Partner.objects.filter(is_active=True)

    featured = partners.filter(is_featured=True)

    benefits = PartnershipBenefit.objects.filter(is_active=True)

    timeline = PartnershipTimeline.objects.all()

    stats    = PartnershipStat.objects.all()

    # Category-wise grouping (optional)
    government_partners = partners.filter(category='government')
    ngo_partners        = partners.filter(category='ngo')
    intl_partners       = partners.filter(category='international')
    corporate_partners  = partners.filter(category='corporate')

    context = {
        'info':                info,
        'partners':            partners,
        'featured':            featured,
        'benefits':            benefits,
        'timeline':            timeline,
        'stats':               stats,
        'government_partners': government_partners,
        'ngo_partners':        ngo_partners,
        'intl_partners':       intl_partners,
        'corporate_partners':  corporate_partners,
    }

    return render(request, 'partnership/partnership.html', context)