#Generators

# def squareNum(nums):
#     result = []
#     for i in nums:
#         result.append(i*i)
#     return result
# myNums = squareNum([1,2,3,4,5])
# print(myNums)

#generator version
def squareNum(nums):
    for i in nums:
        yield(i*i)
myNums = squareNum([1,2,3,4,5])

for num in myNums:
    print(num)
    
#^ Det samme som ovenstående men som list comprehension format
myNums2 = [x*x for x in [1,2,3,4,5]]
#^Man kan convert til list, men det vil forværre performance
#myNums = (x*x for x in [1,2,3,4,5])
#print(list(myNums)

print(myNums2)



