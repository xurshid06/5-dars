# import asyncio
# import json
#
# async def read_data_1():
#     with open('data_1.json', 'r') as a'':
#         data = json.load(a)
#     return data
#
# async def write_data_2(data):
#     with open('data_2.json', 'w') as file:
#         json.dump(data, file)
#
# async def main():
#     data_1 = await read_data_1()
#
#     await write_data_2(data_1)
# asyncio.run(main())

#############     LETCODE
1

dic ={
"I":1,
"V"  :           5,
"X"  :           10,
"L"  :           50,
"C"  :           100,
"D"  :           500,
"M"  :           1000
}


def solution(s):
    sum = 0
    for i in s:
        sum += dic[i]
        print( dic[i])
    return sum
s = "LVII"
print(solution(s))