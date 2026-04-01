import java.util.*;
import java.io.*;
public class Main {
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		StringTokenizer st;
		int n = Integer.parseInt(br.readLine());
		ArrayDeque<Integer> dq = new ArrayDeque<>();
		for(int i = 0; i < n; i++) {
			st = new StringTokenizer(br.readLine());
			int command = Integer.parseInt(st.nextToken());
			switch (command) {
			case 1:
				dq.addFirst(Integer.parseInt(st.nextToken()));
				break;
			case 2:
				dq.addLast(Integer.parseInt(st.nextToken()));
				break;
			case 3:
				if(dq.size()==0) bw.write(-1+ "\n");
				else bw.write(dq.pollFirst()+ "\n");
				break;
			case 4:
				if(dq.size()==0) bw.write(-1+ "\n");
				else bw.write(dq.pollLast()+ "\n");
				break;
			case 5:
				bw.write(dq.size()+ "\n");
				break;
			case 6:
				if(dq.size()==0) bw.write(1+ "\n");
				else bw.write(0+ "\n");
				break;
			case 7:
				if(dq.size()==0) bw.write(-1+ "\n");
				else bw.write(dq.peekFirst()+ "\n");
				break;
			case 8:
				if(dq.size()==0) bw.write(-1+ "\n");
				else bw.write(dq.peekLast()+ "\n");
				break;
			}
		}
		bw.flush();
	}
}
