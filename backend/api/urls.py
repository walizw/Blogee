from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from . import views

urlpatterns = [
    path ("users/login/", TokenObtainPairView.as_view ()),
    path ("users/refresh/", TokenRefreshView.as_view ()),
    path ("users/", views.UsersAPIView.as_view ()),
    path ("user/", views.UserCreateAPIView.as_view ()),
    path ("user/<str:name>/", views.UserGetFromNameAPIView.as_view ()),
    path ("user/<int:pk>/blogs/", views.UserBlogsAPIView.as_view ()),
    path ("blogs/", views.BlogsAPIView.as_view ()),
    path ("blog/<int:pk>/", views.BlogAPIView.as_view ()),
    path ("blog/<int:pk>/categories/", views.BlogCategoriesAPIView.as_view ()),
    path ("blog/<int:pk>/posts/", views.BlogPostsAPIView.as_view ()),
    path ("blog/<int:pk>/update/", views.BlogUpdateAPIView.as_view ()),
    path ("blog/<int:pk>/delete/", views.BlogDeleteAPIView.as_view ()),
    path ("blog/create/", views.BlogCreateAPIView.as_view ()),
    path ("category/create/", views.CategoryCreateAPIView.as_view ()),
    path ("category/<int:pk>/", views.CategoryAPIView.as_view ()),
    path ("category/<int:pk>/update/", views.CategoryUpdateAPIView.as_view ()),
    path ("category/<int:pk>/delete/", views.CategoryDeleteAPIView.as_view ()),
    path ("posts/", views.PostsAPIView.as_view ()),
    path ("post/<int:pk>/", views.PostAPIView.as_view ()),
    path ("post/<int:pk>/update/", views.PostUpdateAPIView.as_view ()),
]
