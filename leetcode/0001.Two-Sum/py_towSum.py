# python 实现


def towSum(nums:list,target:int)->tuple:
    m = dict()
    for index,num in enumerate(nums):
        
        if (p:=m.get(target - num)) is not None:
            return (p,index)
        else:
            m[num] = index
    return ()
        



if __name__ == '__main__':
    nums = [2, 7, 9, 6]
    target = 9
    res = towSum(nums,target)
    print(res)
