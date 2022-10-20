#include <iostream>
using namespace std;
 
 
int is_array_sorted_and_rotated( int arr[], int len)
{
   int start = 0;
   int end = len - 1;
 
   while (start <= end)
   {
       int mid = (start + end) / 2;
 
       if (mid < end && arr[mid + 1] < arr[mid])  
       {
           return mid;
       }
       
       // for the case {4, 5, 1, 2, 3}
       if (mid > start && arr[mid] < arr[mid - 1])
       {
           return mid - 1;
       }
 
       // jump left half or right half
       if (arr[start] > arr[mid])
       {
           end = mid - 1;
       } else {
           start = mid + 1;
       }
   }
 
   return -1;
}
 
int main(void)
{
   int arr[] = {6, 7, 1, 2, 3, 4, 5};
   int len = sizeof(arr) / sizeof(arr[0]);
   int result = is_array_sorted_and_rotated(arr, len);
 
   if(result)
   {
       cout<<"Array is sorted and rotated"<<endl;
   } else {
       cout<<"Array is NOT sorted or NOT rotated"<<endl;
   }
 
   return 0;
}
