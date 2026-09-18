void moveZeroes(int* nums, int numsSize) {
    int k = 0;
    int i;
    for(i=0;i<numsSize;i++){
        if(nums[i]!=0){
            nums[k] = nums[i];
            k++;
        }
    }
    for(i=k;i<numsSize;i++){
        nums[i] =0;
    }
}