
from django.core.paginator import Paginator
from django.shortcuts import render
from .models import BlogPost

def blog_list(request):
    posts = BlogPost.objects.all().order_by('-created_at')

    items_per_page = request.GET.get('items_per_page', 10)
    try:
        items_per_page = int(items_per_page)
    except ValueError:
        items_per_page = 10

    paginator = Paginator(posts, items_per_page)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'items_per_page': items_per_page,
    }
    return render(request, 'blog/blog_list.html', context)
