from django.urls import path
from . import views

app_name = 'FeedApp'

urlpatterns = [
    path('', views.index,name='index'),
    path('posts',views.posts, name = 'posts'),
    path('all_posts',views.all_posts, name = 'all_posts'),
    path('new_post/',views.new_post, name='new_post'),
    path('profile/',views.profile, name='profile'),
    path('comments/<int:post_id>/', views.comments, name = 'comments')
]