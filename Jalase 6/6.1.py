# def split_str(s, char):
#     start = 0
#     end = 0
#     output=[]
#     while end < len(s):
#         if s[end:end+len(char)] == char or end == len(s)-1:
#             # print(s[start:end])
#             output.append(s[start:end])
#             start = end + len(char)
#         end += 1
#     return output
# s="shanbe,1shanbe,2shanbe"
# days=split_str(s, " ")
# print(days)
###########################################
# test1=["shanbe","1shanbe"]
# test2=["1shanbe","3shanbe"]
# test3=["shanbe","2shanbe"]
#             #["shanbe","1shanbe","3shanbe","2shanbe"]
# empty=[]
# for i in range(len(test1)):
#     empty.append(test1[i])
# for i in range(len(test2)):
#     if i != test1[i]:
#         empty.append(test2[i])
# for i in range(len(test3)):
#     if i != test3[i] and test2[i]:
#         empty.append(test3[i])
#         print(empty)
###########################################

# _ = input()
# first_list = input().split()
# _ = input()
# second_list = input().split()
# _ = input()
# third_list = input().split()

# days_of_week = ["shanbe",
#                 "1shanbe",
#                 "2shanbe",
#                 "3shanbe",
#                 "4shanbe",
#                 "5shanbe",
#                 "jome"]

# c = 0
# for day in days_of_week:
#     if day not in first_list and day not in second_list and day not in third_list:
#         c += 1

# print(c)
###########################################

            