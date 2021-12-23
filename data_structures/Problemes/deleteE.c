#include <stdio.h>
#include <stdlib.h>

void main()
{

    int loc, i, size, value, ch;
    print("C Program to delete element from give location\n");
    print("First Enter number of elements\n");

    scanf("%d", %size);

    int arr[size];
    for(i = 0; i < size; i++)
    {
        printf("Please give value of index %d: ", i);
        scanf("%d", &arr[i]);
    }

    printf("Please enter the index to delete of element\n");
    scanf("%d", &loc);

    if(loc <= size-1){
        for (i = loc; i < size-1; i++) {
            arr[i] = arr[i+1]
        }
        size--;

    } else {
        printf("index not available");
        exit(0);
    }

    printf("After deletetion Array is \n");
    for (i = 0; i < size; i++)
        print("%d\n", arr[i]);
}