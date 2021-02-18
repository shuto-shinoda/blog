from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Tag, Comment
from .forms import PostAddForm, CmtForm, ContactForm
from django.contrib.auth.decorators import login_required

from django.db.models import Q

from django.template.loader import render_to_string
from django.http import JsonResponse, HttpResponse
from django.conf import settings
import textwrap
from django.core.mail import BadHeaderError, EmailMessage

#検証用の関数
def is_valid_q(q):
   return q != '' and q is not None

#関数内
def index(request):
   posts = Post.objects.all().order_by('-created_at')
   title_or_user = request.GET.get('title_or_user')
   date_min = request.GET.get('date_min')
   date_max = request.GET.get('date_max')
   tag = request.GET.get('tag')

   if is_valid_q(title_or_user):
       posts = posts.filter(Q(title__icontains=title_or_user)
                      | Q(user__username__icontains=title_or_user)
                      ).distinct()

   if is_valid_q(date_min):
       posts = posts.filter(created_at__gte=date_min)

   if is_valid_q(date_max):
       posts = posts.filter(created_at__lt=date_max)

   if is_valid_q(tag) and tag != 'タグを選択...':
       posts = posts.filter(tag__tag=tag)
   
   return render(request, 'blog_app/index.html', 
   {'posts': posts, 'title_or_user': title_or_user , 'date_min': date_min, 'date_max': date_max ,'tag': tag})

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

 #お問い合わせ
def contact(request):
  form = ContactForm(request.POST or None)
  if form.is_valid():
     name = form.cleaned_data['name']
     message = form.cleaned_data['message']
     email = form.cleaned_data['email']
     subject = 'お問い合わせありがとうございます。'
     contact = textwrap.dedent('''
        ※このメールはシステムからの自動返信です。

        {name} 様
        
        お問い合わせありがとうございます。
        以下の内容でお問い合わせを受け付けました。
        内容を確認させていただき、ご返信させていただきますので、少々お待ちください。

        ----------------------------------

        ・お名前
        {name}

        ・メールアドレス
        {email}

        ・メッセージ
        {message}
        -----------------------------------
        株式会社　〇〇
        〒000-0000
        〇〇県〇〇市〇〇区〇〇1-0-0
        TEL 123-456-7890
        営業時間 8:00~17:00（月~金）
        WEB: https://www.......com/
     ''').format(
        name=name,
        email=email,
        message=message
     )
     to_list = [email]
     bcc_list = [settings.EMAIL_HOST_USER]
     try:
        message = EmailMessage(subject=subject, body=contact, to=to_list, bcc=bcc_list)
        message.send()
     except BadHeaderError:
        return HttpResponse('無効なヘッダが検出されました。')
     return redirect('blog_app:done')

  return render(request, 'blog_app/contact.html',{'form': form})


def done(request):
   return render(request, 'blog_app/done.html')