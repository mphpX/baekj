import java.io.*;
import java.util.*;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		int n = Integer.parseInt(br.readLine());
		StringTokenizer st;
		for(int i = 0; i < n; i++) {
			st= new StringTokenizer(br.readLine());
			int m = Integer.parseInt(st.nextToken());
			String str = st.nextToken();
			for(int j = 0; j< str.length(); j++) {
				for(int k = 0; k < m; k++) bw.write(str.charAt(j));
			}
			bw.write('\n');
		}
		bw.flush();
	}
}
