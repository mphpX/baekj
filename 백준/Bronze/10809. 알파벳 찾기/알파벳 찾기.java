import java.util.*;
import java.io.*;
public class Main {
    public static void main(String args[]) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String str = br.readLine();
        int[] rec = new int[26];
        for(int i = 0; i < 26; i++){ rec[i]= -1;}
        for(int i = 0 ; i < str.length(); i++){
            int idx= str.charAt(i)- 'a';
            if(rec[idx]==-1) rec[idx]= i;
        }
        for(int i = 0; i < 26; i++){
            System.out.printf("%d ", rec[i]);
        }
    }
}
