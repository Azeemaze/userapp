from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.shortcuts import render,HttpResponse,redirect,get_object_or_404,HttpResponseRedirect
from django.views.generic import ListView,DetailView,CreateView
from app.forms import Registration,PostForm
from app.models import Profile,Post
from userrlogin import settings
from django.urls import reverse_lazy,reverse



# Create your views here.

# def home(request):
#     # return HttpResponse("Welcome")
#     return render(request,'app/home.html')

class HomeView(ListView):
    model = Post
    template_name = 'app/home.html'
    ordering = ['created_at']


def registration(request,):
    if request.method == "POST":
        form = Registration(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            if form.cleaned_data['pswd']==form.cleaned_data['conf_pswd']:
                if User.objects.filter(email=form.cleaned_data['email']).exists():
                    return redirect('registration')
                else:
                    user = User.objects.create_user(username=form.cleaned_data['username'],
                                                        email=form.cleaned_data['email'],
                                                        password=form.cleaned_data['pswd'])
                    user.save()
                    profile=Profile(user=user,
                                    contact_no=form.cleaned_data['contact_ph'],
                                    place = form.cleaned_data['place'])
                    profile.save()
                    return HttpResponse("Your account successfully created")
                    return redirect('signin')
            else:
                print("Password mismatch")
                return redirect('registration')
        else:
            print("Form incomplete")
            return redirect('registration')
    else:
        form = Registration()
        r_path = 'app/signup.html'
        return render(request,r_path,{'form':form})

def login(request):
    if request.method == "POST":
        user_name = request.POST['username']
        login_password = request.POST['password']
        print(user_name, ":", login_password)
        if User.objects.filter(username=user_name).exists():
            user = User.objects.get(username=user_name)
            if user.check_password(login_password):
                if user:
                    auth.login(request, user)
                    request.session['user_status']='logged in'
                    request.session['user_name']=user_name
                    return render(request,'app/welcome.html',{'status':request.session['user_status'], 'user': request.session['user_name']})
            else:
                return render(request, 'app/signin.html')
        else:
            return render(request, 'app/signin.html')
    else:
        return render(request, 'app/signin.html')


def LikeView(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True
    return HttpResponseRedirect(reverse('article-detail', args=[str(pk)]))
class Article_View(DetailView):
    model = Post
    template_name = 'app/articleview.html'

    def get_context_data(self, *args, **kwargs):
        cat_menu = Post.objects.all()
        context = super(Article_View, self).get_context_data(*args, **kwargs)
        stuff = get_object_or_404(Post, id=self.kwargs['pk'])
        total_likes = stuff.total_likes()

        liked = False
        if stuff.likes.filter(id=self.request.user.id).exists():
            liked = True
        context["cat_menu"] = cat_menu
        context["total_likes"] = total_likes
        context["liked"] = liked
        return context

class AddPost(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'app/add_post.html'
    # fields = '__all__'
    success_url = reverse_lazy('home')

# @login_required
#
# def userpost(request):
#     pst = Post.objects.all()
#     return render(request, 'app/user
#
#     form = PostForm(request.POST or None)
#     if request.method == "POST":
#         if form.is_valid():
#             form.instance.user = request.user
#             form.save()
#             return HttpResponse("Your post was successfully created!")
#         else:
#             return HttpResponse('Please correct the error below.')
#     else:
#         form = PostForm()
#     return render(request, "app/welcome.html", context={"form": form})
def logout(request):
    auth.logout(request)
    return redirect('signin')