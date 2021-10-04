from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.postgres.search import SearchVector

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.utils import translation

from django.utils.text import slugify

# Create your views here.
from .forms import CommentForm, PostForm, SearchForm
from .models import Category, Post, Comment
from django.views.generic import CreateView, UpdateView,DetailView

def post_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    # posts = Post.objects.filter(status='published')
    object_list = Post.published.all()
    paginator = Paginator(object_list, 3)  # 3 posts in each page
    page = request.GET.get('page')

    try:
        posts = paginator.page(page)


    except PageNotAnInteger:
    # If page is not an integer deliver the first page
          posts = paginator.page(1)
    except EmptyPage:
    # If page is out of range deliver last page of results
           posts = paginator.page(paginator.num_pages)

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        # posts = posts.filter(category=category)
        posts = object_list.filter(category=category)


    return render(request,
                  'blog/list.html',
                  {'category': category,
                   'page':page,
                   'categories': categories,
                   'posts': posts})


def post_detail(request, year, month, day, post,):

            # post =get_object_or_404(Post,slug=post_slug)
            post = get_object_or_404(Post, slug=post,
                                     status='published',publish__year=year,
                                     publish__month=month,publish__day=day)
            # List of active comments for this post
            comments = post.comments.filter(active=True)
            new_comment = None

            comment_form = CommentForm(data=request.POST, )



            if request.method == 'POST':
                # A comment was posted

                # data_prepopulated = {'name': comment.name, 'email': comment.email, 'body': comment.body}
                # comments_form = CommentForm(initial=data_prepopulated)
                if comment_form.is_valid() and  request.user.is_authenticated:
                        reply_obj = None
                        # get reply comment id from hidden input
                        try:
                            # id integer e.g. 15
                            reply_id = int(request.POST.get('reply_id'))
                        except:
                            reply_id = None
                        # if reply_id has been submitted get reply_obj id
                        if reply_id:
                            reply_obj = Comment.objects.get(id=reply_id)
                            # if parent object exist
                            if reply_obj:
                                # create replay comment object
                                replay_comment = comment_form.save(commit=False)
                                # assign parent_obj to replay comment
                                replay_comment.parent = reply_obj


                        # Create Comment object but don't save to database yet
                        new_comment = comment_form.save(commit=False)
                        new_comment.author=request.user
                        # Assign the current post to the comment
                        new_comment.post = post
                        # Save the comment to the database
                        new_comment.save()
                else:
                    messages.error(request, 'Error creating your comment')
                    return HttpResponseRedirect("/")

            else:
                 comment_form = CommentForm()
            return render(request,
                        'blog/detail.html',
                        {'post': post,
                         'comments': comments,
                         'new_comment': new_comment,
                         'comment_form': comment_form})
@login_required()
def post_add (request, ):

    if request.method == 'POST':
        post_form = PostForm(data=request.POST)

        if post_form.is_valid():
            # create a post object but don't save to database yet
            new_post = post_form.save(commit=False)
            # assign the current slug and user to the post
            new_post.author = request.user
            new_post.slug = slugify(new_post.title)
            # save post to database
            new_post.save()
            messages.success(request, 'You post will be published after submitted by moderator')
            return HttpResponseRedirect("/")
        else:
            messages.error(request, 'Error creating your post')
            print(messages.get_messages(request))

    else:
        post_form = PostForm()

    return  render(request,'blog/post_add.html',{ 'post_form':post_form,})

@login_required
def post_edit (request,  year, month, day, post):

    # post = get_object_or_404(Post,slug=post_slug)
    post = get_object_or_404(Post, slug=post,
                             status='published', publish__year=year,
                             publish__month=month, publish__day=day)
    post_form = PostForm(request.POST,instance=post)


    if request.method == 'POST':
        if post_form.is_valid() and post.author == request.user :
            post_form.save()
            messages.success(request, 'Post updated successfully')
            return HttpResponseRedirect(reverse('post_list'))
        else:
            messages.error(request, 'Error updating your post')

    else:
        data_prepopulated ={'body':post.body, 'title':post.title,'category':post.category}
        post_form = PostForm(initial=data_prepopulated)

    return render(request, 'blog/post_edit.html', {'post_form': post_form, })
