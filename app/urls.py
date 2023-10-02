from django.urls import path
from .import views
from .views import HomeView,Article_View,AddPost,LikeView

urlpatterns = [
    # path('home/',views.home,name='home'),
    path('HomeView',HomeView.as_view(), name='home'),
    path('registration/',views.registration,name='registration'),
    path('signin/',views.login,name='signin'),
    path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout'),
    path('article/<int:pk>',Article_View.as_view(),name='article-detail'),
    path('addpost/', AddPost.as_view(), name='addpost'),
    path('like/<int:pk>', LikeView, name='like_post'),

    # path('userpost/',views.userpost,name='userpost'),
    # path('post_create',views.post_create,name='post_create')


]