from django.urls import path
from apiapplication import  views

urlpatterns = [
    path('post/',views.PostListView.as_view()),
    path('post/<int:pk>',views.PostDetailView.as_view()),
    path('comment/',views.CommentListView.as_view()),
    path('comment/<int:pk>',views.CommentDetailView.as_view()),
    path('postlist/',views.PostView.as_view()),
    path('postlist/<int:pk>',views.PostViewId.as_view()),

]
