from flask_restx import Api

from api.config import api_restx


auth_ns = api_restx.namespace(name="Authentication Operations", path="/auth")
users_ns = api_restx.namespace(name="Users Operations", path="/users")
programs_ns = api_restx.namespace(name="Programs Operations", path="/programs")


class NamespaceManager:
    """Class to manage all namespaces."""

    _namespaces = [auth_ns, users_ns, programs_ns]

    @classmethod
    def register_all(cls, api: Api):
        """Register all namespaces to the Flask-restx API."""
        from api import modules

        for ns in cls._namespaces:
            api.add_namespace(ns)
