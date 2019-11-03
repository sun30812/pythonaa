#include <iostream>

// 함수 목록
void menus();

int main()
{
    enum menus {go, info, exit};

    printf("사용을 환영합니다!\n");
    printf("1. 시작하기\n");
    printf("2. 정보\n");
    printf("3. 나가기\n");
}