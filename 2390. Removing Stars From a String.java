class Solution {
    public String removeStars(String s) {
        ArrayList<String> res = new ArrayList<String>();
        for (int i=0; i < s.length(); i++) {
            if (s.charAt(i) != '*') {
                res.add(s.charAt(i) + "");
            } else {
                res.remove(res.size()-1);
            }
        }
        
        return String.join("", res);

    }
}
