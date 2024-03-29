from selene import browser, have


class Promo:
    def open_main_page(self):
        browser.open('/')
        return self

    def select_the_promobanner(self):
        browser.element(
            '.header-categories__item:nth-child(2) > .header-categories__item-link'
        ).click()
        return self

    def assert_selected_promobanner(self):
        browser.element('.subcategory-or-type__heading-title').should(
            have.text('Распродажа: скидки до 70%')
        )
        return self
