//*******************************************************************
// List Merge
// 
// Take two sorted lists and merge them into a singular sorted list.
//
// Author: Drew Fisher
// Date: 6/12/18
//*******************************************************************

public class Main
{
  public static void main(String[] args)
  {
    int[] list1 = {-7, -1, 0, 6, 12};
    int[] list2 = {-44, 1, 3, 6, 9, 12, 44};
    int[] merged = ListMerge.MergeSortedLists(list1, list2);
    for (int i = 0; i < merged.length; i++) {
      System.out.print(merged[i] + " ");
    }
  }
}

public class ListMerge {
  public static int[] MergeSortedLists(int[] l1, int[] l2) {
    int[] mergedList = new int[l1.length + l2.length];
    
    int pos1 = 0;
    int pos2 = 0;
    
    for (int i = 0; i < l1.length + l2.length; i++) {
      //add l2 values if l1 is exhausted
      if (pos1 >= l1.length) {
        mergedList[i] = l2[pos2];
        pos2++;
        continue;
      }
      //add l1 values if l2 is exhausted
      if (pos2 >= l2.length) {
        mergedList[i] = l1[pos1];
        pos1++;
        continue;
      }
      int curr1 = l1[pos1];
      int curr2 = l2[pos2];
      if (curr1 < curr2) {
        mergedList[i] = curr1;
        pos1++;
      } else {
        mergedList[i] = curr2;
        pos2++;
      }
    }
    return mergedList;
  }
  
}
