import java.io.*;
import java.util.*;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		int n = Integer.parseInt(br.readLine());
		int[] nums = new int[n];
		int[] sorted_nums= new int[n];
		int[] idxs= new int[n];
		StringTokenizer st = new StringTokenizer(br.readLine());
		for(int i = 0; i < n; i++) {
			nums[i]= Integer.parseInt(st.nextToken());
			sorted_nums[i]= nums[i];
		}
		Arrays.sort(sorted_nums);
		Map<Integer, Integer> hashMap = new HashMap<>();
		idxs[0] = 0;
		for(int i = 1; i < n; i++) {
			if(sorted_nums[i]==sorted_nums[i-1]) {
				idxs[i]= idxs[i-1];
			}else {
				idxs[i]= idxs[i-1]+1;
			}
		}
		for(int i = 0; i < n; i++) {
			hashMap.put(sorted_nums[i], idxs[i]);
		}
		for(int i = 0; i < n; i++) {
			bw.write(hashMap.get(nums[i])+ " ");
		}
		bw.flush();
	}
}