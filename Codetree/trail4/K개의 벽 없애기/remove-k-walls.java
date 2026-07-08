
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class Main {
    
    static int[] dx = { -1, 1, 0, 0 };
    static int[] dy = { 0, 0, -1, 1 };
    
    static int[][] area;
    static int r1, c1, r2, c2;
    static int N, K, minT;
    
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        
        N = Integer.parseInt(st.nextToken());
        K = Integer.parseInt(st.nextToken());
        
        area = new int[N][N];
        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < N; j++) {
                area[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        st = new StringTokenizer(br.readLine());
        r1 = Integer.parseInt(st.nextToken()) - 1;
        c1 = Integer.parseInt(st.nextToken()) - 1;
        st = new StringTokenizer(br.readLine());
        r2 = Integer.parseInt(st.nextToken()) - 1;
        c2 = Integer.parseInt(st.nextToken()) - 1;
        
        System.out.println(bfs());
        
        br.close();
    }
    
    static int bfs() {
        boolean[][] visited = new boolean[N][N];
        ArrayDeque<int[]> dq = new ArrayDeque<int[]>();
        dq.add(new int[] { r1, c1, 0, 0 });
        visited[r1][c1] = true;
        
        while (!dq.isEmpty()) {
            int[] tmp = dq.poll();
            
            for (int d = 0; d < 4; d++) {
                int nx = tmp[0] + dx[d];
                int ny = tmp[1] + dy[d];
                
                if (!inRange(nx, ny) || visited[nx][ny]) { continue; }
                
                if (nx == r2 && ny == c2) {
                    return tmp[2] + 1;
                }
                
                if (area[nx][ny] == 1 && tmp[3] >= K) {
                    continue;
                }
                visited[nx][ny] = true;
                dq.add(new int[] { nx, ny, tmp[2] + 1, tmp[3] + (area[nx][ny] == 1 ? 1 : 0) });
            }
        }
        
        return -1;
    }
    
    static boolean inRange(int nx, int ny) {
        return nx >= 0 && nx < N && ny >= 0 && ny < N;
    }
    
}
