import java.io.*;
import java.util.*;
public class Main {
	static int[] arr;
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		int n = Integer.parseInt(st.nextToken());
		int k = Integer.parseInt(st.nextToken());
		arr = new int[n];
		st = new StringTokenizer(br.readLine());
		for(int i = 0; i < n; i++) {
			arr[i] = Integer.parseInt(st.nextToken());
		}
		for(int i = 0; i < n; i++) {
			for(int j = 1; j < n - i; j++) {
				if(arr[j-1] > arr[j]) {
					int tmp = arr[j];
					arr[j] = arr[j-1];
					arr[j-1]= tmp;
				}
			}
		}
		System.out.println(arr[n-k]);
		
	}
}