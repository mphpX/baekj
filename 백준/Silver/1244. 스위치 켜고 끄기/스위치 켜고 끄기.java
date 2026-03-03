import java.io.*;
import java.util.*;
public class Main {

	public static void main(String[] args) throws IOException{
		//---------솔루션 코드를 작성하세요.
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int n = Integer.parseInt(br.readLine());
		StringTokenizer st = new StringTokenizer(br.readLine());
		int[] leds= new int[n+1];
		for(int i = 1; i <= n ;i++) {
			leds[i]= Integer.parseInt(st.nextToken());
		}
		int m = Integer.parseInt(br.readLine());
		
		for(int i = 0; i <m ; i++) {
			st = new StringTokenizer(br.readLine());
			int sex = Integer.parseInt(st.nextToken());
			int idx = Integer.parseInt(st.nextToken());
			if(sex == 1) {
				int p = idx;
				for(int j = p; j <=n; j+=p) {
					leds[j]= (leds[j]+1)%2;
				}
			}else {
				int left =idx-1;
				int right=idx+1;
				while(true) {
					if(left< 1 || right >n || leds[left]!=leds[right]) {
						break;
					}
					left--;
					right++;
				}
				for(int j = left+1; j <=right-1; j++) {
					leds[j]= (leds[j]+1)%2;
				}
			}
		}
		int cur = 1;
		System.out.printf("%d ",leds[cur++]);
		while(cur<=n) {
			if(cur%20 ==1) {
				System.out.println();
			}
			System.out.printf("%d ", leds[cur++]);
		}
	}

}
