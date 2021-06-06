class commonUtil:

    def is_contain(self,st_one,st_two):
        """
        判断一个字符串是否在另一个字符串中
        :return:
        st_one 查找的字符串
        st_two： 被查找到字符串
        """

        if st_one in st_two:
            flag =True
        else:
            flag = False
        return flag