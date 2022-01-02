# 显示欢迎信息
print("-"*20,'欢迎来到',"-"*20)
# 身份信息
print('选择你的身份:')
print('\t1.第一位')
print('\t2.第二位')
# 身份选择
player_choose = input('请选择[1 - 2]:')

if player_choose == '1':
    print('一号位')
elif player_choose == '2':
    print('二号位')
else :
    print('输入有误')
# 玩家信息
player_life = 2
player_attack = 2

# boss_life
boss_life = 10
boss_attack = 10

while True:
    print('-'*40)
    # 显示玩家信息
    print(f'life = {player_life} , attack = {player_attack}')
    print('-'*40)
    print('请选择操作:')
    print('\t1.练习')
    print('\t2.打BOSS')
    print('\t3.溜')
    game_choose = input('选择[1-3]:')
    if game_choose == '1':
        player_life += 2
        player_attack += 2
        print('-'*40)
    elif game_choose == '2':
        boss_life -= player_attack
        print('你攻击了boss')
        print('-'*40)
        if boss_life <= 0:
            print(f'boss受到了{player_attack}点伤害,gameover')
            print('-'*40)
            break
        player_life -= boss_attack
        print('boss攻击了你')
        if player_life <= 0:
            print(f'你受到了{boss_attack}点伤害,你死了')
            print('-'*40)
            break
    elif game_choose == '3':
        print('你润了，怂逼')
        print('-'*40)
        break
    else:
        print('错误')