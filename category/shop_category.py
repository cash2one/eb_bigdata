# -*- coding:utf8 -*-
from category import Category


class ShopCategory(Category):
    def __init__(self, category_id, parent_category_id, root_id, category_name, add_cart_item_cnt, cate_item_cnt,
                 cate_uv, order_rate, is_children, client_id = 0):
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
        :param is_children:
        :param client_id: 用户id在decode的时候一般获取不到
        """
        Category.__init__(self, category_id, parent_category_id, root_id, category_name)
        self.add_cart_item_cnt = add_cart_item_cnt
        self.cate_item_cnt = cate_item_cnt
        self.cate_uv = cate_uv
        self.order_rate = order_rate
        self.is_children = is_children
        self.client_id = client_id

    def cate2dict(self):
        cate_dict = {'cate_id': self.category_id,
                     'add_cart_item_cnt': self.add_cart_item_cnt,
                     'cate_item_cnt': self.cate_item_cnt,
                     'cate_uv': self.cate_uv,
                     'order_rate': self.order_rate,
                     'is_children': self.is_children,
                     'client_id': self.client_id}
        return cate_dict
