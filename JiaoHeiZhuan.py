"""
计算用的变量命名集
"""


class JiaoHeiLu:
    """
    包含有关建造焦黑炉所需的一系列方法
    """
    def __init__(self, JiaoZhuTai_Num: int = 1, ZhuZaoPen_Num: int = 1, PaiYeKou_Num: int = 1):
        # a = 焦黑砖
        # b = 玻璃
        # c = 方块个数
        self.JiaoZhuTai = {'a': 7, 'c': JiaoZhuTai_Num}
        self.ZhuZaoPen = {'a': 7, 'c': ZhuZaoPen_Num}
        self.PaiYeKou = {'a': 6, 'c': PaiYeKou_Num}
        self.JiaoHeiChuGuan = {'a': 8, 'b': 1, 'c': 1}
        self.KongZhiQi = {'a': 8, 'c': 1}
        self.JiaoZhuKou = {'a': 3, 'c': (self.JiaoZhuTai['c'] + self.ZhuZaoPen['c'])}
        self.JiaoHeiShiZhuan = {'a': 4, 'c': 1}
        self.block = [self.JiaoZhuTai, self.ZhuZaoPen, self.PaiYeKou,
                      self.JiaoHeiChuGuan, self.KongZhiQi, self.JiaoZhuKou,
                      self.JiaoHeiShiZhuan]

    def __OtherSum(self) -> int:
        return (self.JiaoZhuTai['c'] + self.ZhuZaoPen['c'] + self.PaiYeKou['c'] +
                self.JiaoHeiChuGuan['c'] + self.KongZhiQi['c'] + self.JiaoZhuKou['c'])

    def BuildNeed_Num(self, area: int, height: int) -> int:
        """
        建造area大小,height高所需的焦黑砖块数量
        :param area:
        :param height:
        """
        self.JiaoHeiShiZhuan['c'] = area * (area + 4 * height)
        # 原公式：焦黑砖个数 = 底部（area ** 2） + 四周（（area + 2） ** 2 - area ** 2 - 4）
        self.JiaoHeiShiZhuan['c'] -= self.__OtherSum()
        zhuan_num = 0
        boli_num = self.JiaoHeiChuGuan['c']
        for i in self.block:
            zhuan_num += i['c'] * i['a']
        return {'a': zhuan_num, 'b': boli_num}


def CaiLiao_Num(zhuan: int, boli: int) -> None:
    """
    输出焦石砖对应水泥所需沙子，砂砾与黏土数量
    :param boli:
    :param zhuan:
    """
    print(f"需要:\n"
          f"{zhuan * 4 + boli}个沙子，\n"
          f"{zhuan * 4}个砂砾，\n"
          f"{zhuan}个黏土块即{zhuan * 4}个黏土")
