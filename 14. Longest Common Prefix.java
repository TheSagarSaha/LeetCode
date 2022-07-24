class Solution {
    public String longestCommonPrefix(String[] strs) {
        if (strs.length == 1) {
            return strs[0];
        } else if (strs.length == 0) {
            return "";
        }
        String text = strs[0];
        for (int i = 1; i < strs.length; i++) {
            while(strs[i].indexOf(text) != 0) {
                text = text.substring(0, text.length()-1);
            }
        }
        return text;
        
    }
}
