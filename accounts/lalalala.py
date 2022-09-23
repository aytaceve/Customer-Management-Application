# list1 = [3,2,4]
# maxNum = max(list1)
#
#
# def ulduzla(list1):
#     result = []
#     for i in list1:
#         inList = []
#         while i < maxNum:
#             inList.append(' ')
#             i += 1
#         for j in range(i):
#             inList.append('*')
#         result.append(inList)
#
    # for i in range(maxNum):
    #     a = []
    #     for j in range(len(result)):
    #         a.append(result[j][i])
    #     print(*a)
    #     print()

    # print(*list1)

digits = [9, 9, 9]

def plusOne(digits):
    num = ''
    for i in digits:
        num += (str(i))
    intNum = int(num)
    plusOne = intNum + 1
    result = []
    while plusOne != 0:
        a = plusOne % 10
        result.insert(0, a)
        plusOne //= 10
    print(result)

plusOne(digits)



############################################

# def ulduzla(list1):
#     result = []
#     for i in list1:
#         inList = []
#         if i < maxNum:
#             for d in range(maxNum - i):
#                 inList.append(' ')
#         for j in range(i):
#             inList.append('*')
#         result.append(inList)
#
#     for i in range(maxNum):
#         a = []
#         for j in range(len(result)):
#             a.append(result[j][i])
#         print(*a)
#         print()
#
#     print(*list1)



# ulduzla(list1)

#############################################
# class Solution:
#     def plusOne(self, digits):
#         if digits[-1] < 9:
#             digits[-1] += 1
#             return digits
#         elif len(digits) == 1 and digits[0] == 9:
#             return [1, 0]
#         else:
#             digits[-1] = 0
#             digits[0:-1] = self.plusOne(digits[0:-1])
#             return digits
#
# a = Solution()
# print(a.plusOne([1, 9, 9, 9]))