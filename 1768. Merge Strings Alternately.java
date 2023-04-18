class Solution {
    public String mergeAlternately(String word1, String word2) {
        String res = "";
        int word1Count = 0;
        int word2Count = 0;
        while(word1Count < word1.length() && word2Count < word2.length()) {
            res += word1.charAt(word1Count);
            res += word2.charAt(word2Count);
            word1Count++; word2Count++;
        }

        if (word1Count == word1.length()) {
            while(word2Count < word2.length()) {
                res += word2.charAt(word2Count);
                word2Count++;
            }
        } else {
            while(word1Count < word1.length()) {
                res += word1.charAt(word1Count);
                word1Count++;
            }
        }
        return res;
    }
}
