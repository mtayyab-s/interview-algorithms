/*
 * Trie data structure implementation
 * insert,delete,seach time complexities O(k) 
 * k is the length of the word
 * @author: Muhammad Tayyab
 * date: 01/17/2018
 */



package heapPackage;
import java.util.HashMap;
import java.util.Map;


public class Trie {
		private class TrieNode{
			Map<Character,TrieNode> children;
			boolean endOfWord;
			
			TrieNode(){
				children = new HashMap<>();
				endOfWord = false;
			}
		}
		
		final TrieNode root;
		
		Trie( ){
			 root = new TrieNode();
			 
	    }
		
		// time complexity is O(l(average length of word)x n(no. of words)
		public void insert(String word){
			TrieNode current = root;
			for(int i=0;i<word.length();i++){
				char ch = word.charAt(i);
				TrieNode node = current.children.get(ch);
				if(node==null){
					node = new TrieNode();
					current.children.put(ch,node);
				}
				current = node;
				
			}
			current.endOfWord = true;
		}
		
		public boolean search(String word){
			TrieNode current = root;
			for(int i=0;i<word.length();i++){
				char ch = word.charAt(i);
				TrieNode node  = current.children.get(ch);
				if(node==null)
					return false;
				current = node;
				
				}
			return current.endOfWord;
			}
		
		
		
		
		
		public void delete(String word){
			del(root,word,0);
			
		}
		
		public boolean del(TrieNode current,String word, int index){
			if(index == word.length()){
				if(current.endOfWord== false)
					return false;
				current.endOfWord = false;
				return current.children.size()==0;
						
			}
			char ch = word.charAt(index);
			TrieNode node = current.children.get(ch);
			
			if(node == null)
				return false;
			boolean shouldDelete = del(node,word,index+1);
			
			if(shouldDelete){
				current.children.remove(ch);
				return current.children.size() ==0;
			}
			return false;
		}
	
			
	}


