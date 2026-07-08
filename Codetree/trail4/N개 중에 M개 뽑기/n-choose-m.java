
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    
    static int N, M;
    static int[] bucket;
    
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        
        bucket = new int[M];
        comb(1, 0);
        
        br.close();
    }
    
    static void comb(int start, int cnt) {
        if (cnt == M) {
            for (int i = 0; i < M; i++) {
                System.out.print(bucket[i] + " ");
            }
            System.out.println();
            return;
        }
        
        for (int i = start; i <= N; i++) {
            bucket[cnt] = i;
            comb(i + 1, cnt + 1);
        }
        
    }
    
}
