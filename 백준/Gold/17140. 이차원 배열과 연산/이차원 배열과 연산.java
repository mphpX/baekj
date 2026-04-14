/*
문제: 이차원 배열과 연산
크기가 3×3인 배열 A
1-based

# 연산
	R 연산: 
	C 연산: 
# 정렬 규칙: 횟수 오름차순, 숫자 오름차순
행, 열 가장 큰 것 기준으로 0으로 채우기, 0은 정렬할 때 무시
100개까지만 인정

# input
1 2 2	// r, c, k가 주어진다. (1 ≤ r, c, k ≤ 100)
1 2 1
2 1 3
3 3 3

# output:  A[r][c]에 들어있는 값이 k가 되기 위한 최소 시간
100초 안에 불가능하면 -1 출력
*/

import java.io.*;
import java.util.*;

public class Main {
    static int r, c, k;
    static int[][] A;
    static int rCnt, cCnt;	// 행의 개수와 열의 개수

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        // 초기화
        st = new StringTokenizer(br.readLine(), " ");
        r = Integer.parseInt(st.nextToken()) - 1;
        c = Integer.parseInt(st.nextToken()) - 1;
        k = Integer.parseInt(st.nextToken());
        A = new int[100][100];
        rCnt = cCnt = 3;
        
        for (int i = 0; i < 3; i++) {
        	st = new StringTokenizer(br.readLine(), " ");
        	for (int j = 0; j < 3; j++) {
        		A[i][j] = Integer.parseInt(st.nextToken());
			}
		}
        // logic
        int ans = -1;
        for (int time = 0; time <= 100; time++) {
			// A[r][c] == k이면 종료
        	if (A[r][c] == k) {
        		ans = time;
        		break;
        	}
        	
        	// 행 >= 열: R 연산
        	if (rCnt >= cCnt) {
        		rOpration();
        	} else {	// C 연산
        		cOperation();
        	}
		}

        // 출력
        System.out.println(ans);
    }

    private static void cOperation() {
        A = transpose(A);
        int temp = rCnt;
        rCnt = cCnt;
        cCnt = temp;

        rOpration();

        A = transpose(A);
        temp = rCnt;
        rCnt = cCnt;
        cCnt = temp;
    }

    static int[][] transpose(int[][] arr) {
        int[][] temp = new int[100][100];

        for (int i = 0; i < rCnt; i++) {
            for (int j = 0; j < cCnt; j++) {
                temp[j][i] = arr[i][j];
            }
        }

        return temp;
    }

	/*
	 * 배열 A의 모든 행에 대해서 정렬을 수행한다
	 */
    private static void rOpration() {
        int[][] newArr = new int[100][100];

        int rMax = 0;
        for (int r = 0; r < rCnt; r++) {
        	int[] res = customSort(A[r], cCnt);

            if (res.length > 100) {
                res = Arrays.copyOf(res, 100);
            }

            rMax = Math.max(rMax, res.length);

            for (int i = 0; i < res.length; i++) {
                newArr[r][i] = res[i];
            }
        }

        A = newArr;
        cCnt = rMax;
    }

	/*
	 * arr의 배열에 커스텀 정렬을 적용한 배열을 리턴한다.
	 */
    static int[] customSort(int[] arr, int len) {

	    Map<Integer, Integer> map = new HashMap<>();

	    // 1. 카운팅 (0 제외)
	    for (int i = 0; i < len; i++) {
	        int num = arr[i];
	        if (num == 0) continue;
	        map.put(num, map.getOrDefault(num, 0) + 1);
	    }

	    // 2. 리스트 변환
	    List<int[]> list = new ArrayList<>();
	    for (Map.Entry<Integer, Integer> entry : map.entrySet()) {
	        list.add(new int[]{entry.getKey(), entry.getValue()});
	    }
	    
	    // 3. 정렬
	    Collections.sort(list, (a, b) -> {
	        if (a[1] == b[1]) return a[0] - b[0];
	        return a[1] - b[1];
	    });

	    // 4. 결과 배열
	    int size = list.size() * 2;
	    int[] res = new int[Math.min(size, 100)];

	    int idx = 0;
	    for (int[] pair : list) {
	        if (idx >= 100) break;
	        res[idx++] = pair[0];

	        if (idx >= 100) break;
	        res[idx++] = pair[1];
	    }

	    return res;
	}
}
