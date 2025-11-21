import pytest
from pages.shop_page import ShopPage


@pytest.mark.regression
def test_add_product_to_cart(page, config):
    base_url = config["base_url"]
    shop_page = ShopPage(page)

    shop_page.open(base_url)
    shop_page.select_product("Hoodie")
    shop_page.add_to_cart()
    shop_page.assert_cart_visible()
