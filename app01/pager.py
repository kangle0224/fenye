#!/usr/bin/env python
# coding: utf-8

class Pagination(object):
    def __init__(self, totalCount, currentPage, perPageNum=10, maxPageNum=7):
        # 数据总个数
        self.total_count = totalCount
        # 当前页
        self.current_page = 1
        try:
            v = int(currentPage)
            if v <= 0:
                v=1
                self.current_page = v
            else:
                self.current_page = v
        except Exception as e:
            self.current_page = 1
        # 每页显示的行数
        self.per_page_num = perPageNum
        # 最多显示页码
        self.max_page_num = maxPageNum

    def start(self):
        return (self.current_page-1)*self.per_page_num

    def end(self):
        return self.current_page*self.per_page_num

    @property
    def num_pages(self):
        # 总页数
        # 加上property之后，调用方法就不用加()了
        a, b = divmod(self.total_count, self.per_page_num)
        if b == 0:
            return a
        else:
            return a+1

    def pager_num_range(self):
        if self.num_pages < self.max_page_num:
            return range(1, self.num_pages+1)

        part = int(self.max_page_num/2)
        if self.current_page <= part:
            return range(1, self.max_page_num+1)
        if (self.current_page+part) > self.num_pages:
            return range(self.num_pages-self.max_page_num+1, self.num_pages+1)
        return range(self.current_page-part, self.current_page+part+1)

    def page_str(self):
        page_list = []
        first = "<li><a href='/index/?p=1'>首页</a></li>"
        page_list.append(first)
        if self.current_page == 1:
            prev = "<li><a href='#'>上一页</a></li>"
        else:
            prev = "<li><a href='/index2/?p=%s'>上一页</a></li>" % (self.current_page-1,)
        page_list.append(prev)

        for i in self.pager_num_range():
            if i == self.current_page:
                temp = "<li class='active'><a href='/index2/?p=%s'>%s</a></li>" % (i, i)
            else:
                temp = "<li><a href='/index2/?p=%s'>%s</a></li>" % (i, i)
            page_list.append(temp)

        if self.current_page == self.num_pages:
            nex = "<li><a href='#'>下一页</a><li>"
        else:
            nex = "<li><a href='/index2/?p=%s'>下一页</a></li>" % (self.current_page+1,)
        page_list.append(nex)
        end = "<li><a href='/index/?p=%s'>尾页</a></li>" % self.num_pages
        page_list.append(end)
        return ''.join(page_list)



