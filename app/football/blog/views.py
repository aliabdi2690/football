from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Tag, Comment
from django.views.generic.base import RedirectView
from django.http import HttpResponseRedirect
from .forms import CommentForm
from django.contrib.auth.decorators import login_required
import datetime

def homepage(request):

    posts = Post.objects.all().order_by('-pub_date')
    return render(request, 'home.html', {'posts':posts})

def detail(request, slug):
    comment_form = CommentForm()
    post = get_object_or_404(Post, slug=slug)
    comments = post.comments.all().order_by('-time')
    return render(request, 'detailview.html', {'post':post, 'comment_form':comment_form, 'comments':comments})


def tags(request, slug):
    tag = get_object_or_404(Tag, slug=slug)
    posts = tag.post.all().order_by('-pub_date')
    return render(request, 'tag.html', {'posts':posts, 'tag':tag})


class likeview(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        slug = self.kwargs.get("slug")
        obj = get_object_or_404(Post, slug=slug)
        url_ = obj.get_absolute_url()
        user = self.request.user
        if user.is_authenticated:
            if user in obj.likes.all():
                obj.likes.remove(user)
            else:
                obj.likes.add(user)
        else:
            return redirect('/logein')
        return url_



class Commentvieew(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        user = self.request.user
        slug = self.kwargs.get("slug")
        obj = get_object_or_404(Post, slug=slug)
        if user.is_authenticated:
            
            form = CommentForm(data=self.request.POST)
            
            if form.is_valid():
                body = form.cleaned_data['body']
                new_comment = Comment.objects.create(body=body, username=user.username)
                new_comment.post = obj
                new_comment.save()
            url_ = obj.get_absolute_url()
            return url_
        else:
            url_ = obj.get_absolute_url()
            return url_


