num = int(input())
meeting_list = []

for i in range(num):
    meeting_list.append(list(map(int, input().split())))

meeting_list.sort(key=lambda x: (x[1], x[0])) 

end_time = meeting_list[0][1]
cnt = 1

for i in range(1, len(meeting_list)):
    if end_time <= meeting_list[i][0]:
        end_time = meeting_list[i][1]
        cnt += 1
print(cnt)


'''
2차원 리스트 정렬
 - 2차원 배열에서 sort의 기본값: list.sort()
    : 0번째 리스트를 오름차순 정렬하고 같은 값의 경우 오름차순으로 재정렬
 
 - 첫번째 값 이용하기
 list.sort(key=lambda x:x[0])

 - 두번째 값 이용하기
 list.sort(key=lambda x: (x[0], -x[1]))
    : 0번째 인덱스에 대해서 오름차순으로 정렬한 뒤 동일한 값의 경우 내림차순으로 재정렬
'''
