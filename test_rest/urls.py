from django.urls import path
from .views import post_view, post_detail, PostApiView, PostDetail
urlpatterns = [
    # path('', post_view, name='post'),
    # path('detail/<int:pk>', post_detail, name='post_detail')
    path('', PostApiView.as_view(), name='post'),
    path('detail/<int:pk>', PostDetail.as_view(), name='post_detail')
]