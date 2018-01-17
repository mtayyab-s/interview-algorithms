package implementation;

public class mainHeap {
	public static void main(String[] args){
		heap h = new heap(4);
		h.insert(7);
		h.insert(9);
		h.insert(10);
		h.insert(1);
		h.display();
	}

}
