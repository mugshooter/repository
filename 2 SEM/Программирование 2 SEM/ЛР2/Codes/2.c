int main()
{
    int a, b, sum;
    int *ptr1, *ptr2;

    printf("Enter two numbers: ");
    scanf("%d %d", &a, &b);

    ptr1 = &a;
    ptr2 = &b;

    sum = *ptr1 + *ptr2;

    printf("Sum is %d\n", sum);
    return 0;
}