# -*- coding:utf8 -*-
from keyword import Keyword


class CategoryExKeyword(Keyword):
    def __init__(self, keyword, click_rate, click_uv, order_num, p4p_ref_price, pay_rate, suv, tm_click_rate,
                 info_cycle, cycle_start_date, cycle_end_date, keyword_group, category_id, keyword_id=0):
        Keyword.__init__(self, click_rate, click_uv, order_num, p4p_ref_price, pay_rate, suv, tm_click_rate,
                         info_cycle, cycle_start_date, cycle_end_date, keyword_id)
        self.keyword_group = keyword_group
        self.category_id = category_id
