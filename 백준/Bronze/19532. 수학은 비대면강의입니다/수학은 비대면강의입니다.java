import java.io.*;
import java.util.*;
public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		int[] arr = new int[6];
		for(int i = 0; i < 6; i++) {
			arr[i]= Integer.parseInt(st.nextToken());
		}
		int cur = 0;
		for(int x = -999; x < 1000; x++) {
			for(int y = -999; y < 1000; y++) {
				cur = 0;
				if(arr[cur]*x + arr[cur+1]*y==arr[cur+2]) {
					cur+=3;
					if(arr[cur]*x + arr[cur+1]*y==arr[cur+2]) {
						System.out.printf("%d %d\n", x,y);
						System.exit(0);
					}
				}
			}
		}
	}
}