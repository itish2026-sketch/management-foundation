from django.shortcuts import render, get_object_or_404
from .models import WhatWeDo


def whatwedo_list(request):
    """সব active post একসাথে, category filter সহ।"""

    category = request.GET.get('category', '')

    posts = WhatWeDo.objects.filter(is_active=True)

    if category:
        posts = posts.filter(category=category)

    context = {
        'posts':      posts,
        'category':   category,
        'categories': WhatWeDo.CATEGORY_CHOICES,
    }

    return render(request, 'whatwedo/list.html', context)



def whatwedo_detail(request, slug):
    """একটা post-এর detail page।"""

    post = get_object_or_404(WhatWeDo, slug=slug, is_active=True)

    related = (
        WhatWeDo.objects
        .filter(is_active=True, category=post.category)
        .exclude(id=post.id)[:3]
    )

    return render(request, 'whatwedo/detail.html', {
        'post':    post,
        'related': related,
    })