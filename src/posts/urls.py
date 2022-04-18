from django.urls import path, include
from posts.views import BookHome, BookPostCreate, BookPostUpdate, BookPostDetail, BookPostDelete

app_name = "posts"

urlpatterns = [
    path('', BookHome.as_view(), name="home"),
    path('create/', BookPostCreate.as_view(), name="create"),
    path('<str:slug>/', BookPostDetail.as_view(), name='detail'),
    path('edit/<str:slug>/', BookPostUpdate.as_view(), name="edit"),
    path('delete/<str:slug>/', BookPostDelete.as_view(), name="delete"),
]