def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
     """
    Do not return anything, modify nums1 in-place instead.
    """
    
    if m==0:  
        for k in range(n):
            nums1[k]=nums2[k]
    else:
        i=j=0
        while j<len(nums2):
            if nums1[m+j-1]<=nums2[j]:
                nums1[m+j]=nums2[j]
                j+=1
                    
            else:
                for i in range(m+n):
                    if nums1[i]>nums2[j]:
                        t=nums1[i]
                        nums1[i]=nums2[j]
                        nums2[j]=t
