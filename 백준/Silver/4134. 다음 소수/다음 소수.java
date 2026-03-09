import java.io.*;
import java.util.*;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		int n = Integer.parseInt(br.readLine());
		boolean[] nums = new boolean[200001];
		boolean isit = true;
		nums[2]= nums[3]= true;
		for(int i = 4; i < 200001; i++) {
			isit = true;
			for(int j = 2; j <= Math.sqrt(i); j++) {
				if(nums[j] && i%j ==0) {
					isit = false;
					break;
				}
			}
			if(isit) nums[i]= true;
		}
		for(int i = 0; i < n; i++) {
			long a= Long.parseLong(br.readLine());
			while(true) {
                isit = true;
				if(a < 200001) {
                    int x = (int)a;
					if(nums[x]){
                        break;
                    }
				}else{
                    for(long j = 2; j <= Math.sqrt(a); j++){
                        if(a% j ==0){
                            isit = false;
                            break;
                        }
                    }
                    if(isit){
                        break;
                    }
                }
                a+=1;
			}
            bw.write(a + "\n");
		}
        bw.flush();
	}
}   