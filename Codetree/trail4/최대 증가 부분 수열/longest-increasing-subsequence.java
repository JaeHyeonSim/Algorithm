
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    
    static int N, s1[], s2[], size;
    
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        
        N = Integer.parseInt(st.nextToken());
        
        s1 = new int[N];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            s1[i] = Integer.parseInt(st.nextToken());
        }

        s2 = new int[N];
        s2[0] = s1[0];
        size = 1;
        for (int i = 1; i < N; i++) {
            if (s1[i] > s2[size - 1]) {
                s2[size++] = s1[i];
                continue;
            }
            int x = search(s1[i]);
            if (x != -1 && s1[i] != s2[x]) {
                s2[x] = s1[i];
            }
        }

//        System.out.println(Arrays.toString(s2));
        System.out.println(size);
        
        br.close();
    }
    
    static int search(int num) {
        int s = 0;
        int e = size;
        int ans = -1;
        while (s < e) {
            int mid = (s + e) / 2;
            if (num <= s2[mid]) {
                ans = mid;
                e = mid;
            } else {
                s = mid + 1;
            }
        }
        return ans;
    }
    
}
