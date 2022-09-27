import time

import allure


@allure.description('Denomination buttons check')
@allure.tag('Positive')
def test_buttons(my_fixture):
    with allure.step("Site open"):
        my_fixture.site_open()
        time.sleep(1)

    with allure.step("500 button default status check"):
        assert my_fixture.search.card_500_button().get_attribute("class") == \
               "par-options__button"
    my_fixture.search.card_500_button().click()
    time.sleep(1)
    with allure.step("500 button clicked status check"):
        assert my_fixture.search.card_500_button().get_attribute("class") == \
               "par-options__button par-options__button--active"
    with allure.step("Card value input after click 500 check"):
        assert my_fixture.search.card_value_input().get_attribute("value") == '500'

    with allure.step("1000 button default status check"):
        assert my_fixture.search.card_1000_button().get_attribute("class") == \
               "par-options__button"
    my_fixture.search.card_1000_button().click()
    time.sleep(1)
    with allure.step("1000 button clicked status check"):
        assert my_fixture.search.card_1000_button().get_attribute("class") == \
               "par-options__button par-options__button--active"
    with allure.step("Card value input after click 1000 check"):
        assert my_fixture.search.card_value_input().get_attribute("value") == '1000'

    with allure.step("2000 button default status check"):
        assert my_fixture.search.card_2000_button().get_attribute("class") == \
               "par-options__button"
    my_fixture.search.card_2000_button().click()
    time.sleep(1)
    with allure.step("2000 button clicked status check"):
        assert my_fixture.search.card_2000_button().get_attribute("class") == \
               "par-options__button par-options__button--active"
    with allure.step("Card value input after click 2000 check"):
        assert my_fixture.search.card_value_input().get_attribute("value") == '2000'

    with allure.step("3000 button default status check"):
        assert my_fixture.search.card_3000_button().get_attribute("class") == \
               "par-options__button"
    my_fixture.search.card_3000_button().click()
    time.sleep(1)
    with allure.step("3000 button clicked status check"):
        assert my_fixture.search.card_3000_button().get_attribute("class") == \
               "par-options__button par-options__button--active"
    with allure.step("Card value input after click 3000 check"):
        assert my_fixture.search.card_value_input().get_attribute("value") == '3000'

    with allure.step("5000 button default status check"):
        assert my_fixture.search.card_5000_button().get_attribute("class") == \
               "par-options__button"
    my_fixture.search.card_5000_button().click()
    time.sleep(1)
    with allure.step("5000 button clicked status check"):
        assert my_fixture.search.card_5000_button().get_attribute("class") == \
               "par-options__button par-options__button--active"
    with allure.step("Card value input after click 5000 check"):
        assert my_fixture.search.card_value_input().get_attribute("value") == '5000'

    with allure.step("10000 button default status check"):
        assert my_fixture.search.card_10000_button().get_attribute("class") == \
               "par-options__button"
    my_fixture.search.card_10000_button().click()
    time.sleep(1)
    with allure.step("10000 button clicked status check"):
        assert my_fixture.search.card_10000_button().get_attribute("class") == \
               "par-options__button par-options__button--active"
    with allure.step("Card value input after click 10000 check"):
        assert my_fixture.search.card_value_input().get_attribute("value") == '10000'
