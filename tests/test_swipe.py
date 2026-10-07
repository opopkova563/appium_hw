import allure
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@allure.feature("Swipe Test")
@allure.story("Swipe to Calendar")
def test_swipe(driver):
    with allure.step("Загрузка приложения:"):
        WebDriverWait(driver, 120).until(
            EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("USER APPS")')))

    try:
        while True:

            with allure.step("Поиск элементов"):
                elements = driver.find_elements(AppiumBy.ID, "com.csdroid.pkg:id/tv_title")
                previous_title = elements[0].text
                print("previous_title: " + previous_title)
            with allure.step("Выполнение свайпа"):
                driver.swipe(elements[2].rect['x'], elements[2].rect['y'], elements[0].rect['x'], elements[0].rect['y'])

            with allure.step("Поиск элементов после свайпа"):
                elements = driver.find_elements(AppiumBy.ID, "com.csdroid.pkg:id/tv_title")
                element_names = [name.text for name in elements]
                current_title = elements[0].text
                print("current_title: " + current_title)

            with allure.step("Если найден Calendar, нажать на него"):
                if 'Calendar' in element_names:
                    elements[element_names.index('Calendar')].click()
                    break

            with allure.step("Проверить, изменился ли список"):
                if current_title == previous_title:
                    raise RuntimeError(
                        "Достигнут конец списка: приложение «Календарь» не найдено."
                    )

    except NoSuchElementException as error:
        raise RuntimeError("Не удалось найти приложение «Календарь».")\
    from error
