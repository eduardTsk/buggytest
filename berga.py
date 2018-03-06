import pytest
import selene
from selene.api import *
from selene.browser import set_driver, driver

from selene.conditions import *
from selenium import webdriver

"""
    test_increment() - проверка блока "Счетчик"
    test_insert_item(), test_remove_item() - проверка блока "Список" 
"""
def setup_function(function):
    set_driver(webdriver.Chrome())
    browser.open_url("https://buggy.unitedtraders.team/")
    s('[href="\/login"]').click()
    s('#email').send_keys('satemkuwer@gmail.com')
    s('#password').send_keys('1qaz2wsx')
    s('.btn-success').click()
    print(s(".alert-success").should_be(visible).text)

def teardown_function(function):
    driver().quit()

#  в этом тесте проверим функцию вставки нового айтема в лист
#  новое значение должно появится в конце списка
#
# @pytest.mark.skip()
def test_insert_item():
    items = ss(".col-md-6")

    # это новый айтем
    new_item = "Elastic Hair Ties"
    items[1].find("#title").should_be(visible).send_keys(new_item)

    # заполним соответствующее поле и нажмем на кнопку Добавить
    items[1].find(".btn-success").click()

    item_list = items[1].find_elements_by_tag_name("li")

    # убедимся что заголовок нового айтема появился в конце списка
    assert print(item_list[len(item_list) - 1].text.find(new_item)) is not -1


#  в этом тесте проверим работу инкрементного счетчика, который должен
#  увеличиваться после каждого нажания на кнопку Инкремент
#
# @pytest.mark.skip()
def test_increment():
    # определим значение текущего счетчика
    old_value = int(s('#counter_value').should_be(visible).text)

    # нажимаем на кнопку Инкремент
    s('.site-content [class="col-md-6"]:nth-of-type(1) [type]').click()

    cnt_value = int(s('#counter_value').should_be(visible).text)

    # убедимся что текущий счетчик увеличился на один
    assert cnt_value == (old_value + 1)

#  в этом тесте проверим функцию Удалить из списка
#  пробуем удалить первый айтем
#
# @pytest.mark.skip()
def test_remove_item():
    items = ss(".col-md-6")

    # читаем текущий список айтемов
    item_list = items[1].find_elements_by_tag_name("li")

    # запомним текст первого айтема в списке
    old_item = item_list[0].text

    # нажмем кнопку Удалить в этом айтеме
    item_list[0].find_element_by_link_text("Remove").click()

    # перечитываем заного список айтемов
    item_list = items[1].find_elements_by_tag_name("li")
    # определим текст текущего первого айтема,(он должен быть другим)
    first_item = item_list[0].text

    # убеждаемся что старый первый айтем удалился
    assert old_item != first_item
