class Solution {
    public int lengthOfLastWord(String s) {
        boolean start = false;
        int j = 0;
        for (int i = s.length() - 1; i >= 0; i--) {
            if(!s.substring(i, i+1).equals(" ")) {
                start = true;
                if (!s.substring(i, i+1).equals(" ")) {
                    j++;
                } else {
                    break;
                }
            } else if (start) {
                break;
            }

        }
        return j;
    }
}
