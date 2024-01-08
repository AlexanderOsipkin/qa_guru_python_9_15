from metro_tests_suite.pages.product_page import ProductPage
from selene import browser, be, have


def test_enter_delivery_address():
    browser.open('/')
    browser.element('.header-address .header-address__receive-button').click()
    browser.element('#search-input').type('Санкт-Петербург, Лиговский проспект, 50')
    browser.element('.obtainment-delivery__address .rectangle-button').click()
    # ПРОБЛЕМНЫЙ СЕЛЕКТОР
    browser.element('.header-address .header-address__receive-address').should(
        have.text('Санкт-Петербург, Лиговский проспект, 50')
    )

    # browser.element('.header-main__content .header-address__receive-address').click()
    # browser.element('.obtainment-delivery__input-wrapper #search-input').type(
    #     'Санкт-Петербург, Лиговский проспект, 50'
    # )  # можно добавить замену адреса
    # browser.element('.obtainment-delivery__address > .rectangle-button').with_(
    #     timeout=6.0
    # ).click()
    # browser.element('.header-main__content .header-address__receive-address').click()
    # browser.element('.obtainment-delivery__input-box .reset-input__icon-close').click()
    # browser.element('.obtainment-delivery__input-wrapper #search-input').type(
    #     'Санкт-Петербург, Невский проспект, 88'
    # )  # можно добавить замену адреса
    # browser.element('.obtainment-delivery__apply-btn-desktop').click()


def test_add_product_to_cart_with_search():
    browser.open('/')
    browser.element('.header-main__search .search-bar__input').should(be.blank).type(
        "METRO Chef Мороженое Пломбир ванильный, 2.5кг"
    ).press_enter()
    browser.element('.product-card__content .simple-button').click()
    browser.element('.obtainment-delivery__input-wrapper #search-input').type(
        'Санкт-Петербург, Невский проспект, 14'
    )
    browser.element('.obtainment-delivery__address .rectangle-button').click()
    browser.element('.header-main__cart .header-cart-button').click()
    browser.element('.header-cart-product-card .button-remove').click()
    browser.element('.product-card__content .simple-button').click()


# done переход в раздел каталога "Мясо, птица, колбасы"
def test_catalog():
    browser.open('/')
    browser.element('.header-main__catalog .header-button-catalog').click()
    browser.element('li:nth-child(7) span:nth-child(2)').click()
    browser.element(
        '.slider-main-block__heading--h1 .slider-main-block__heading-title'
    ).should(have.text('Мясо, птица, колбасы'))


# done добавление товара в корзину с выбором самовывоза по предложенному адресу
def test_pickup_with_search():
    browser.open('/')
    browser.element('.header-main__search .search-bar__input').should(be.blank).type(
        "METRO Chef Лапша гречневая, 600г"
    ).press_enter()
    browser.element('.product-card__content .simple-button').click()
    browser.element(
        '.obtainments-list__item:nth-child(2) .obtainments-list__description'
    ).click()
    browser.element('.pickup__apply-btn-desk > .rectangle-button').click()
