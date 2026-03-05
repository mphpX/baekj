import java.io.*;
import java.util.*;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		int n = Integer.parseInt(br.readLine());
		String[] words = new String[n];
		int[][] arr = new int[n][2];
		StringTokenizer st;
		for(int i = 0; i < n; i++) {
			st= new StringTokenizer(br.readLine());
			arr[i][0]= Integer.parseInt(st.nextToken());
			arr[i][1]= i;
			words[i]= st.nextToken();
		}
		Arrays.sort(arr, (a,b)->{
			if(a[0]!= b[0]) return Integer.compare(a[0], b[0]);
			return Integer.compare(a[1], b[1]);
		});
		for(int i = 0; i < n; i++) {
			bw.write(arr[i][0] + " "+ words[arr[i][1]]);
			bw.write("\n");
		}
		bw.flush();
	}
}