# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Tag
from .forms import PostAddForm
from django.contrib.auth.decorators import login_required

from django.db.models import Q

<<<<<<< Updated upstream
# Create your views here.
=======
from django.template.loader import render_to_string
from django.http import JsonResponse
#検証用の関数
def is_valid_q(q):
   return q != '' and q is not None

#関数内
>>>>>>> Stashed changes
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
   liked = False
   if post.like.filter(id=request.user.id).exists():
       liked = True
   return render(request, 'blog_app/detail.html', {'post': post, 'liked': liked})

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
