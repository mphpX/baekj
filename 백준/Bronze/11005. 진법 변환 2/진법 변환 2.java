import java.io.*;
import java.util.*;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		int N = Integer.parseInt(st.nextToken());
		int B = Integer.parseInt(st.nextToken());
		
		StringBuilder sb = new StringBuilder(10);
		int cur = 0;
		while(N>0) {
			cur = N % B;
			if(cur<10) {
				sb.append(cur);
			}else {
				sb.append((char)('A'+(cur-10)));
			}
			N/=B;
		}
		System.out.println(sb.reverse().toString());
	}
}
