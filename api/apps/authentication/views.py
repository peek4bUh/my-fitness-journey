from dj_rest_auth.urls import (LoginView as DjRestAuthLoginView,
                               LogoutView as DjRestAuthLogoutView,
                               TokenVerifyView, get_refresh_view)
from drf_spectacular.utils import extend_schema


@extend_schema(tags=["Auth"])
class CustomLoginView(DjRestAuthLoginView):
    """
    Check the credentials and return the JSON Web Token if the credentials
    are valid and authenticated.
    """
    pass


@extend_schema(tags=["Auth"])
class CustomLogoutView(DjRestAuthLogoutView):
    """
    Invalidate the JSON Web Token if the user is authenticated.
    """
    @property
    def allowed_methods(self):
        # The `ACCOUNT_LOGOUT_ON_GET: False` setting is not working as
        # expected, so we need to override the allowed methods to prevent
        # GET requests to the logout endpoint.
        methods = []
        for method in super().allowed_methods:
            if method != 'GET':
                methods.append(method)

        return methods


@extend_schema(tags=["Auth"])
class CustomTokenVerifyView(TokenVerifyView):
    pass


@extend_schema(tags=["Auth"])
class CustomTokenRefreshView(get_refresh_view()):
    pass
