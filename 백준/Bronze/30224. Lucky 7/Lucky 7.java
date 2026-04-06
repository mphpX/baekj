import java.util.*;
import java.io.*;
public class Main {
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		int n = Integer.parseInt(br.readLine());
		int ans = 0;
        int tmp = n;
		boolean isit = false;
		while(tmp>0) {
			if(tmp%10 == 7) {
				isit = true;
				break;
			}
            tmp/=10;
		}
		if(n% 7 ==0) {
			if(isit) {
				ans = 3;
			}else {
				ans = 1;
			}
		}else {
			if(isit) {
				ans = 2;
			}else {
				ans = 0;
			}
		}
		System.out.println(ans);	
	}
}