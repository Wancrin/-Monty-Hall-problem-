'''
参赛者会看见三扇关闭了的门，
其中一扇的后面有一辆汽车，选中后面有车的那扇门可赢得该汽车，另外两扇门后面则各藏有一只山羊。
当参赛者选定了一扇门，但未去开启它的时候，节目主持人开启剩下两扇门的其中一扇，露出其中一只山羊。
主持人其后会问参赛者要不要换另一扇仍然关上的门。问题是：换另一扇门是否会增加参赛者赢得汽车的几率。
'''
import random as rd

listforjudgegive = [] #demo:[1,2,1,2,1,……] 裁判给出的每次非大奖的门的编号
listforcases = [] #demo:[[1,2,0],[2,1,0],[0,2,1],……]  三扇门中哪个是大奖 哪个是裁判给出的门，大奖：1，裁判给出：2
result = [] #demo:[0,1,1,0,1,……] 每局成功还是失败

def judgegive(cases):
    num = rd.randint(1,2)  #裁判在1到6中随机生成一个数
    if num == 1:
        for i in cases:
            if i == 0:
                cases[cases.index(i)] = 2
                break
    elif num == 2:
        j = 0
        for i in range(len(cases)):
            if cases[i] == 0:
                cases[i] = j
                j+=2
    print("【debug】judge give num:", num)
    print("【debug】judge change cases:", cases)
    listforjudgegive.append(num)
    listforcases.append(cases)
    return cases

def makecases():
    num = rd.randint(1,3)
    give = []
    if num == 1:
        give = [1, 0, 0]
        pass
    elif num == 2:
        give = [0, 1, 0]
        pass
    elif num == 3:
        give = [0, 0, 1]
        pass
    print("--------------------------------------------\n【debug】makecases()生成的是：",num,give)

    return give


def story(iftest,testmod):
    #[0,1],[0,1]
    final = 0
    cases = makecases()
    cases = judgegive(cases)
    index2 = cases.index(2)
    playernum = 0
    if iftest == 1:
        playernum = rd.randint(0,2)
    elif iftest == 0:
        print('你要选择几号门？\n请输入阿拉伯数字，你的选择有：1，2，3\n')
        playernum = int(input('在此输入：')) - 1
    if playernum + 1 == 1:
        print('\n你选择的是', playernum + 1, '号门')
        print('那么现在的情况是：① 2 3\n')
        pass
    elif playernum + 1 == 2:
        print('\n你选择的是', playernum + 1, '号门')
        print('那么现在的情况是：1 ② 3\n')

        pass
    elif playernum + 1 == 3:
        print('\n你选择的是', playernum + 1, '号门')
        print('那么现在的情况是：1 2 ③\n')
    errorindex = 0
    if playernum == index2:
        index2 = cases.index(0)
        errorindex = index2
        print('裁判告诉你，', index2 + 1, '号门后面是空的！')
    else:
        errorindex = index2
        print('裁判告诉你，', index2 + 1, '号门后面是空的！')
    temp = [0, 1, 2]
    temp.remove(playernum)
    temp.remove(errorindex)

    if iftest == 0:
        print('那么在现在的情况下，你要选择：')
        print('A.仍然坚持选择----', playernum + 1, '号门')
        print('B.选择另一张门----', temp[0] + 1, '号门')
        choicechange = input()
        if choicechange == 'a' or choicechange == 'A':
            final = playernum
            print('【坚持】你选择了坚持选择！')
        elif choicechange == 'b' or choicechange == 'B':
            final = temp[0]
            print('【重选】你选择了另外一扇门！')
    if iftest == 1:
        if testmod == 0:
            print('当前为固执模式')
            final = playernum
        if testmod == 1:
            final = temp[0]
            print('当前为改变模式')
        pass
    if cases[final] == 1:
        result.append(1)
        print('恭喜您！！！恭喜您成功选中大奖~~~')
    else:
        result.append(0)
        print('很抱歉！您没有选中大奖~~~')

if __name__ == '__main__':
    print('1.故事模式')
    print('2.测试模式')
    choice = int(input('请输入游戏模式：'))
    if choice == 0:
        pass
    elif choice == 1:
        story(0,0)
    elif choice == 2:
        testnumber = int(input('请输入你想要测试多少次：'))
        testmod = int(input('请输入改变还是不改变，不改变输入0,改变输入1：'))
        for i in range(testnumber):
            story(1,testmod)
        print(result)
        if testmod == 0:
            print('当前测试为不改变原选择模式。')
        else:
            print('当前测试为又知道一扇门后，改变原选择模式。')
        print('本次测试共计',len(result),'场，玩家获胜',result.count(1),'局！')
        shenglv = '{:.2%}'.format(result.count(1)/len(result))
        print('胜率：',shenglv )



