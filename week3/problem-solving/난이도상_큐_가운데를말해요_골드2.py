# 큐 - 가운데를 말해요 (백준 골드2)
# 문제 링크: https://www.acmicpc.net/problem/1655


# 더미노드를 만들고 헤드가 가리키게함
head = ListNode()

# result도 헤드랑 같은 더미노드를 가리키게함
result = head

# 올림수 할 변수 0으로 초기화
plus = 0

# l1이 가리키는게 아무것도 없을때까지
while l1 is not None and l2 is not None:
    # l1의 val과 l2의 va1을 더하고, 올림수가 있다면 더해준다
    # 맨 뒷자리는 올릴 필요가 없음
    sum = l1.val + l2.val + plus

    # 더해주고 초기화
    plus = 0

    # 두수를 더해서 10을 넘으면 올림수를 1 올려줌
    if sum >= 10:
        plus = 1

    # 두수를 저장한 값을 새 노드에 저장함
    new_node = ListNode(sum%10)

    #result가 가리키는 더미노드의 next가 새 노드를 가리키게함(처음만)
    # 다음부터는 result가리키는 노드의 next가 새 노드를 가리키게함
    result.next = new_node

    #이제 result의 next가 있기 때문에 result에 저장해줌
    result = result.next  

    #l1이 가리키는 곳을 다음으로 옮겨줌
    l1 = l1.next

    #l2가 가리키는 곳을 다음으로 옮겨줌
    l2 = l2.next

# l1과 l2가 길이가 다를 경우 위의 반복문을 나오고 끝남
# l1과 l2 중 남은 노드가 있을 경우 계산해주는 while문 두개
# l1이 가리키는게 None이 아닐때까지
while l1 is not None:

    # l1의 val과 올림수(있다면) 더해주기
    sum = l1.val + plus

    # sum을 10으로 나눈 나머지를 더해주기
    new_node = ListNode(sum%10)
    
    #위에서 이미 sum값에 올림수를 더해주었기 때문에 올림수 초기화
    plus = 0

    # 다음 수에 올림수 계산해놓기. sum이 10 이상이면 플러스1
    if sum >= 10:
        plus = 1
    
    # result가 가리키는 노드의 next가 새 노드를 가리키게함
    result.next = new_node

    #result가 result가 원래 가리키는 노드가, 가리키는 곳에 있는 노드를 가리키게됨
    result = result.next
    
    #l1이 가리키는 곳을 다음 노드로 옮겨줌
    l1 = l1.next

#l2가 가리키는게 None이 아닐때까지
# 왜 l2.next가 아닌지는 한번 그려보면 알게됨(sum에 저장하지 않고 반복문을 나가버림)
while l2 is not None:

    # sum에 l2에 val과 올림수를 저장해줌
    sum = l2.val + plus

    #새로운 노드에 sum값을 10으로 나눈 나머지를 저장
    new_node = ListNode(sum%10)

    #위의 계산결과를 sum에 넣어주었으니 plus는 초기화
    plus = 0

    #sum이 10 이상이면 올림수 1해주기
    if sum >= 10:
        plus = 1
    
    #현재 result가 가리키는 노드의 넥스트가 새 노드를 가리키게함
    result.next = new_node

    #result가 result가 가리키는 노드의 넥스트가 가리키는 곳을 가리키게됨
    result = result.next
    l2 = l2.next

# 맨 마지막 자리수는 10이 넘어가면 그 다음 올림수가 나와야함
if plus == 1:
    
    #새 노드를 만들고 val으로 1을 줌
    new_node = ListNode(1)

    # result가 현재 가리키는 노드의 next가 새 노드를 가리키게 연결
    # result는 노드를 연결시키기 위해 none을 가리키는 가장 마지막 노드를 가리키고 있음
    result.next = new_node

# head부터 하면 더미노드도 출력되기 때문에 head.next
return head.next
