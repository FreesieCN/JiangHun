import JiaoHeiZhuan

while 1:
    input_cur = input("请输入焦黑砖炉的面积和高度并以空格为分隔：\n")
    while len(input_cur.split()) != 2: # 必须输入面积和高度两个参数
        print("请输入正确的参数")
        input_cur = input("请输入焦黑砖炉的面积和高度并以空格为分隔：\n")
    area, height = [int(x) for x in input_cur.split()]
    print("请依次输入所需的排液口，浇筑台与铸造盆的个数")
    input_cur = input("排液口：\n")
    while not input_cur.isdigit():
        print("请输入整数")
        input_cur = input("排液口：\n")
    a = int(input_cur)
    input_cur = input("浇筑台：\n")
    while not input_cur.isdigit():
        print("请输入整数")
        input_cur = input("浇筑台：\n")
    b = int(input_cur)
    input_cur = input("铸造盆：\n")
    while not input_cur.isdigit():
        print("请输入整数")
        input_cur = input("铸造盆：\n")
    c = int(input_cur)
    cur_JiaoHeiLu = JiaoHeiZhuan.JiaoHeiLu(b, c, a)

    cur_Block = cur_JiaoHeiLu.BuildNeed_Num(area, height)
    cur_CaiLiao = JiaoHeiZhuan.CaiLiao_Num(cur_Block['a'], cur_Block['b'])
    Output_str = (f"需要:\n"
        f"{cur_CaiLiao['shazi']}个沙子，\n"
        f"{cur_CaiLiao['shali']}个砂砾，\n"
        f"{cur_CaiLiao['niantu']}个黏土块即{cur_CaiLiao['niantu'] * 4}个黏土")
    print(Output_str)
    
    f = open(f"./{area}x{area}, {height}.txt2", 'w')
    f.write(Output_str)
    f.close()

    input_cur = input("是否结束（输入\"是\"或\"否\"）\n")
    while input_cur != '是' and input_cur != '否':
        print("请输入\"是\"或\"否\"")
        input_cur = input("是否结束（输入\"是\"或\"否\"）\n")
    if input_cur == '是':
        break