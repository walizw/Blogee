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
    path ("blog/<int:pk>/update/", views.BlogUpdateAPIView.as_view ()),
    path ("blog/create/", views.BlogCreateAPIView.as_view ())
]
