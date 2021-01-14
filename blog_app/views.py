# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Tag, Comment
from .forms import PostAddForm, CmtForm
from django.contrib.auth.decorators import login_required

from django.db.models import Q

from django.template.loader import render_to_string
from django.http import JsonResponse
#検証用の関数
def is_valid_q(q):
   return q != '' and q is not None

#関数内
def index(request):
   query = request.GET.get('q')
   if query:
       posts = Post.objects.all().order_by('-created_at')
       posts = posts.filter(
       Q(title__icontains=query)|
       Q(user__username__icontains=query)
       ).distinct()
   else:
       posts = Post.objects.all().order_by('-created_at')  
   return render(request, 'blog_app/index.html', {'posts': posts, 'query': query,})

def detail(request, post_id):
   post = get_object_or_404(Post, id=post_id)
   comments = Comment.objects.filter(post=post).order_by('-created_at')
   liked = False
   if post.like.filter(id=request.user.id).exists():
       liked = True
   if request.method == "POST":
       form = CmtForm(request.POST or None)
       if form.is_valid():
           text = request.POST.get('text')
           comment = Comment.objects.create(post=post, user=request.user, text=text)
           comment.save()
   else:
       form = CmtForm()
   context = {
       'post': post,
       'comments': comments,
       'form': form,
       'liked': liked
   }    
   if request.is_ajax():
       html = render_to_string('blog_app/comment.html', context, request=request )
       return JsonResponse({'form': html})    
   return render(request, 'blog_app/detail.html', {'post': post, 'form': form, 'comments': comments, 'liked': liked})

@login_required
def add(request):
   if request.method == "POST":
      form = PostAddForm(request.POST, request.FILES)
      if form.is_valid():
         post = form.save(commit=False)
         post.user = request.user
         post.save()
         return redirect('blog_app:index')
   else:   
       form = PostAddForm()
   return render(request, 'blog_app/add.html', {'form': form})

@login_required
def edit(request, post_id):
   post = get_object_or_404(Post, id=post_id)
   if request.method == "POST":
       form = PostAddForm(request.POST, request.FILES, instance=post)
       if form.is_valid():
           form.save()
           return redirect('blog_app:detail', post_id=post.id)
   else:
       form = PostAddForm(instance=post)
   return render(request, 'blog_app/edit.html', {'form': form, 'post':post })

@login_required
def delete(request, post_id):
   post = get_object_or_404(Post, id=post_id)
   post.delete()
   return redirect('blog_app:index')

def like(request):
   post = get_object_or_404(Post, id=request.POST.get('post_id'))
   liked = False
   if post.like.filter(id=request.user.id).exists():
       post.like.remove(request.user)
       liked = False
   else:    
       post.like.add(request.user)
       liked = True
   context={
       'post': post,
       'liked': liked,
   }    
   if request.is_ajax():
       html = render_to_string('blog_app/like.html', context, request=request )
       return JsonResponse({'form': html})

def comment_delete(request, comment_id):
   comment = get_object_or_404(Comment, id=comment_id)
   comment.delete()
   return redirect('blog_app:detail', post_id=comment.post.id)