class Solution {
    public int solution(String skill, String[] skill_trees) {
        int answer = 0;
        int[] alpha = new int[26];
        int[] skill_idx = new int[skill.length()];
        for(int i = 0; i < skill.length(); i++){
            skill_idx[i]= (int)skill.charAt(i) - 'A';
            alpha[skill_idx[i]] = -1;
        }
        alpha[skill_idx[0]]= 0;
        for(int i = 0; i < skill_trees.length; i++){
            for(int j = 0; j < 26; j++){
                alpha[j] = 0;
            }
            for(int j = 0; j < skill.length(); j++){
                skill_idx[j]= (int)skill.charAt(j) - 'A';
                alpha[skill_idx[j]] = -1;
            }
            alpha[skill_idx[0]]= 0;
            int isit= 1;
            int cur = 0;
            for(int j = 0; j < skill_trees[i].length(); j++){
                int cur_s = (int)skill_trees[i].charAt(j) - 'A';
                if(alpha[cur_s]==-1){
                    isit = 0;
                    break;
                }else{
                    if(skill_idx[cur]==cur_s){
                        cur+=1;
                        alpha[cur_s]= 1;
                        if(cur== skill.length()) break;
                        alpha[skill_idx[cur]]=0;
                    }
                }
            }
            answer+=isit;
        }
        return answer;
    }
}