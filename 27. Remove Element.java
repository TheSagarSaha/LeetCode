class Solution {
    public int removeElement(int[] nums, int val) {
        for(int i = 0; i < nums.length; i++) {
            if (nums[i] == val || nums[i] == -1) {
                nums[i] = -1;
                for(int j = i+1; j < nums.length; j++) {
                    if (nums[j] != val && nums[j] != -1) {
                        nums[i] = nums[j];
                        nums[j] = -1;

                        break;
                    }
                }
            }
        }
        int k = 0;
        for(int i = 0; i < nums.length; i++) {
            if (nums[i] != -1) {
                k++;
            }
        }
        return k;
    }
}
