
from modules.ui.page_objects.order_page_object import Order
import pytest
import time

@pytest.mark.test_ui
def test_ui_course_page_object():
    order = Order()

    order.go_to_the_order('термокилимок', 999)
    order.order_info('Валентин', +3809666666, 'Вибачте будь ласка, пишу автотести =(')

    time.sleep(5)

    assert order.check_title('monobank')

    order.close()







