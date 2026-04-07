/*
문제: [모의 SW 역량테스트] 점심 식사시간
계단의 입구는 반드시 2개이며, 서로 위치가 겹치지 않는다.
계단마다 길이 K가 주어지며, 계단에 올라간 후 완전히 내려가는데 K 분이 걸린다.
계단 위에는 동시에 최대 3명까지만 올라가 있을 수 있다.

# input
5
0 1 1 0 0
0 0 1 0 3
0 1 0 1 0
0 0 0 0 0
1 0 5 0 0

# output: 모든 사람들이 계단을 내려가 이동이 완료되는 시간의 최소값
#1 9
===========================================================
->1. 시뮬레이션 풀이
2. 배열로 압축

*/

import java.io.*;
import java.util.*;

public class Solution {

    static int N;
    static List<int[]> people;
    static int[][] stairs; // [2][3] -> r, c, length
    static int personCount;

    static int[] selected;
    static int answer;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        int T = Integer.parseInt(br.readLine());

        for (int tc = 1; tc <= T; tc++) {
            N = Integer.parseInt(br.readLine());

            people = new ArrayList<>();
            stairs = new int[2][3];

            int stairIdx = 0;

            for (int i = 0; i < N; i++) {
                st = new StringTokenizer(br.readLine());
                for (int j = 0; j < N; j++) {
                    int val = Integer.parseInt(st.nextToken());

                    if (val == 1) {
                        people.add(new int[]{i, j});
                    } else if (val > 1) {
                        stairs[stairIdx][0] = i;
                        stairs[stairIdx][1] = j;
                        stairs[stairIdx][2] = val;
                        stairIdx++;
                    }
                }
            }

            personCount = people.size();
            selected = new int[personCount];
            answer = Integer.MAX_VALUE;

            dfs(0);

            System.out.println("#" + tc + " " + answer);
        }
    }

    // 완전탐색
    static void dfs(int idx) {
        if (idx == personCount) {
            simulate();
            return;
        }

        selected[idx] = 0;
        dfs(idx + 1);

        selected[idx] = 1;
        dfs(idx + 1);
    }

    // 시뮬레이션
    static void simulate() {

        // 계단별 도착시간 저장
        List<Integer> arr1 = new ArrayList<>();
        List<Integer> arr2 = new ArrayList<>();

        for (int i = 0; i < personCount; i++) {
            int[] p = people.get(i);
            int s = selected[i];

            int dist = Math.abs(p[0] - stairs[s][0]) +
                       Math.abs(p[1] - stairs[s][1]);

            int arrive = dist + 1; // 핵심: +1

            if (s == 0) arr1.add(arrive);
            else arr2.add(arrive);
        }

        int t1 = simulateStair(arr1, stairs[0][2]);
        int t2 = simulateStair(arr2, stairs[1][2]);

        answer = Math.min(answer, Math.max(t1, t2));
    }

    // 계단 하나 시뮬
    static int simulateStair(List<Integer> arrival, int K) {
        if (arrival.isEmpty()) return 0;

        Collections.sort(arrival);

        Queue<Integer> wait = new LinkedList<>();   // 대기
        Queue<Integer> stair = new LinkedList<>();  // 내려가는 중 (남은 시간)

        int time = 0;
        int idx = 0; // arrival 인덱스

        while (true) {
            time++;

            // 1. 계단 내려가는 사람 처리
            int size = stair.size();
            for (int i = 0; i < size; i++) {
                int t = stair.poll() - 1;
                if (t > 0) stair.add(t);
            }

            // 2. 도착한 사람 -> 대기열
            while (idx < arrival.size() && arrival.get(idx) <= time) {
                wait.add(arrival.get(idx));
                idx++;
            }

            // 3. 계단 진입 (최대 3명)
            while (stair.size() < 3 && !wait.isEmpty()) {
                wait.poll();
                stair.add(K);
            }

            // 4. 종료 조건
            if (idx == arrival.size() && wait.isEmpty() && stair.isEmpty()) {
                break;
            }
        }

        return time;
    }
}