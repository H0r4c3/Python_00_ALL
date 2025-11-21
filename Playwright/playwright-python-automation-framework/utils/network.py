from playwright.sync_api import Page


def mock_json_response(page: Page, pattern: str, json_body: str, status: int = 200) -> None:
    """
    Intercept requests matching pattern and respond with provided JSON.

    pattern: e.g. '**/api/products'
    json_body: a JSON string
    """
    def _handler(route):
        route.fulfill(
            status=status,
            content_type="application/json",
            body=json_body,
        )

    page.route(pattern, _handler)
