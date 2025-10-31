from typing import Any, Dict, Optional
from dataclasses import dataclass
import requests
from flask import jsonify, make_response


@dataclass
class HttpResult:
    status_code: Optional[int]
    json: Optional[Any] = None
    text: Optional[str] = None
    headers: Dict[str, Any] = None
    ok: bool = False
    error: Optional[str] = None


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
    ) -> HttpResult:
        url = self._build_url(path)
        hdrs = self.default_headers.copy()
        if headers:
            hdrs.update(headers)
        try:
            resp = self.session.request(
                method, url, json=json, params=params, headers=hdrs
            )
            # do not raise for status here if you want the raw response,
            # but keep raise_for_status to convert 4xx/5xx into exceptions if preferred
            resp.raise_for_status()
            content_type = resp.headers.get("Content-Type", "")
            body_json = resp.json() if "application/json" in content_type else None
            return HttpResult(
                status_code=resp.status_code,
                json=body_json,
                text=resp.text,
                headers=dict(resp.headers),
                ok=resp.ok,
                error=None,
            )
        except requests.RequestException as e:
            # try to extract info from response attached to the exception
            resp = getattr(e, "response", None)
            status = getattr(resp, "status_code",
                             None) if resp is not None else None
            text = getattr(resp, "text", None) if resp is not None else str(e)
            headers = dict(resp.headers) if resp is not None and getattr(
                resp, "headers", None) else {}
            return HttpResult(
                status_code=status,
                json=None,
                text=text,
                headers=headers,
                ok=False,
                error=str(e),
            )

    def get(self,
            path: str,
            params: Optional[Dict[str, Any]] = None,
            headers: Optional[Dict[str, str]] = None) -> HttpResult:
        return self._request("GET", path, json=None, params=params, headers=headers)

    def post(self,
             path: str,
             json: Optional[Dict[str, Any]] = None,
             params: Optional[Dict[str, Any]] = None,
             headers: Optional[Dict[str, str]] = None) -> HttpResult:
        return self._request("POST", path, json=json, params=params, headers=headers)

    def put(self,
            path: str,
            json: Optional[Dict[str, Any]] = None,
            params: Optional[Dict[str, Any]] = None,
            headers: Optional[Dict[str, str]] = None) -> HttpResult:
        return self._request("PUT", path, json=json, params=params, headers=headers)

    def delete(self,
               path: str,
               params: Optional[Dict[str, Any]] = None,
               headers: Optional[Dict[str, str]] = None) -> HttpResult:
        return self._request("DELETE", path, json=None, params=params, headers=headers)
