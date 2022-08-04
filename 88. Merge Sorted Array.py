class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        duplicate = nums1[::]
        n1 = 0
        n2 = 0
        count = 0

        if m == 0 and n == 0:
            print("dont do anything")
        elif m == 0:
            count1 = 0
            n21 = 0
            while n21 != n:
                nums1[count1] = nums2[n21]
                n21 += 1
                count1 += 1
            n2 = n
        elif n == 0:
            print("dont do anything 2")
        else:

            while True:
                if duplicate[n1] < nums2[n2]:
                    nums1[count] = duplicate[n1]
                    count += 1
                    n1 += 1
                elif duplicate[n1] > nums2[n2]:
                    nums1[count] = nums2[n2]
                    count += 1
                    n2 += 1
                elif duplicate[n1] == nums2[n2]:
                    nums1[count] = duplicate[n1]
                    count += 1
                    nums1[count] = nums2[n2]
                    count += 1
                    n1 += 1
                    n2 += 1

                if (n1 == m and n2 == n) or n1 == m or n2 == n:
                    break

        if n1 == m and n1 != 0:
            while n2 != n:
                nums1[count] = nums2[n2]
                count += 1
                n2 += 1

        elif n2 == n and n2 != 0:
            while n1 != m:
                nums1[count] = duplicate[n1]
                count += 1
                n1 += 1
                
                
        print(nums1)
