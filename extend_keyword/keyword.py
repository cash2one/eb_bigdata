# -*- coding:utf8 -*-
class Keyword:
    def __init__(self, keyword, click_rate, click_uv, order_num, p4p_ref_price, pay_rate, suv, tm_click_rate,
                 info_cycle, cycle_start_date, cycle_end_date, keyword_id=0):
        self.keyword = keyword
        self.keyword_id = keyword_id
        self.click_rate = click_rate
        self.click_uv = click_uv
        self.order_num = order_num
        self.p4p_ref_price = p4p_ref_price
        self.pay_rate = pay_rate
        self.suv = suv
        self.tm_click_rate = tm_click_rate
        self.info_cycle = info_cycle
        self.cycle_start_date = cycle_start_date
        self.cycle_end_date = cycle_end_date
