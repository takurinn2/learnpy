# Employee Manager System 员工管理系统
# 命令行版本的员工管理系统
# 功能：
# 1.查询    显示当前系统中所有员工
# 2.添加    将员工添加到当前系统中
# 3.删除    删除员工
# 4.退出    退出系统

print('='*20,'欢迎使用EMS','='*20)
emps = ['001号\t18\t男\t一区','002号\t23\t男\t一区']
while True :
    print('请选择要做的操作:')
    print('\t1.查询员工')
    print('\t2.添加员工')
    print('\t3.删除员工')
    print('\t4.退出系统')
    user_choose = input('请选择[1-4]:')
    print('='*60)
    if user_choose == '1':
        print('\t序号\t姓名\t年龄\t性别\t住址')
        n = 1
        for emp in emps :
            print(f'\t{n}\t{emp}')
            n += 1
    elif user_choose == '2':
       
        emp_name = input('输入员工姓名')
        emp_age = input('输入员工年龄')
        emp_gender = input('输入员工性别')
        emp_address = input('输入员工住址')

        emp = f'{emp_name}\t{emp_age}\t{emp_gender}\t{emp_address}'
        print('='*60)
        print('姓名\t年龄\t性别\t住址')
        print(emp)
        print('='*60)
        choose = input('是否添加[y/n]')
        if choose == 'y' or choose == 'yes' :#确认
            emps.append(emp)
            print('插入成功!')
        else :#取消操作
            print('取消插入!')
   
    elif user_choose == '3':
        del_num = int(input('输入要删除员工的序号'))
        if del_num > 0 and del_num <= len(emps) :
            del_i = del_num - 1 #索引数值
            print('='*60)
            print('\t序号姓名\t年龄\t性别\t住址')
            print(f'\t{del_num}\t{emps[del_i]}')
            print('='*60)
            choose = input('是否删除[y/n]')
            if choose == 'y' or choose == 'yes' :
                emps.pop(del_i)
                print('员工已被删除!')
            else :
                print('操作取消!')
        else :
            print('输入有误')
   
    elif user_choose == '4':
        print('='*60)
        input('再见!\t点击回车键退出!')
        break
    else :
        print('输入有误，重新选择')
    print('='*60)
