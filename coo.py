import os
memo_org = []

def main() :
	a = ''
	print('=======================')
	print('간단 매모장 만들기')
	print('=======================')
	print('소개 : 간단한 메모를 표시합니다. ')
	print('\n')
	while (a != '0') :
		os.system('clear')
		print('=====================')
		print('메뉴')
		print('=====================')
		print('1. 메모 작성')
		print('2. 메모 표시')
		print('0. 프로그램 종료')
		print('')
		a = input('입력 : ')
		if (a == '1') :
			w_memo()
		elif (a == '2') : 
			v_memo()
		elif (a == '0') :
			print('프로그램울 종료합니다. ')
			break
		else :
			print('잘못 누르셨습니다. ')

def w_memo() :
	memo = ''
	print('\n\n')
	memo = input('입력할 메모 내용 : ')
	memo_org.append(memo)
	print('저장 되었습니다')
	
def v_memo() :
	a = 0
	print('\n\n')
	print('입력한 메모 목록: ')
	for index, a in enumerate(memo_org) :
		print('%d: %s' % (index+1,a))
	print('')
	print('메모 출력 완료')
main()
