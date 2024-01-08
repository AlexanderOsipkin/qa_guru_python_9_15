from selene import browser, have, be, by

class ProductPage:
    def open_product_page(self):
        browser.open('https://www.dns-shop.ru/')
        return self

    def select_product(self):
        browser.element('[name="q"]').should(be.blank).type('apple iphone 15 pro '
                                                            'max').press_enter()
        return self

