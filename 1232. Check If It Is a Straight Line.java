class Solution {
    public boolean checkStraightLine(int[][] coordinates) {
        Set<Double> slopes = new HashSet<>();
        boolean undefined = false;
        for(int i=0; i < coordinates.length-1; i++) {
            if (coordinates[i][0] == coordinates[i+1][0]) {
                undefined = true;
            } else if (coordinates[i][1] == coordinates[i+1][1]) {
                double currentSlope = (double)(coordinates[i+1][1] - coordinates[i][1]) / (double)(coordinates[i+1][0] - coordinates[i][0]);
                if (!slopes.contains(currentSlope)){
                    slopes.add(Math.abs(currentSlope));
                }
            } else {
                double currentSlope = (double)(coordinates[i+1][1] - coordinates[i][1]) / (double)(coordinates[i+1][0] - coordinates[i][0]);
                if (!slopes.contains(currentSlope)){
                    slopes.add(currentSlope);
                }
                System.out.println(currentSlope);
            }
        }

        if (undefined == false && slopes.size() == 1) {
            return true;
        } else if (undefined == true && slopes.size() == 0) {
            return true;
        } return false;
    }
}
