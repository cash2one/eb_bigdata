# -*- coding: UTF-8 -*-
import json
from category.category import Category
from category.shop_category import ShopCategory


def decode_item(json_item, is_children=0):
    shop_cat = ShopCategory(category_id=json_item["cateId"], parent_category_id=json_item["parentCateId"], root_id="",
                            category_name=json_item['cateName'], add_cart_item_cnt=json_item['addCartItemCnt'],
                            cate_item_cnt=json_item['cateItemCnt'], cate_uv=json_item['cateUv'],
                            order_rate=json_item['orderRate'], is_children=is_children)
    return shop_cat


def decode(json_str):
    """
    解析店铺类目的json字符串
    :param json_str:店铺类目的json字符串
    :return:
    """
    json_data = json.loads(json_str)
    cate_list = json_data['data']['list']
    cate_results = []
    for cate in cate_list:
        shop_cat = decode_item(cate)
        cate_results.append(shop_cat)
        children_items = cate['children']
        if len(children_items) > 0:
            for ci in children_items:
                sub_shop_cat = decode_item(ci,1)
                cate_results.append(sub_shop_cat)
    return cate_results


def test():
    jsonstr = '''{"data":{"list":[{"cateName":"办公家具","orderRate":0.0176,"addCartItemCnt":79,"children":[{"cateName":"文件柜","orderRate":0.0182,"addCartItemCnt":30,"children":[],"cateId":50001399,"parentCateId":211503,"cateItemCnt":44,"cateUv":330},{"cateName":"更衣柜","orderRate":0.0142,"addCartItemCnt":36,"children":[],"cateId":50015429,"parentCateId":211503,"cateItemCnt":24,"cateUv":211},{"cateName":"办公电脑桌","orderRate":0.0345,"addCartItemCnt":13,"children":[],"cateId":211508,"parentCateId":211503,"cateItemCnt":12,"cateUv":87},{"cateName":"排椅系列","orderRate":0.0000,"addCartItemCnt":0,"children":[],"cateId":50015512,"parentCateId":211503,"cateItemCnt":3,"cateUv":17},{"cateName":"餐桌椅系列","orderRate":0.0000,"addCartItemCnt":0,"children":[],"cateId":50015511,"parentCateId":211503,"cateItemCnt":2,"cateUv":3},{"cateName":"保险柜（新增）","orderRate":0.0000,"addCartItemCnt":0,"children":[],"cateId":50023078,"parentCateId":211503,"cateItemCnt":6,"cateUv":3},{"cateName":"休闲椅","orderRate":0.0000,"addCartItemCnt":0,"children":[],"cateId":50015472,"parentCateId":211503,"cateItemCnt":4,"cateUv":2},{"cateName":"组合\/屏风工作位","orderRate":0.0000,"addCartItemCnt":0,"children":[],"cateId":50015437,"parentCateId":211503,"cateItemCnt":1,"cateUv":1},{"cateName":"阅览桌","orderRate":0.0000,"addCartItemCnt":0,"children":[],"cateId":50015439,"parentCateId":211503,"cateItemCnt":1,"cateUv":1},{"cateName":"报刊架","orderRate":0.0000,"addCartItemCnt":0,"children":[],"cateId":50015477,"parentCateId":211503,"cateItemCnt":1,"cateUv":1},{"cateName":"大班台\/主管桌","orderRate":0.0000,"addCartItemCnt":0,"children":[],"cateId":50001391,"parentCateId":211503,"cateItemCnt":0,"cateUv":0},{"cateName":"钥匙箱","orderRate":0.0000,"addCartItemCnt":0,"children":[],"cateId":50015430,"parentCateId":211503,"cateItemCnt":1,"cateUv":0},{"cateName":"矮柜","orderRate":0.0000,"addCartItemCnt":0,"children":[],"cateId":50015433,"parentCateId":211503,"cateItemCnt":1,"cateUv":0},{"cateName":"沙发","orderRate":0.0000,"addCartItemCnt":0,"children":[],"cateId":50015442,"parentCateId":211503,"cateItemCnt":0,"cateUv":0},{"cateName":"其它配件","orderRate":0.0000,"addCartItemCnt":0,"children":[],"cateId":50015507,"parentCateId":211503,"cateItemCnt":1,"cateUv":0},{"cateName":"其他柜类（新增）","orderRate":0.0000,"addCartItemCnt":0,"children":[],"cateId":50023084,"parentCateId":211503,"cateItemCnt":1,"cateUv":0}],"cateId":211503,"parentCateId":50020611,"cateItemCnt":102,"cateUv":626},{"cateName":"校园教学家具","orderRate":0.0000,"addCartItemCnt":2,"children":[{"cateName":"其他","orderRate":0.0000,"addCartItemCnt":2,"children":[],"cateId":50020817,"parentCateId":50020679,"cateItemCnt":2,"cateUv":57},{"cateName":"课桌椅","orderRate":0.0000,"addCartItemCnt":0,"children":[],"cateId":50020813,"parentCateId":50020679,"cateItemCnt":1,"cateUv":9}],"cateId":50020679,"parentCateId":50020611,"cateItemCnt":3,"cateUv":66},{"cateName":"超市家具","orderRate":0.0000,"addCartItemCnt":0,"children":[{"cateName":"寄存柜","orderRate":0.0000,"addCartItemCnt":0,"children":[],"cateId":50020704,"parentCateId":50020612,"cateItemCnt":6,"cateUv":37}],"cateId":50020612,"parentCateId":50020611,"cateItemCnt":6,"cateUv":37},{"cateName":"货架\/展柜","orderRate":0.0286,"addCartItemCnt":5,"children":[{"cateName":"图书音像货架","orderRate":0.0323,"addCartItemCnt":5,"children":[],"cateId":50023197,"parentCateId":50015518,"cateItemCnt":3,"cateUv":31},{"cateName":"仓储货架","orderRate":0.0000,"addCartItemCnt":0,"children":[],"cateId":50007016,"parentCateId":50015518,"cateItemCnt":2,"cateUv":4}],"cateId":50015518,"parentCateId":50020611,"cateItemCnt":5,"cateUv":35},{"cateName":"餐饮\/烘焙家具","orderRate":0.0000,"addCartItemCnt":0,"children":[{"cateName":"餐台椅","orderRate":0.0000,"addCartItemCnt":0,"children":[],"cateId":50020716,"parentCateId":50020672,"cateItemCnt":0,"cateUv":0}],"cateId":50020672,"parentCateId":50020611,"cateItemCnt":0,"cateUv":0},{"cateName":"邮费","orderRate":0.0000,"addCartItemCnt":0,"children":[],"cateId":50023725,"parentCateId":50023724,"cateItemCnt":1,"cateUv":0},{"cateName":"发廊\/美容家具","orderRate":0.0000,"addCartItemCnt":0,"children":[{"cateName":"美容\/美发床","orderRate":0.0000,"addCartItemCnt":0,"children":[],"cateId":50020797,"parentCateId":50020677,"cateItemCnt":0,"cateUv":0}],"cateId":50020677,"parentCateId":50020611,"cateItemCnt":0,"cateUv":0}]},"code":0,"traceSql":["select stat_date statDate, parent_cate_id parentCateId, cate_id cateId, on_itm_cnt_1d_001 cateItemCnt, ipv_uv_1d_001 cateUv, cart_itm_qty_1d_001 addCartItemCnt, vst_crt_byr_rate_1d_001 orderRate, cate_flag cateFlag FROM do_tao_mbr_par_cate_d WHERE user_id=1958019580 and stat_date='2017-01-03 00:00:00' and cate_flag=2; spend(ms):74","select parent_id parentCateId, cate_id cateId, cate_name cateName, is_leaf isLeaf from do_tao_cate_dim where stat_date='2017-01-03 00:00:00' and cate_id in ( 211503 , 50015518 , 50020612 , 50020672 , 50020677 , 50020679 , 50023725 ); spend(ms):4","select stat_date statDate, parent_cate_id parentCateId, cate_id cateId, on_itm_cnt_1d_001 cateItemCnt, ipv_uv_1d_001 cateUv, cart_itm_qty_1d_001 addCartItemCnt, vst_crt_byr_rate_1d_001 orderRate, cate_flag cateFlag FROM do_tao_mbr_par_cate_d WHERE user_id=1958019580 and stat_date='2017-01-03 00:00:00' and cate_flag=0 and parent_cate_id in ( 211503 , 50015518 , 50020612 , 50020672 , 50020677 , 50020679 , 50023725 ); spend(ms):11","select parent_id parentCateId, cate_id cateId, cate_name cateName, is_leaf isLeaf from do_tao_cate_dim where stat_date='2017-01-03 00:00:00' and cate_id in ( 211508 , 50001391 , 50001399 , 50015429 , 50015430 , 50015433 , 50015437 , 50015439 , 50015442 , 50015472 , 50015477 , 50015507 , 50015511 , 50015512 , 50023078 , 50023084 , 50007016 , 50023197 , 50020704 , 50020716 , 50020797 , 50020813 , 50020817 , 50023725 ); spend(ms):4"]}'''
    scate_datas = decode(jsonstr)
    for sc in scate_datas:
        print sc.cate2dict()['is_children']


if __name__ == '__main__':
    test()
