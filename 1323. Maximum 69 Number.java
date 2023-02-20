class Solution {
    public int maximum69Number (int num) {
        String x = String.valueOf(num);
        String res = "";
        boolean cont = true;
        for (int i = 0; i < x.length(); i++) {
            if (String.valueOf(x.charAt(i)).equals("6") && cont) {
                res += "9";
                cont = false;
            } else {
                res += String.valueOf(x.charAt(i));
            }
        }
        
        return Integer.valueOf(res);
    }
}
