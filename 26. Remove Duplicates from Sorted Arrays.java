class Solution {
    public int removeDuplicates(int[] nums) {
        for(int i = 0; i < nums.length - 1; i++) {
            if (nums[i] == nums[i+1]) {
                nums[i] = -1001;
            }
        }

        for (int i=0; i < nums.length; i++) {
            for (int j=i+1; j < nums.length; j++) {
                if (nums[i] == -1001 && nums[i] != nums[j]) {
                    nums[i] = nums[j];
                    nums[j] = -1001;
                    break;
                }
            }
        }

        for (int i=0; i < nums.length; i++) {
            if (nums[i] == -1001) {
                return i;
            }
        }
        return nums.length;
    }
}
