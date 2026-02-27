import java.io.*;
import java.util.*;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		String N = st.nextToken();
		int B = Integer.parseInt(st.nextToken());
		int ans = 0;
		int mul = 1;
		for(int i = N.length()-1; i > -1; i--) {
			char cur = N.charAt(i);
			if(cur < 'A') {
				 ans+=(int)(cur- '0')*mul;
			}else {
				ans+= ((int)(cur-'A')+10)*mul;
			}
			mul*=B;
		}
		System.out.println(ans);
	}
}
