# -*- coding:utf8 -*-
from category import Category


class ShopCategory(Category):
    def __init__(self, category_id, parent_category_id, root_id, category_name, add_cart_item_cnt, cate_item_cnt,
                 cate_uv, order_rate, is_children):
        """
        店铺本身经营的一些类目
        :param category_id:
        :param parent_category_id:
        :param root_id:
        :param category_name:
        :param add_cart_item_cnt: 加购数量
        :param cate_item_cnt:
        :param cate_uv:
        :param order_rate:
        :param is_children
        """
        super(ShopCategory, self).__init__(category_id, parent_category_id, root_id, category_name)
        self.add_cart_item_cnt = add_cart_item_cnt
        self.cate_item_cnt = cate_item_cnt
        self.cate_uv = cate_uv
        self.order_rate = order_rate
        self.is_children = is_children
        # def __str__(self):
        #     pass
