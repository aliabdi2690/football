from django.shortcuts import render, get_object_or_404
from .models import Post, Tag


def homepage(request):
    posts = Post.objects.all().order_by('-pub_date')
    return render(request, 'home.html', {'posts':posts})

def detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'detailview.html', {'post':post})


def tags(request, slug):
    tag = get_object_or_404(Tag, slug=slug)
    posts = tag.post.all().order_by('-pub_date')
    return render(request, 'tag.html', {'posts':posts, 'tag':tag})