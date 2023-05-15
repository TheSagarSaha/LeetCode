class Solution {
    public int countMatches(List<List<String>> items, String ruleKey, String ruleValue) {
        int checker;
        int res = 0;
        if (ruleKey.equals("type")) { checker = 0; }
        else if (ruleKey.equals("color")) { checker = 1; }
        else { checker = 2; }

        for (int i=0; i < items.size(); i++) {
            if (items.get(i).get(checker).equals(ruleValue)) { res++; }
        }

        return res;
    }
}
