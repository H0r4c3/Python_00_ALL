from typing import Any, Dict, Optional
from playwright.sync_api import APIRequestContext, APIResponse


class APIClient:
    """Thin wrapper around Playwright APIRequestContext."""

    def __init__(self, request_context: APIRequestContext) -> None:
        self.request = request_context

    def get(self, url: str, params: Optional[Dict[str, Any]] = None) -> APIResponse:
        return self.request.get(url, params=params)

    def post(self, url: str, data: Optional[Dict[str, Any]] = None) -> APIResponse:
        return self.request.post(url, data=data)

    def put(self, url: str, data: Optional[Dict[str, Any]] = None) -> APIResponse:
        return self.request.put(url, data=data)

    def delete(self, url: str) -> APIResponse:
        return self.request.delete(url)
