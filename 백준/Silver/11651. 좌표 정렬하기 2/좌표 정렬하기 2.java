import java.io.*;
import java.util.*;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		int n = Integer.parseInt(br.readLine());
		int[][] nums = new int[n][2];

		for(int i = 0; i < n; i++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			nums[i][0]= Integer.parseInt(st.nextToken());
			nums[i][1]= Integer.parseInt(st.nextToken());
		}
		Arrays.sort(nums, (a, b) -> {
			if(a[1]!=b[1]) return Integer.compare(a[1], b[1]);
			return Integer.compare(a[0], b[0]);
		});
		
		for(int i = 0; i < n; i++) {
			bw.write(nums[i][0]+ " "+ nums[i][1]);
			bw.write("\n");
		}
		bw.flush();
	}
}