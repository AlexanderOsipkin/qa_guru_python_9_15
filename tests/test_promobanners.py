import allure
from metro_tests_suite.pages.promo_page import Promo


@allure.title('Test promobanner')
def test_promobanners():
    promo_banners = Promo()

    with allure.step('Open main page'):
        promo_banners.open_main_page()

    with allure.step('Select the happy new year promobanner'):
        promo_banners.select_the_promobanner()

    with allure.step('Assert selected promobanner'):
        promo_banners.assert_selected_promobanner()
