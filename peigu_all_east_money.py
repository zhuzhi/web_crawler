#!/usr/bin/python
# coding: utf-8
import urllib
import pandas
import ast


def get_peigu_all_east_money(num=10000):

    """
    :param num:
    :type num: int
    :return: df_peigu_all_east_money
    """

    url_peigu_all_east_money = u"http://datainterface.eastmoney.com/EM_DataCenter/JS.aspx?type=NS&sty=NSA&st=6&sr=-1&p=1&ps=NUM"
    url_peigu_all_east_money = url_peigu_all_east_money.replace("NUM", str(num))

    page_peigu_all_east_money = urllib.urlopen(url_peigu_all_east_money)

    peigu_all_east_money = page_peigu_all_east_money.read()

    peigu_all_east_money = peigu_all_east_money.strip("\(").strip("\)")

    peigu_all_east_money = ast.literal_eval(peigu_all_east_money)

    peigu_all_east_money = [element.split(",") for element in peigu_all_east_money]

    col_names = ["unknow0", "GSDM", "ZQDM", "ZQMC", "PGDM",
                 "PGMC", "PGBL", "PGJG", "GB_BEF", "PGSL",
                 "GB_AFT", "GQDJR", "JKQSR", "JKJZR", "PGSSR",
                 "CQJZR", "SJMZZE", "SJMZJE", "CXFS", "PGGGR",
                 "ZXJG", "unknow1"]
    # GSDM: 公司代码
    # stock_code: 股票代码
    # stock_name: 股票名称
    # PGDM: 配股代码
    # PGMC: 配股名称
    # PGBL: 配股比例（10股配*）
    # PGJG: 配股价格
    # GB_BEF: 配股前股本
    # PGSL: 配股数量
    # GB_AFT: 配股后股本
    # GQDJR_T: 股权登记日，T日
    # JKQSR: 缴款起始日，T+1日
    # JKJZR: 缴款截止日, T+5日
    # PGSSR: 配股上市流通日
    # CQJZR： 除权基准日
    # SJMZZE: 实际募资总额
    # SJMZJE: 实际募资净额
    # CXFS: 承销方式
    # PGGGR: 刊登配股说明书及摘要、配股发行公告及网上路演公告日， T-2日
    # ZXJG: 最新价格
    # unknow0: 未知代码
    # unknow1: 未知代码，似乎和盈亏有关。在东方财富网是上，最新价黑色此列为空，绿色此列为负，红色此列为正。具体数值意义未知。

    df_peigu_all_east_money = pandas.DataFrame(peigu_all_east_money, columns=col_names)

    return df_peigu_all_east_money

peigu_all = get_peigu_all_east_money(num=10000)
peigu_all.to_csv(path_or_buf="./peigu_all_east_money", sep=",", index=True)