#include <stdbool.h>
#include <string.h>
#include <ctype.h>

bool isPalindrome(char* s) {
    int size_s = strlen(s) - 1;
    int index = 0;
    for (int i = 0; i < strlen(s); i++)
    {
        if (isalnum(s[i]))
        {
            while (!isalnum(s[size_s - index]))
            {
                index++;
            }
            if (tolower(s[i]) != tolower(s[size_s - index]))
            {
                return false;
            }
            index++;
        }
    }
    return true;
}