package implementation;

public class heap {
	int size;
	int[] item;
	heap(int j){
		size = 0;
		item = new int[10];
	}
	public int getParentIndex(int i){return (i-1)/2;};
	public int getLeftChildIndex(int i){return (2*i+1);};
	public int getRightChildIndex(int i){return (2*i+2);};
	
	public boolean hasParent(int i){
		if (getParentIndex(i)<0)
			return false;
		else
			return true;
	};
	
	public boolean hasLeftChild(int i){
		if(getLeftChildIndex(i)>=size)
			return false;
		else
			return true;
	}
	public boolean hasRightChild(int i ){
		if(getLeftChildIndex(i)>=size)
			return false;
		else
			return true;
	}
	
	
	public int getParent(int i){return item[getParentIndex(i)];};
	public int getLeftChild(int i){return item[getLeftChildIndex(i)];};
	public int getRightChild(int i){return item[getRightChildIndex(i)];};
	
	
	public int peek(){
		if(size==0) 
			throw new IllegalStateException();
		return item[0];
	}
	public int poll(){
		int temp = peek();
		item[0] = item[size-1];
		size--;
		heapifyDown();
		return temp;
	}
	
	public void insert(int i){
		item[size] = i;
		size++;
		heapifyUp();
	}
	
	public void swap(int indexOne, int indexTwo){
		int temp = item[indexOne];
		item[indexOne] =  item[indexTwo];
		item[indexTwo] = temp;
	}
			
	public void  heapifyDown(){
		int index = 0;
		while(hasLeftChild(index)){
			int minChildindex = getLeftChildIndex(index);
			if (hasRightChild(index) && item[minChildindex]>getRightChild(index))
				minChildindex = getRightChildIndex(index);
			if(item[index]<item[minChildindex]){
				break;
			}
			else
				swap(index,minChildindex);
			index = minChildindex;
			
			
		}
		
		
	}
	
	public void heapifyUp(){
		int index= size-1;
		while(hasParent(index) && getParent(index)>item[index]){
			int parent = getParent(index);
			swap(index,getParentIndex(index));
			index = getParentIndex(index);
			
		
		}
	}
	
	public void display(){
		for(int j=0;j<item.length;j++){
			System.out.println(item[j]);
		}
	}
	
}
