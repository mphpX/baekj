import java.io.*;
import java.util.*;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		int n = Integer.parseInt(br.readLine());
		ArrayList<Integer> list = new ArrayList<>(10);
		int idx = 0;
		while(n>0) {
			list.add(n%10);
			n/=10;
			idx+=1;
		}
		list.sort(Comparator.reverseOrder());
		for(int i = 0; i < idx; i++) {
			bw.write(list.get(i)+'0');
		}
		bw.flush();
	}
}