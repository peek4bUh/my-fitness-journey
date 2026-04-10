from dj_rest_auth.urls import (LoginView as DjRestAuthLoginView,
                               LogoutView as DjRestAuthLogoutView)


class CustomLoginView(DjRestAuthLoginView):
    """
    Check the credentials and return the JSON Web Token if the credentials
    are valid and authenticated.
    """
    pass


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
