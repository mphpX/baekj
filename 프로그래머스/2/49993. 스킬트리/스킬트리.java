class Solution {
    public int solution(String skill, String[] skill_trees) {
        int answer = 0;
        int[] alpha = new int[26];
        int[] skill_idx = new int[skill.length()];
        for(int i = 0; i < skill.length(); i++){
            skill_idx[i]= (int)skill.charAt(i) - 'A';
            alpha[skill_idx[i]] = i+1;
        }
        for(int i = 0; i < skill_trees.length; i++){
            int isit= 1;
            int cur = 1;
            for(int j = 0; j < skill_trees[i].length(); j++){
                int cur_s = (int)skill_trees[i].charAt(j) - 'A';
                if(alpha[cur_s]==0)continue;
                else{
                    if(cur == alpha[cur_s]){
                        cur+=1;
                    }else{
                        isit = 0;
                        break;
                    }
                }
            }
            answer+=isit;
        }
        return answer;
    }
}