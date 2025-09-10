#include <string.h>
#include <stdbool.h>
#include <stdlib.h>

bool isValid(char* s)
{
    char *order = (char *)malloc(strlen(s) + 1);
    int index = -1;

    for (int i = 0; i < strlen(s); i++){
        switch (s[i]){
            case '(':
            case '[':
            case '{':
                index++;
                order[index] = s[i];
                break;
            case ')':
                if (index == -1 || order[index] != '(')
                {
                    free(order);
                    return false;
                }
                index--;
                break;
            case '}':
                if (index == -1 || order[index] != '{')
                {
                    free(order);
                    return false;
                }
                index--;
                break;
            case ']':
                if (index == -1 || order[index] != '[')
                {
                    free(order);
                    return false;
                }
                index--;
                break;
            default:
                break;
        }
    }

    bool result = (index == -1);
    free(order);
    return result;
}
