#include <stdio.h>
#include <stdlib.h>

struct Node {
    int data;
    struct Node* next;
    struct Node* prev;
};

int main() {
    struct Node* head = NULL;
    struct Node* tail = NULL;

    for (int i = 1; i <= 5; i++) {
        struct Node* newNode = malloc(sizeof(struct Node));
        newNode->data = i;
        newNode->next = NULL;
        newNode->prev = tail;
        if (tail) {
            tail->next = newNode;
        } else {
            head = newNode;
        }
        tail = newNode;
    }

    for (struct Node* current = head; current; current = current->next) {
        printf("%d ", current->data);
    }
    printf("\n");

    for (struct Node* current = tail; current; current = current->prev) {
        printf("%d ", current->data);
    }
    printf("\n");

    return 0;
}