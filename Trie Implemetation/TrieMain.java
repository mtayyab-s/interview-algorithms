package heapPackage;

public class TrieMain {
	public static void main(String[] args){
		Trie t = new Trie();
		t.insert("abcd");
		t.insert("abc");
		t.delete("abcd");
		System.out.println(t.search("abcd"));
	}

}
