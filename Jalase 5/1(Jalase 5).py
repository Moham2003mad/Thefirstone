# m='shanbe seperator 1shanbeseperator 2shanbe , seperator3sahn'
# def split_str(s,char):
#     start,end=0,0
#     while end < len (s):
#         if m[end]==char or end == len(s)-1:
#             print(s[start:end])
#             start=end+1
#         end+=1
# split_str(m, "seperator")
# m = "shanbe seperator 1shanbeseperator 2shanbeseperator3shanfgfrbe"

# def split_str(s,char):
#     start,end = 0,0
#     while end<len(s):
#         if s[end]==char or end==len(s)-1 :
#             print(s[start:end])
#             start=end+1  
#         elif s[start:end]=='seperator':
#             print(s[start:end])
#             start=end+1 
#         end+=1

# split_str(m,"seperator")
# m = "seperatorshanbe seperator 1shanbeseperator 2shanbe seperator3shanfgfrbe"

# def split_str(s, char):
#     start = 0
#     end = 0
#     while end < len(s):
#         if s[end:end+len(char)] == char or end == len(s)-1:
#             print(s[start:end])
#             start = end + len(char)
#         end += 1

# split_str(m, "")
# a=['array','list']
# print(a.pop(0))
 #########################


# i=1 
# s=[] 
# many=int(input("how many people are in your class : "))
# a=many
# while i<=a: 
#     n=input()
#     s.append(n)
#     i+=1
# print(s)    
####################################
# many=int(input("how many product do you have? "))
# sum=0
# for i in range(many) :
#     i=int(input("how much its price "))
#     sum+=i
# print("the price is " ,sum)
####################################
def split_str(s, char):
    start = 0
    end = 0
    output=[]
    while end < len(s):
        if s[end:end+len(char)] == char or end == len(s)-1:
            # print(s[start:end])
            output.append(s[start:end])
            start = end + len(char)
        end += 1
    return output
s="shanbe,1shanbe,2shanbe"
days=split_str(s, " ")
print(days)
        


