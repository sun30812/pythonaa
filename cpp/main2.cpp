#include <iostream>
#include <syscall.h>

int menu_num;
// 함수 목록
void menus();

int main()
{
  printf("사용을 환영합니다!\n\n");
  menus();

  printf("사용해주셔서 감사합니다!!\n");

  return 0;
}

void menus()
{
  enum menus { go=1, info, exit_code };
  while (menu_num != exit_code) {
  printf("메뉴를 선택해 주십시오\n");
    printf("1. 시작하기\n");
    printf("2. 정보\n");
    printf("3. 나가기\n");
    printf("입력: "), scanf("%d", &menu_num);

    system("clear");
  }
}