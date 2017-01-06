# -*- coding:utf8 -*-


class Category(object):
    """
    电商类目
    """
    def __init__(self, category_id, parent_category_id, root_id, category_name):
        """
        init 方法
        :param category_id:类目本身id
        :param parent_category_id:类目上一层类目的id
        :param root_id:跟类目id
        :param category_name:类目名
        """
        self.id = category_id
        self.higher_id = parent_category_id
        self.root_id = root_id
        self.category_name = category_name

    def __str__(self):
        return "category_id:{0} higher_category_id:{1} root_id:{2} category_name:{3}".format(self.id, self.higher_id, self.root_id, unicode.encode(self.category_name,"utf-8"))

