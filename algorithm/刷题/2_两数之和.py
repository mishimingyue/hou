'''
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。

你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/two-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


def twoSum(nums, target):
    lens = len(nums)
    j = -1
    for i in range(lens):
        if (target - nums[i]) in nums:
            if (nums.count(target - nums[i]) == 1) & (
                    target - nums[i] == nums[i]):  # 如果num2=num1,且nums中只出现了一次，说明找到是num1本身。
                continue
            else:
                j = nums.index(target - nums[i], i + 1)  # index(x,i+1)是从num1后的序列后找num2
                break
    if j > 0:
        return [i, j]
    else:
        return []


if __name__ == '__main__':
    print(twoSum([5, 3, 8, 2, 2], 8))
