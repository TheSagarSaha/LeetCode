class Solution {
    public boolean isPerfectSquare(int num) {
        int x = (int)(Math.pow(num, 0.5));
        return (x*x == num);
    }
}
