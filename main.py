# 开源作者：github: @MichaelDebugger
# 开源作者主页：https://github.com/MichaelDebugger
# 再分享请注明
# 为确保程序能够正常运行，请使用python3.9及以上版本

class Magic():
    def cards(self, cards: list[str], name_lenth: int, area: int, gender: int) -> tuple:
        import random

        # 打乱卡牌
        random.shuffle(cards)

        # 对折撕开并重新洗牌
        tornCards = cards*2
        firstTornCards = tornCards[:]

        # 根据名字长度修改牌组
        tornCards = tornCards[name_lenth:] + tornCards
        afterNameCards = tornCards[:]

        # 拿起上面的三张牌放到中间
        topThree = tornCards[3:]
        middleCards = random.randint(3, len(tornCards))
        tornCards = tornCards[3:middleCards] + topThree
        afterThreeCards = tornCards[:]

        # 把上面的牌存下来
        underAssCard = tornCards.pop(0)

        # 拿一张牌放到中间
        userCard = tornCards.pop(0)
        middleCards = random.randint(3, len(tornCards)-1)
        tornCards = tornCards[:middleCards] + [userCard] + tornCards[middleCards:]

        # 根据性别修改牌组
        for _ in range(gender):
            tornCards.remove(random.choice(tornCards))

        # 根据地区修改牌组
        for _ in range(area):
            tornCards.remove(random.choice(tornCards))
        
        afterGenderCards = tornCards[:]

        # 把最上面的牌放到下面，重复7次
        for _ in range(7):
            topCard = tornCards.pop(0)
            tornCards.append(topCard)

        while len(tornCards) > 1:
            tornCards.append(tornCards.pop(0))
            tornCards.pop(0)

        result = underAssCard == topCard[0]

        return (firstTornCards, afterNameCards, afterThreeCards, afterGenderCards, tornCards, underAssCard, result)


if __name__ == "__main__":
    obj = Magic()

    # 获取数据
    userCards = [input("请输入四张扑克牌（回车键至下一张）："), input(), input(), input()]
    user_name_length = len(input("请输入名字："))
    userGender = input("请输入性别：")
    userGender = 1 if userGender=="male" else 2
    area = input("请输入地区：")
    area = 1 if area=="south" else 2 if area=="north" else 3

    firstTornCards, afterNameCards, afterThreeCards, afterGenderCards, tornCards, hiddenCards, result = \
        obj.cards(userCards, user_name_length, area, userGender)
    print(f"刚开始洗好并且撕成两半的牌：{firstTornCards}")
    print(f"根据姓名长度修改牌组，把姓名长度张牌放到后面：{afterGenderCards}")
    print(f"把上面的三张牌放到中间任意位置：{afterThreeCards}")
    print(f"南方人拿掉1张，北方人拿起2张，其他拿起3张，插入到中间。\n\
          男生拿起1张，女生拿起2张，撒到空中（删除牌）\n\
          {afterGenderCards}")
    print(f"最后的牌：{tornCards}")
    print(f"藏的牌：{hiddenCards}")
    print("结果正确！" if result else "结果错误，请重新运行脚本。")