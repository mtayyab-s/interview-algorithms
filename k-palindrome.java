/*
Please note that it's Function problem i.e.
you need to write your solution in the form of Function(s) only.
Driver Code to call/invoke your function would be added by GfG's Online Judge.

*http://practice.geeksforgeeks.org/problems/k-palindrome/1
* K-Palindrome
* Muhammad Tayyab
* 11/11/2017
*/


class GfG
{
    String reverse(String s){
        String temp = "";
        for(int i = s.length()-1; i>=0; i--){
            temp = temp+s.charAt(i);
        }
        return temp;
    }
    
    int mini(int a, int b){
        if(a<b)
            return a;
        else
            return b;
    }
    boolean is_k_palin(String str, int k)
    {
       String rev_s = reverse(str);
       int n = str.length();
       int m = rev_s.length();
      
	   int[][] table = new int[n+1][m+1];
	   
	   for(int b=0;b<table.length;b++){
	       table[0][b] = b;
	       table[b][0]= b;
	   
	   }
	  
	  for(int p =1;p<table.length;p++){
	      for(int q =1;q<table[0].length;q++){
	            if(str.charAt(p-1) == rev_s.charAt(q-1))
	                table[p][q] = table[p-1][q-1];
	            else
	                table[p][q] = 1+mini(table[p][q-1],table[p-1][q]);
	                
	            
	      }
	  }
	   int f = (table[table.length-1][table[0].length-1]);
       if(f<=2*k)
	    return true;
	   else
	    return false;
	    
    }
}