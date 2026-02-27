import java.io.*;
import java.util.*;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		StringTokenizer st;
		int max_x= 0;
		int max_y= 0;
		int ans= 0;
		int x= 0;
		for(int i = 0; i < 9; i++) {
			st= new StringTokenizer(br.readLine());
			for(int j = 0; j < 9; j++) {
				x= Integer.parseInt(st.nextToken()); 
				if(ans < x) {
					max_x = i;
					max_y = j;
					ans = x;
				}
			}
		}
		System.out.printf("%d\n%d %d", ans, max_x+1, max_y+1);
	}
}
