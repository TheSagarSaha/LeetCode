class Solution {
    public int findMaxConsecutiveOnes(int[] nums) {
        int count = 0;
        int curr = 0;

        for (int i = 0; i < nums.length; i++) {
            if (nums[i] == 1) {
                curr++;
                if (curr > count) {
                    count = curr;
                }
            } else {
                if (curr > count) {
                    count = curr;
                }
                curr = 0;
            }
        }
        return count;
    }
}
