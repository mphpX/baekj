import java.io.*;
import java.util.*;

public class Solution {
    static int N;
    static int[] x, y;
    static long ans;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        int T = Integer.parseInt(br.readLine());
        for (int tc = 1; tc <= T; tc++) {

            N = Integer.parseInt(br.readLine());

            x = new int[N];
            y = new int[N];

            for (int i = 0; i < N; i++) {
                st = new StringTokenizer(br.readLine());
                x[i] = Integer.parseInt(st.nextToken());
                y[i] = Integer.parseInt(st.nextToken());
            }

            ans = Long.MAX_VALUE;

            bt(0, 0, 0, 0, 0, 0);

            System.out.println("#" + tc + " " + ans);
        }
    }

    static void bt(int idx, int cntA,
                   long sumAX, long sumAY,
                   long sumBX, long sumBY) {

        // 가지치기
        if (cntA > N / 2) return;
        if (cntA + (N - idx) < N / 2) return;

        if (idx == N) {
            if (cntA == N / 2) {
                long vx = sumAX - sumBX;
                long vy = sumAY - sumBY;

                long dist = vx * vx + vy * vy;
                ans = Math.min(ans, dist);
            }
            return;
        }

        // A 그룹
        bt(idx + 1, cntA + 1,
           sumAX + x[idx], sumAY + y[idx],
           sumBX, sumBY);

        // B 그룹
        bt(idx + 1, cntA,
           sumAX, sumAY,
           sumBX + x[idx], sumBY + y[idx]);
    }
}