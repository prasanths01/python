# # 1
# n = 3
# for i in range(n):
#     for j in range(1,n+1):
#         print(j,end = '')
#     print()
#
# '''
# 123
# 123
# 123
# '''
# # 2
# n = 3
# for i in range(n):
#     for j in range(n, 0, -1):
#         print(j, end='')
#     print()
#
# '''
# 321
# 321
# 321
# '''
#
# # 3
#
# n = 5
# for i in range(5,0,-1):
#     for j in range(1,i+1):
#         print(j,end  = ' ')
#     print()
#
# '''
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5
# '''
#
# # 4
#
# n = 5
# for i in range(5,0,-1):
#     for j in range(1,i+1):
#         print(j,end  = ' ')
#     print()
#
# '''
# 1 2 3 4 5
# 1 2 3 4
# 1 2 3
# 1 2
# 1
# '''

# 5

# n = 5
# a = 4
# for i in range(1,n+1):
#     print('- '*a,end='')
#     for j in range(i,0,-1):
#         print(j,end=' ')
#     print()
#     a-=1
#
# '''
# - - - - 1
# - - - 2 1
# - - 3 2 1
# - 4 3 2 1
# 5 4 3 2 1
# '''
# # 6
# n = 5
# a = 0
# for i in range(n,0,-1):
#     print('- '*a,end='')
#     for j in range(i,0,-1):
#         print(j,end=' ')
#     print()
#     a +=1
#
# '''
# 5 4 3 2 1
# - 4 3 2 1
# - - 3 2 1
# - - - 2 1
# - - - - 1
# '''
# # 7
#
# n = 5
# for i in range(n,0,-1):
#     for j in range(i,n+1):
#         print(j,end=' ')
#     print()
#
# '''
# 5
# 4 5
# 3 4 5
# 2 3 4 5
# 1 2 3 4 5
#
# '''
# # 8
#
# n = 5
# for i in range(1,n+1):
#     for j in range(i,n+1):
#         print(j,end=' ')
#     print()
#
# '''
# 1 2 3 4 5
# 2 3 4 5
# 3 4 5
# 4 5
# 5
#
# '''
# 9

n = 5
for i in range(n,0,-1):
    for j in range(i,0,-1):
        print(j,end=' ')
    print()
'''
5 4 3 2 1 
4 3 2 1 
3 2 1 
2 1 
1

'''
# 10
n =5
for i in range(1,n+1):
    for j in range(i,0,-1):
        print(j,end=' ')
    print()

'''
1 
2 1 
3 2 1 
4 3 2 1 
5 4 3 2 1 

'''
# 11

n = 5
for i in range(n,0,-1):
    for j in range(n,i-1,-1):
        print(j,end=' ')
    print()

'''

5 
5 4 
5 4 3 
5 4 3 2 
5 4 3 2 1 

'''
# 12

n = 5
for i in range(n):
    for j in range(n,i,-1):
        print(j,end=' ')
    print()
'''
5 4 3 2 1 
5 4 3 2 
5 4 3 
5 4 
5 

'''
# 15
'''
n = 5
a = 0
for i in range(0,n+1):
    print(' '*a,end='')
    p = 1
    for j in range(i,n+1):
        print(p+i,end='')
    print()
    a +=1
    p +=1

111111
 22222
  3333
   444
    55
     6
'''
n = 5
a = 0
for i in range(n):
    print(' '*a,end='')
    p = 1
    for j in range(i,n):
        print(i+1,end='')
    print()
    a +=1
    p +=1

'''
11111
 2222
  333
   44
    5
'''