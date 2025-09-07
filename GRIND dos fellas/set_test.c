#include <stdio.h>

int theMaximumAchievableX(const int num, const int t) {
    const int x = t * 2 + num;
    return x;
}

int main(){

    int num = 0;
    int t = 0;

    scanf("%i", &num);
    getchar();
    scanf("%i", &t);

    const int x = theMaximumAchievableX(num, t);
    printf("%i", x);
    return x;
}