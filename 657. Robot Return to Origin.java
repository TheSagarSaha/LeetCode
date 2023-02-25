class Solution {
    public boolean judgeCircle(String moves) {
        int[] arr = {0, 0, 0, 0};
        for (int i = 0; i < moves.length(); i++) {
            if (String.valueOf(moves.charAt(i)).equals("U")) {
                arr[0] += 1;
            } else if (String.valueOf(moves.charAt(i)).equals("D")) {
                arr[1] += 1;
            } else if (String.valueOf(moves.charAt(i)).equals("R")) {
                arr[2] += 1;
            } else if (String.valueOf(moves.charAt(i)).equals("L")) {
                arr[3] += 1;
            }
        }
        return (arr[0] == arr[1] && arr[2] == arr[3]);
    }
}
