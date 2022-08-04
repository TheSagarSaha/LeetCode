class Solution {
    public int[] sortedSquares(int[] nums) {
        
        if (nums.length == 1) {
            nums[0] = nums[0]*nums[0];
            return nums;
        }
        
        int l = 0, r = nums.length-1, count = nums.length-1;
        int[] res = new int[nums.length];
    
        while (l != r && (l < r)) {
            int left = nums[l]*nums[l], right = nums[r]*nums[r];
            if (left < right) {
                res[count] = right;
                r--;
                count--;
            } else if (left > right) {
                res[count] = left;
                l++;
                count--;
            } else if (left == right) {
                res[count] = left;
                count--;
                l++;
                res[count] = right;
                count--;
                r--;
            }
        }
        if (l == r) {
            res[count] = nums[l]*nums[r];
        }
        return res;
        
        
    }
}
