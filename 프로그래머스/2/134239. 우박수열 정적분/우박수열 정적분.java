import java.util.ArrayList;

class Solution {
    public double[] solution(int k, int[][] ranges) {
        double[] answer = {};
        
        ArrayList<Double> areas = new ArrayList<>();
        int point = k;
        while (point > 1) {
            int last = point;
            if (point % 2 == 0) {
                point /= 2;
            } else {
                point = point * 3 + 1;
            }
            areas.add(0.5 * (point + last));
        }
        
        int n = areas.size();
        answer = new double[ranges.length];
        for (int i = 0; i < ranges.length; i++) {
            int a = ranges[i][0];
            int b = ranges[i][1];
            
            if (a - b > n) {
                answer[i] = -1;
                continue;
            }
            
            double area = 0;
            for (int j = a; j <= (n - 1) + b; j++) {
                area += areas.get(j);
            }
            answer[i] = area;
        }
        
        return answer;
    }
}