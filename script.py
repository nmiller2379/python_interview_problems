# def merge(nums1, m, nums2, n):
#     # initialize nums1_pointer to m-1 
#     nums1_pointer = m - 1
#     # intialize nums2_pointer to n-1 
#     nums2_pointer = n - 1
#     # initialize counter to n 
#     counter = n 
#     # initialize position to n + m -1 
#     position = n + m - 1
#     # While counter is > 0
#     while counter > 0:
#         # Check if nums2[nums2_pointer] >= nums1[nums1_pointer] If it is,
#         if nums2[nums2_pointer] >= nums1[nums1_pointer]: 
#             # nums1[position] = nums2[nums2_pointer] 
#             nums1[position] = nums2[nums2_pointer]
#             # nums2_pointer -= 1
#             nums2_pointer -= 1 
#             # position -= 1 
#             position -= 1 
#             # counter -= 1 
#             counter -= 1
#         # Else
#         else:
#             # nums1[position] = nums2[nums1_pointer] -> [1,2,3,3, 4]
#             nums1[position] = nums1[nums1_pointer]
#             # nums1_pointer -= 1 -> 1 (pointing at 2)
#             nums1_pointer -= 1
#             # position -= 1 -> 2
#             position -= 1
            
#     print(nums1)

# def merge(nums1, m, nums2, n):
#     # initialize nums1_pointer to m-1 
#     nums1_pointer = m - 1
#     # intialize nums2_pointer to n-1 
#     nums2_pointer = n - 1
#     # initialize counter to n 
#     position = n + m - 1
#     # While nums2_pointer is >= 0
#     while nums2_pointer >= 0:
#         # Check if nums2[nums2_pointer] >= nums1[nums1_pointer] If it is,
#         if nums2[nums2_pointer] >= nums1[nums1_pointer]: 
#             # nums1[position] = nums2[nums2_pointer] 
#             nums1[position] = nums2[nums2_pointer]
#             # nums2_pointer -= 1
#             nums2_pointer -= 1 
#             # position -= 1 
#             position -= 1 
#         # Else
#         else:
#             # nums1[position] = nums2[nums1_pointer] 
#             nums1[position] = nums1[nums1_pointer]
#             # nums1_pointer -= 1 
#             if nums1_pointer > 0:
#                 nums1_pointer -= 1
#             # position -= 1 
#             position -= 1
            
#     print(nums1)

def merge(nums1, m, nums2, n):
    nums1_pointer = m - 1
    nums2_pointer = n - 1
    position = n + m - 1
    while nums2_pointer >= 0:
        if nums1_pointer >= 0 and nums1[nums1_pointer] > nums2[nums2_pointer]:
            nums1[position] = nums1[nums1_pointer]
            nums1_pointer -= 1
        else:
            nums1[position] = nums2[nums2_pointer]
            nums2_pointer -= 1
        position -= 1
         
            
    print(nums1)

merge([1,2,3,0, 0], 3, [2, 4], 2) # [1, 2, 2, 3, 4]

merge([2,0], 1, [1], 1) # [1, 2]

merge([1], 1, [], 0) #[1]

merge([0], 0, [1], 1) #[1]
