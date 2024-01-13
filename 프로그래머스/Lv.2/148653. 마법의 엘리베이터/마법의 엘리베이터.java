class Solution {
    public int solution(int storey) {
        int answer = 0;
        
        while (storey > 0) {
            int unit = storey % 10;
            
            storey /= 10;
            
            if (unit < 5) {
                answer += unit;
            } else if (unit > 5) {
                answer += 10 - unit;
                storey += 1;
            } else {
                answer += unit;
                if (storey % 10 >= 5) {
                    storey += 1;
                }
            }
            System.out.println(storey + ", "+ unit + " -> " + answer);
        }
        
        return answer;
    }
}