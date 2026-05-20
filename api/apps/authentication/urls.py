from django.urls import path

from apps.authentication.views import CustomLoginView, CustomLogoutView, CustomTokenVerifyView, CustomTokenRefreshView


urlpatterns = [
    path('login', CustomLoginView.as_view(), name='login'),
    path('logout', CustomLogoutView.as_view(), name='logout'),

    path('token/verify', CustomTokenVerifyView.as_view(),
         name='token_verify'),
    path('token/refresh', CustomTokenRefreshView().as_view(),
         name='token_refresh'),
]
