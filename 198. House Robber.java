class Solution {
    public int rob(int[] nums) {
     int prev=0;
     int last=0;
     for (int curr : nums)
         last = Math.max(prev+curr, prev=last);
     return last;
}
}
