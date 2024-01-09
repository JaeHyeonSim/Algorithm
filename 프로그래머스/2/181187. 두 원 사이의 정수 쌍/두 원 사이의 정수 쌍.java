import java.util.*;
import java.lang.Math;

class Solution {
    public long solution(int r1, int r2) {
        long answer = 0;
        
        for (long x = 1; x <= r2; x++) {
            double y2 = Math.pow(((long)r2 * r2 - x * x), 0.5);
            double y1 = Math.pow(((long)r1 * r1 - x * x), 0.5);
            if (y1 < 0) {
                y1 = 0;
            }
            if (y1 != 0 && y1 % 1 != 0) {
                y1++;
            }
            answer += (int)y2 - (int)y1 + 1;
        }
        answer *= 4;
        
        return answer;
    }
}