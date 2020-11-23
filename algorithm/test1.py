'''

双指针解决去重问题：

给定一个排序数组，你需要在 原地 删除重复出现的元素，使得每个元素只出现一次，返回移除后数组的新长度。

不要使用额外的数组空间，你必须在 原地 修改输入数组 并在使用 O(1) 额外空间的条件下完成。

视频：https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array/solution/shuang-zhi-zhen-shan-chu-zhong-fu-xiang-by-t9qx90n/

'''
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        i = 0
        for j in range(1, len(nums)):
            if nums[i] != nums[j]:
                i += 1
                nums[i] = nums[j]
        return i + 1


if __name__ == '__main__':
    nums = [3, 4, 4, 5, 5, 6]
    hou = Solution()
    print(hou.removeDuplicates(nums))

    # 输出 去重后的 数组
    # print([i for i in nums[:Solution().removeDuplicates(nums)]])

'''


利用两个指针i, j,初始化值为0和1，当两个指针对应的值相等时，指针j+1，继续执行循环；而当两个指针对应的值不相等时，将指针i+1，并将指针j对用的值赋值给指针i，然后指针j+1，继续向下执行循环，直到循环结束。



'''
