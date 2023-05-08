class Solution {
    public int diagonalSum(int[][] mat) {
        int res = 0;
        int len = mat.length;
        for(int i=0; i < len; i++) {
            res += mat[i][i];
            res += mat[i][len-1-i];
        }
        if (len % 2 == 0) {
            return res;
        }
        return res - mat[len/2][len/2];
    }
}
