import java.util.Scanner;
import java.math.BigInteger;
class Main {
	public static void move(int n ,int cur, int go) {
		if(n== 0) return;
		int mid = 6- cur- go;
		move(n-1,cur,mid);
		System.out.println(cur+" "+ go);
		move(n-1,mid,go);
	}
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int t = sc.nextInt();
		BigInteger cnt = BigInteger.TWO.pow(t).subtract(BigInteger.ONE);
		System.out.println(cnt);
		if(t<=20)move(t,1,3);
		}
}
