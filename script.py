def merge(nums1, m, nums2, n):
    # 1.  Iterate thrhough nums1[:m]
    for index, num in enumerate(nums1[:m]):
    # 2. Check if element in nums1 is greater than element in nums2
        if num > nums2[0]:
        # 3. If it is, store the value
            value = num
        # 4. assign the nums2 value to the index position
            nums1[index] = nums2[0]
        # 5. assign the stored value to the index position + 1
            nums1[m] = value

print(merge([1,2,3,0, 0], 3, [2, 4], 2))