from django.urls import path

from dj_rest_auth.app_settings import api_settings

from apps.authentication.views import CustomLoginView, CustomLogoutView


urlpatterns = [
    # URLs that do not require a session or valid token
    path('login', CustomLoginView.as_view(), name='login'),

    # URLs that require a user to be logged in with a valid session / token.
    path('logout', CustomLogoutView.as_view(), name='logout'),
]

if api_settings.USE_JWT:
    from rest_framework_simplejwt.views import TokenVerifyView

    from dj_rest_auth.jwt_auth import get_refresh_view

    urlpatterns += [
        path('token/verify', TokenVerifyView.as_view(),
             name='token_verify'),
        path('token/refresh', get_refresh_view().as_view(),
             name='token_refresh'),
    ]
