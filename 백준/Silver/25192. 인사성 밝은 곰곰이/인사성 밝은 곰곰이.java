import java.util.*;
import java.io.*;
public class Main {
    public static void main(String args[]) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        Map <String, Integer> ht = new HashMap<>();
        int n = Integer.parseInt(br.readLine());
        String name;
        int cur = 0;
        int ans = 0;
        for(int i = 0; i < n; i++){
            name= br.readLine();
            if(name.equals("ENTER")){
                cur+=1;
            }else{
                if(ht.containsKey(name)){
                    if(ht.get(name) == cur){
                        continue;
                    }else{
                        ans+=1;
                        ht.put(name,cur);
                    }
                }else{
                    ht.put(name, cur);
                    ans+=1;
                }
            }
        }
        System.out.println(ans);
    }
}