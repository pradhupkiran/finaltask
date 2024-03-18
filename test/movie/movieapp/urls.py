from django.urls import path
from . import views
app_name='movie'

urlpatterns = [
    path('home/', views.home,name='home'),
    path('<slug:c_slug>/',views.home,name='products_by_category'),
    path('home/<int:post_id>/',views.post_detail,name='post_detail'),
    path('home/add_post',views.add_post,name='add_post'),
    path('home/my_post',views.my_post,name='my_post'),
    path('edit/<int:post_id>/', views.edit_post, name='edit_post'),
    path('delete/<int:post_id>/', views.delete_post, name='delete_post'),

]