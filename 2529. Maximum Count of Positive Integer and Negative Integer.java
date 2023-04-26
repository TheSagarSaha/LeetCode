class Solution {
    public int maximumCount(int[] nums) {
        int count = nums.length;
        int count2 = 0;
        for (int i=0; i < nums.length; i++) {
            if (nums[i] == 0) {
                count--;
            }
            else if (nums[i] > 0) {
                break;
            } else {
                count--;
                count2++;
            }
        }
        return Math.max(count, count2);
    }
}
