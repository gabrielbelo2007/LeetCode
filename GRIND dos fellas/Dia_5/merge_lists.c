#include <stdio.h>
#include <stdlib.h>

typedef struct ListNode {
    int val;
    struct ListNode *next;
}ListNode;

struct ListNode* mergeTwoLists(struct ListNode* list1, struct ListNode* list2) {
    struct ListNode ancora;
    struct ListNode *tail = &ancora;

    while (list1 != NULL && list2 != NULL) {
        if (list1->val <= list2->val) {
            tail->next = list1;
            list1 = list1->next;
        } else {
            tail->next = list2;
            list2 = list2->next;
        }
        tail = tail->next;
    }

    if (list1 != NULL) {
        tail->next = list1;
    } else {
        tail->next = list2;
    }

    return ancora.next;
}