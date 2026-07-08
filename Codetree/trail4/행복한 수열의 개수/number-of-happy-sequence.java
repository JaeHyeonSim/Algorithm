import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    
    static int N, M;
    static int[][] matrix;
    
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        
        matrix = new int[N][N];
        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < N; j++) {
                matrix[i][j] = Integer.parseInt(st.nextToken());
            }
        }

//        for (int i = 0; i < N; i++) {
//            for (int j = 0; j < N; j++) {
//                System.out.print(matrix[i][j] + " ");
//            }
//            System.out.println();
//        }

        int answer = 0;
        
        for (int i = 0; i < N; i++) {
            int seq = 1;
            for (int j = 1; j < N; j++) {
                if (matrix[i][j] == matrix[i][j - 1]) {
                    seq++;
                } else {
                    if (seq >= M) { break; }
                    seq = 1;
                }
            }
            if (seq >= M) { answer++; }
        }

        for (int i = 0; i < N; i++) {
            int seq = 1;
            for (int j = 1; j < N; j++) {
                if (matrix[j][i] == matrix[j - 1][i]) {
                    seq++;
                } else {
                    if (seq >= M) { break; }
                    seq = 1;
                }
            }
            if (seq >= M) { answer++; }
        }
        
        System.out.println(answer);
        
        br.close();
    }
    
}
