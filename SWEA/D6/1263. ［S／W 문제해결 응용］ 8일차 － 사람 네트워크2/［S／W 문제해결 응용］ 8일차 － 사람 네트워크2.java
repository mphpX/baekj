/*
문제: 사람 네트워크2
입력으로 주어지는 사람 네트워크에서 노드 자신을 연결하는 간선은 없다.
하나의 연결 요소(connected component)로

# input
3 0 1 0 1 0 1 0 1 0

# output: CC 값들 중에서 최솟값
==================================
사람 네트워크의 최대 사용자 수는 1,000 이하(노드 1000개 이하)
플로이드 워셜 사용불가,,,? 1_000_000_000			20초 제한이므로 가능할듯

가중치 없음, 주어진 자료는 인접행렬
1. 플로이드 워셜??
2. bfs? 

*/

import java.io.*;
import java.util.*;

public class Solution {
    static int N;
    static int[][] dist;	// dp[i][j]	// i~j 최단 거리
    
    static int INF = 1_000_000_000;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        StringTokenizer st;

        int T = Integer.parseInt(br.readLine());
        for (int tc = 1; tc <= T; tc++) {
            // 초기화

            // data
            st = new StringTokenizer(br.readLine(), " ");
            N = Integer.parseInt(st.nextToken());
            dist = new int[N][N];
            
            for (int i = 0; i < N; i++) {
				for (int j = 0; j < N; j++) {
					int temp = Integer.parseInt(st.nextToken());
					
			        if (i == j) dist[i][j] = 0;
			        else if (temp == 1) dist[i][j] = 1;
			        else dist[i][j] = INF;
				}
			}
            
            // logic: 플로이드 워셜
            for (int k = 0; k < N; k++) {
            	for (int i = 0; i < N; i++) {
            		for (int j = 0; j < N; j++) {
            			if (dist[i][k] == INF || dist[k][j] == INF) continue;
            			int cost = dist[i][k] + dist[k][j];
            			dist[i][j] = Math.min(dist[i][j], cost);
					}
				}
			}
            
            // 최소 CC 찾기
            int min = INF;
            for (int i = 0; i < N; i++) {
            	int sum = 0;
				for (int j = 0; j < N; j++) {
					sum += dist[i][j];
				}
				min = Math.min(min, sum);
			}

            // 출력
            sb.append("#").append(tc).append(" ").append(min).append('\n');
        }
        System.out.println(sb.toString());
    }
}
