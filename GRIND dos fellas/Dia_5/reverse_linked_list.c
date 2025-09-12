#include <stdio.h>
#include <stdlib.h>

typedef struct ListNode {
    int val;
    struct ListNode *next;
}ListNode;

ListNode* reverseList(struct ListNode* head){
    ListNode *head_reversed = NULL;

    if (head != NULL)
    {
        while (head != NULL){
            ListNode *p = (ListNode*)malloc(sizeof(ListNode));
            p->val = head->val;
            p->next = head_reversed;

            head_reversed = p;

            if(head != NULL){
                head = head->next;
            }
        }
    }

    return head_reversed;
}
