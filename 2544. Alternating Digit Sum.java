class Solution {
    public int alternateDigitSum(int n) {
        int res = 0;
        String num = String.valueOf(n);
        for (int i=0; i < num.length(); i++) {
            res = res + (int)(Math.pow(-1, i)*Integer.parseInt(String.valueOf(num.charAt(i))));
        }
        return res;
    }
}
