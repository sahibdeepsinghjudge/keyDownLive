from multiprocessing import context
from turtle import title
from django.core.checks import messages
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import redirect, render
from .models import PostLikes, blog, blog_Details, tagsData
from django.contrib import messages
from django.views.generic.list import ListView
from .forms import blogForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from users.models import UserDetail
def blog_all(request):
    blogs=blog_Details.objects.all().order_by('-id')[0:11]
    bloga=blog_Details.objects.all().order_by('-id')[0:1]
    tags = tagsData.objects.all().order_by("-tag_uses")[0:11]
    print("tags",tags)
    context={
         'title':'Blog',
         'bloga':blogs,
         'blog':bloga,
        'tags':tags
    }
    return render(request,'blog/blog.html',context)

def blog_details(request,slug):
    blogd=blog_Details.objects.filter(slug=slug)
    
    if blogd:
        blog_object=blog_Details.objects.get(slug=slug)
        blogs=blog_Details.objects.all().order_by('-blog_clicks')[0:6]
        try:
            blog_content = blog.objects.get(blog_id = blog_object.id)
        except:
            if request.user == blog_object.blog_creator:

                return redirect('/'+slug+'/update/')
            else:
                messages.warning(request,"Requested source is incomplete.")
                return redirect('/')
        blog_object.blog_clicks=blog_object.blog_clicks+1
        blog_object.save()
        if blog_object in blogs:
            trending = True
        else:
            trending = False
        context = {
            'title':'Blog | '+ blog_object.blog_title,
            'blog':blogd,
            'blog_content':blog_content.blog_content,
            'is_trending':trending,
        }
        return render(request,'blog/blog.html',context)
    else:
        messages.info(request,"Requested blog not found!")
        return redirect('/')

def create_blog_page(request):
    if not request.user.is_authenticated:
        return redirect("/login/")
    context = {
        'title':'Create Blog',
    }
    return render(request,'blog/createblog.html',context)
def create_blog(request):
    if request.method=='POST':
        blog_title = request.POST.get('title')
        brief = request.POST.get('brief')
        bloga = blog.objects.create(blog_title=blog_title,blog_brief=brief)
        bloga.save()
        messages.success(request,'Blog created')
    return redirect('/create-blog/write/')

class AddBlogView(ListView,LoginRequiredMixin):
    model = blog
    def get(self, request):
        if request.user.is_authenticated:
            form = blogForm()
            return render(request, 'blog/createblog.html', {'form':form,'name':'Create Blog'})
        else:
            messages.info(request,'Access denied or 404')
        return redirect('/blog/')
   
    def post(self, request):
        form = blogForm(request.POST)
        if form.is_valid():
    
            blog_content = form.cleaned_data['blog_content']
            add_post = blog.objects.create( blog_content= blog_content)
            add_post.save()
            form = blogForm()
            messages.success(request,'Blog created')
            return redirect('/users/profile/'+request.user.username)
        else:
            messages.error(request,"Process failed due to internal server error.")
            return redirect('/')
@login_required
def update_view(request, slug):
    # dictionary for initial data with 
    # field names as keys
    context ={}
  
    # fetch the object related to passed id
    blog_det = blog_Details.objects.get(slug=slug)
    def retrunBlog():
        try:
            obj = blog.objects.get(blog_id = blog_det.id)
            return obj
        except:
            blog_ob = blog.objects.create(blog_id = blog_det,blog_content = '')
            blog_ob.save()
            retrunBlog()
        
        
    # pass the object as instance in form
    form = blogForm(request.POST or None, instance = retrunBlog())
  
    # save the data from the form and
    # redirect to detail_view
    if form.is_valid():
        form.save()
        messages.success(request,'Blog post updated')
        return redirect("/blog/"+slug+'/')
       
    # add form dictionary to context
    context["form"] = form
    context["name"] = 'Update | '+blog_det.blog_title
     
    return render(request, "blog/createblog.html", context)
@login_required
def blog_delete_view(request,slug):
    if request.user.is_superuser:
        blog_det_obj = blog_Details.objects.get(slug=slug)
        blog_det_obj.delete()
        messages.success(request,"Your blog has been deleted!")
        return redirect('/')
    else:
        messages.error(request,"Action not completed")
        return redirect('/blog/',slug)

#home page

def home_view(request):
    blogs=blog_Details.objects.all().order_by('-blog_clicks')[0:6]
    authors = UserDetail.objects.all().order_by('-subs')[0:6]
    tags = tagsData.objects.all().order_by("-tag_uses")[0:10]
    all_blogs = blog_Details.objects.all().order_by("-date")[:20]
    try :
        userData = UserDetail.objects.get(username = request.user)
    except:
        userData =""
    context={
         'title':'Blog',
         'blogs':blogs,
         'authors':authors,
        'tags':tags,
        "all_blogs":all_blogs,
        'userData':userData,
    }
    
    return render(request,'home/index.html',context)

def user_blog(request,username):
    try:
        user_obj = User.objects.get(username=username)
        blogs = blog_Details.objects.filter(blog_creator = user_obj.id).order_by('-blog_clicks')
        blogs_list = []
        for i in blogs:
            blogs_list.append({'title':i.blog_title,'tags':i.tags_input,'date':i.date,'clicks':i.blog_clicks,'slug':i.slug})
        data = {
            'blogs':blogs_list,
        }
        return JsonResponse(data)
    except User.DoesNotExist:
        return redirect('/')

def create_blog(request):
    if not request.user.is_authenticated:
        return redirect("/login/")
    return render(request,"blog/createblog_first.html")

@login_required
def addBlogDetails(request):
    if request.method=='POST':
        title = request.POST.get('blog_title')
        tags = request.POST.get('blog_tags')
        about = request.POST.get('blog_breif')
        thumbnail = request.POST.get('blog_thumbnail_url')
        blog_obj = blog_Details.objects.create(blog_title = title,blog_thumbnail_url=thumbnail,blog_brief=about,tags_input = tags,blog_creator = request.user)
        blog_obj.save()
        messages.success(request,"Details added")
        return redirect('/'+blog_obj.slug+'/update/')
    else:
        messages.warning(request,"POST method not found!")
    return redirect('/')

def main_info_page(request):
    return render(request,'home/main_loder.html')

def search_page(request):
    return render(request,"home/search.html")


def search_process(request):
    if request.method == "POST":
        query = request.POST.get("searchQ")
        searchObj = blog_Details.objects.filter(Q(blog_title__icontains=query)  | Q(blog_brief__icontains=query) | Q(tags_input__icontains=query))
        context = {
            'blogs':searchObj
        }
        return render(request,"home/search.html",context)

'''def like_a_post(request):
    if request.method == "POST":
        post = request.POST.get('id')
        post = blog_Details.objects.filter(id = post)
        likeObj = PostLikes.objects.filter(post = post,liked_by = request.user)
        if likeObj:
            if likeObj.status = "like":
                likeObj.status = 'unlike'
                messages.warning(request,"Like Removed from the post")
        else:
            likeObj = PostLikes.objects.create(post=id,liked_by=request.user,status = 'like')
            messages.success(request,"Like added to the post")
            likeObj.save()

        return redirect()'''
