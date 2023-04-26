class Solution {
    public int search(int[] nums, int target) {
        int leftPointer = 0;
        int rightPointer = nums.length;
        while (leftPointer < rightPointer) {
            int mid = (leftPointer + rightPointer) / 2;
            if (nums[mid] == target) {
                return mid;
            } else if (nums[mid] > target) {
                rightPointer = mid;
            } else {
                leftPointer = mid+1;
            }
        }
        return -1;
    }
}