@login_required()
def post_delete (request, year, month, day, post):
    post = get_object_or_404(Post, slug=post,
                             status='published', publish__year=year,
                             publish__month=month, publish__day=day)
    data_prepopulated = {'body': post.body, 'title': post.title, 'category': post.category}
    post_form = PostForm(initial=data_prepopulated)
    if request.method == 'POST':
        post.delete()
        messages.success(request, 'Post deleted successfully')
        return HttpResponseRedirect(reverse('post_list'))
    return render(request, 'blog/post_delete.html', {'post': post,'post_form':post_form })
# class UpdatePostView( LoginRequiredMixin,UserPassesTestMixin,UpdateView):
#     model = Post
#     fields = ['body', 'title', 'category']
#     slug_url_kwarg = 'post_slug'
#     def form_valid(self, form):
#         form.instance.author = self.request.user
#         return super(UpdatePostView, self).form_valid(form)
#     def test_func(self):
#         post = self.get_object()
#         if self.request.user==post.author:
#             return True
#         return False
@login_required()
def comment_edit(request, id):
    comment = get_object_or_404(Comment, id=id)
    comments_form = CommentForm(request.POST,instance=comment)

    if request.method == 'POST':
        if comments_form.is_valid() :
            comments_form.save()
            messages.success(request, 'Comment updated successfully')
            return HttpResponseRedirect(comment.post.get_absolute_url())
        else:
            messages.error(request, 'Error updating your comment')

    else:
        data_prepopulated = { 'email': comment.email, 'body': comment.body}
        comments_form  = CommentForm(initial=data_prepopulated)

    return render(request, 'blog/comment_edit.html', {'comments_form': comments_form,'comment':comment })

# def comment_delete(request, id):
#     comment = get_object_or_404(Comment, id=id)
#     comments_form = CommentForm(request.POST, instance=comment)
#
#     if request.method == 'POST':
#         if comments_form.is_valid() :
#             comments_form.delete()
#             messages.success(request, 'Comment deleted successfully')
#             return HttpResponseRedirect(comment.post.get_absolute_url())
#         else:
#              messages.error(request, 'Error updating your comment'
#     else:
#         data_prepopulated = {'email': comment.email, 'body': comment.body}
#         comments_form = CommentForm(initial=data_prepopulated)
#     return render(request, 'blog/comment_delete.html', {'comments_form': comments_form,'comment':comment })

@login_required()
def comment_delete(request, id):
    comment = get_object_or_404(Comment, id=id)
    comments_form = CommentForm(request.POST,instance=comment)

    if request.method == 'POST':
        if comments_form.is_valid() :
            comment.delete()
            messages.success(request, 'Comment deleted successfully')
            return HttpResponseRedirect(comment.post.get_absolute_url())
        else:
            messages.error(request, 'Error updating your comment')

    else:
        data_prepopulated = { 'email': comment.email, 'body': comment.body}
        comments_form  = CommentForm(initial=data_prepopulated)

    return render(request, 'blog/comment_delete.html', {'comments_form': comments_form,'comment':comment })

# def post_search(request):
#     # search_form = SearchForm()
#     query = None
#     results = []
#     if 'query' in request.POST:
#         # search_form = SearchForm(request.POST)
#         if search_form.is_valid():
#             # query = search_form.cleaned_data['query']
#             results = Post.published.annotate(
#             search=SearchVector('title', 'body'),
#             ).filter(search=query)
#     return render(request, 'blog/list.html',
#             {'search_form': search_form,
#             'query': query,
#             'results': results})
def post_search(request):
 if request.method == "POST":
     query = request.POST['query']
     results = Post.published.annotate(
                 search=SearchVector('title', 'body'),
                 ).filter(search=query)
     return render(request, 'blog/search.html',
            {
            'query': query,
            'results': results
            })
 else:
     return render(request, 'blog/search.html',
                   {

                   })

def selectlanguage(request):
     if request.method == 'POST':
         curr_lunguage = translation.get_language()
         lasturl = request.META.get('HTTP_REFERER')
         lang =request.POST['language']
         translation.activate(lang)
         request.session[translation.LANGUAGE_SESSION_KEY]=lang
         return HttpResponseRedirect('/'+lang)