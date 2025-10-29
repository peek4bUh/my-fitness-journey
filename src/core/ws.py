from typing import Any, Dict, Optional
import requests


class WebService:

    def __init__(self) -> None:
        self.base_url = "http://localhost:7777"
        self.session = requests.Session()
        self.default_headers = {"Content-Type": "application/json"}

    def _build_url(self, path: str) -> str:
        if path.startswith("http://") or path.startswith("https://"):
            return path
        if not self.base_url:
            return path
        return f"{self.base_url}/{path.lstrip('/')}"

    def _request(
        self,
        method: str,
        path: str,
        json: Optional[Dict[str, Any]] = None,
        params: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> Any:
        url = self._build_url(path)
        hdrs = self.default_headers.copy()
        if headers:
            hdrs.update(headers)
        try:
            resp = self.session.request(
                method, url, json=json, params=params, headers=hdrs
            )
            resp.raise_for_status()
            content_type = resp.headers.get("Content-Type", "")
            if "application/json" in content_type:
                return {"json": resp.json(), "status_code": resp.status_code}
            return resp.text
        except requests.RequestException as e:
            return {"error": str(e), "status_code": getattr(e.response, "status_code", None)}

    def get(self,
            path: str,
            params: Optional[Dict[str, Any]] = None,
            headers: Optional[Dict[str, str]] = None) -> Any:
        return self._request("GET", path, json=None, params=params, headers=headers)

    def post(self,
             path: str,
             json: Optional[Dict[str, Any]] = None,
             params: Optional[Dict[str, Any]] = None,
             headers: Optional[Dict[str, str]] = None) -> Any:
        return self._request("POST", path, json=json, params=params, headers=headers)

    def put(self,
            path: str,
            json: Optional[Dict[str, Any]] = None,
            params: Optional[Dict[str, Any]] = None,
            headers: Optional[Dict[str, str]] = None) -> Any:
        return self._request("PUT", path, json=json, params=params, headers=headers)

    def delete(self,
               path: str,
               params: Optional[Dict[str, Any]] = None,
               headers: Optional[Dict[str, str]] = None) -> Any:
        return self._request("DELETE", path, json=None, params=params, headers=headers)
