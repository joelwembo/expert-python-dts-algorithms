#Python program to illustrate the working of slicing function

#Using List (Without steps value)

my_List = [0,1,2,3,4,5,6,7,8,9]

#index   0,1,2,3,4,5,6,7,8,9
#index   -10,-9,-8,-7,-6,-5,-4,-3,-2,-1

slicedValueObject = slice(0,5,2)

print(my_List[slicedValueObject])