class adsort:
    def partition(arr,low,high): 
        i = ( low-1 )         # 最小元素索引
        pivot = arr[high]       
        for j in range(low , high):   
            # 当前元素小于或等于 pivot 
            if   arr[j] <= pivot:           
                i = i+1 
                arr[i],arr[j] = arr[j],arr[i]   
        arr[i+1],arr[high] = arr[high],arr[i+1] 
        return ( i+1 )    
    # arr[] --> 排序数组
    # low  --> 起始索引
    # high  --> 结束索引  
    # 快速排序函数
    def quickSort(arr,low,high): 
        if low < high: 
            pi = adsort.partition(arr,low,high) 
            adsort.quickSort(arr, low, pi-1) 
            adsort.quickSort(arr, pi+1, high)

        
    
    #归并排序
    def mergeSort(arr,left,right):
        if left>=right:
            return arr
        mid=(left+right)>>1
        adsort.mergeSort(arr,left,mid)
        adsort.mergeSort(arr,mid+1,right)
        adsort.merge(arr,left,mid,right)
    
    #归并排序之合并
    def merge(arr,left,mid,right):
        result=[]
        i,j=left,mid+1
        while i<=mid and j<=right:
            if arr[i]<=arr[j]:
                result.append(arr[i])
                i+=1
            else:
                result.append(arr[j])
                j+=1
        while i<=mid:
            result.append(arr[i])
            i+=1
        while j<=right:
            result.append(arr[j])
            j+=1
        arr[left:right+1]=result
  





arr1 = [9,7,6,3,1,8,6,4,2]
arr2 = [8,6,4,2,9,7,3,1]
n1 = len(arr1)
n2 = len(arr2)
adsort.quickSort(arr1,0,n1-1)
adsort.mergeSort(arr2,0,n2-1)
print ("快速排序后的数组:",arr1)
print ("归并排序后的数组:",arr2)

