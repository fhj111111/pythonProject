filename = 'student.txt'

def main():
    while True:
        menm()
        choice = int(input('请选择：'))
        if choice in  [0,1,2,3,4,5,6,7]:
            if choice == 0:
                anser  = input('您确定要退出系统吗？y/n')
                if anser == 'y' or anser == 'Y':
                    print('谢谢您的使用！')
                    break
            elif choice == 1:
                insert() #录入学生信息

            elif choice == 2:
                search() # 查找学生信息

            elif choice ==3 :
                delete() # 删除学生信息

            elif choice ==4:
                update() # 更新学生信息

            elif choice == 5:
                sotr() # 排序

            elif choice == 6:
                total() #统计学生总人数

            elif choice == 7:
                show() # 显示所有的学生信息


def menm ():
    print('=======================学生信息管理系统=================')
    print('-----------------------功能菜单------------------------')
    print('\t\t\t\t\t\t\t\t\t1.录入学生信息')
    print('\t\t\t\t\t\t\t\t\t2.查找学生信息')
    print('\t\t\t\t\t\t\t\t\t3.删除学生信息')
    print('\t\t\t\t\t\t\t\t\t4.修改学生信息')
    print('\t\t\t\t\t\t\t\t\t5.排序')
    print('\t\t\t\t\t\t\t\t\t6.统计学生总人数')
    print('\t\t\t\t\t\t\t\t\t7.显示所有学生信息')
    print('\t\t\t\t\t\t\t\t\t0.退出')
    print('------------------------------------------------------')

def insert():
    student_list=[]
    while True:
        id = input('请输入id：')
        if not id:
            break
        name = input('请输入姓名：')
        if not name:
            break
        try:
            englist = int(input('请输入英语成绩:'))
            python = int(input('请输入python成绩:'))
            Java = int(input('请输入Java成绩：'))
        except:
            print('输入无效，不是整数类型，请重新输入！')
            continue
        student = {'id':id,'name':name,'englist':englist,'python':python,'java':Java}

        student_list.append(student)
        answer = input('是否继续添加 y/n')
        if answer == 'y':
            continue
        else:
            break

    save(student_list)
    print('学生信息录入完毕！')

def save(lst):
    try:
       stu_txt = open(filename,'a',encoding='utf-8')
    except:
        stu_txt = open(filename,'w',encoding='utf-8')

    for item in lst:
        stu_txt.write(str(item)+'\n')
    stu_txt.close()

def search():
    pass
import os
# def delete():
#     while True:
#         student_id = input('请输入要删除学生的id：')
#         if id != '':
#             if os.path.exists(filename):
#                 with open(filename,'r',encoding='utf-8') as file:
#                     student_id = file.readline()
#             else:
#                 student_id=[]
#                 flag = False
#             if student_old:
#                 with open(filename,'w',encoding='utf-8') as wfile:
#                     d = []
#                     for i

def update():
    pass

def sotr():
    pass

def total():
    pass

def show():
    pass



if __name__ == '__main__':
    # t = menm()
    # print(t)
    # s = main()
    # print(s)
    main()