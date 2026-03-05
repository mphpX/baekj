import java.io.*;
import java.util.*;
public class Main {
	static int[] arr;
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		arr = new int[5];
		int total = 0;
		for(int i = 0; i < 5; i++) {
			arr[i] = Integer.parseInt(br.readLine());
			total+= arr[i];
		}
		for(int i = 0; i < 5; i++) {
			for(int j = 1; j < 5 - i; j++) {
				if(arr[j-1] > arr[j]) {
					int tmp = arr[j];
					arr[j] = arr[j-1];
					arr[j-1]= tmp;
				}
			}
		}
		System.out.printf("%d\n%d\n", total/5, arr[2]);
		
	}
}