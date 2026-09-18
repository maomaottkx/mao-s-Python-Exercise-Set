# 作用：学习列表 list 的增删改查和常用统计函数。
num_list = [1, 2, 4, 6, 77, 9, 10]
# list 作用：用方括号创建列表，按顺序保存多个数据。
num_list.append(11)
# append() 作用：在列表末尾添加一个元素。
num_list.remove(9)
# remove() 作用：删除第一个匹配的元素。
print(num_list[2])
# 索引作用：用位置编号取元素，编号从 0 开始。
num_list[3] = 88
# 修改元素：通过索引给指定位置赋新值。
print(max(num_list))
# max()/min()/sum() 作用：求最大值、最小值和总和。
print(min(num_list))
print(sum(num_list))
print(sorted(num_list))
# sorted() 作用：返回排序后的新列表，不改变原列表。