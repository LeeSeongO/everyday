"""
Q. 라면 공장에서는 하루에 밀가루를 1톤씩 사용합니다.
원래 밀가루를 공급받던 공장의 고장으로 앞으로 k일 이후에야 밀가루를
공급받을 수 있기 때문에 해외 공장에서 밀가루를 수입해야 합니다.

해외 공장에서는 향후 밀가루를 공급할 수 있는 날짜와 수량을 알려주었고,
라면 공장에서는 운송비를 줄이기 위해 최소한의 횟수로 밀가루를 공급받고 싶습니다.

현재 공장에 남아있는 밀가루 수량 stock, 밀가루 공급 일정(dates)과 해당 시점에
공급 가능한 밀가루 수량(supplies), 원래 공장으로부터 공급받을 수 있는 시점 k가 주어질 때,
밀가루가 떨어지지 않고 공장을 운영하기 위해서 최소한 몇 번 해외 공장으로부터 밀가루를 공급받아야 하는지를 반환하시오.

dates[i]에는 i번째 공급 가능일이 들어있으며, supplies[i]에는 dates[i] 날짜에 공급 가능한 밀가루 수량이 들어 있습니다.
"""



import heapq

ramen_stock = 4
supply_dates = [4, 10, 15]
supply_supplies = [20, 5, 10]
supply_recover_k = 30


# 고려해야 할 사항
"""
조건 1. 최소한의 공급이 목표이기때문에 최소한의 횟수로 부족한 밀가루를 가져오기 위해서는 
       밀가루가 제일 많은 것을 가져오면 된다. 즉 supplies_max 를 반복해서 가져오면서 k와 비교하면된다는 뜻..
       
하지만 제약조건이 stock 이 비면 공장이 멈추기 떄문에 stock 이 떨어지기 전까지 공급량들 중에서 가장 큰값을 넣어야 한다.

last_added_date_index < len(dates) // dates 안에있는 값들 중 선택 하기 위한 조건
dates[last_added_date_index] <= stock 
"""

def get_minimum_count_of_overseas_supply(stock, dates, supplies, k):
    # 공급 횟수를 저장할 변수
    answer = 0

    # heap에 supplies 값을 저장할때 중복된 값을 저장하지 않도록 인덱스를 저장해놓는다.
    last_dates_index = 0

    # spplies 의 최대 공급량을 저장하기 위한 heap
    max_heap = []

    # stock: 현재 가지고있는 물량 - 하루에 1씩 감소 // k: 최대 버텨야 되는 일수 .
    # 목표: 현재 가지고있는 물량이 최대일수보다 많으면 된다.. 빠져나와서 공급한 횟수를 반환
    while stock <= k:
        # 조건 1. 현재 가지고있는 stock // dates 의 날짜보다 적으면 공급이 중단되므로 체크
        # 조건 2. 최소의 공급을 원하므로 == 최대 공급량.. 조건 1에 부합되는 모든 supplies 값들을 max_heap 으로 저장
        while last_dates_index < len(dates) and dates[last_dates_index] <= stock:
            # 최대 값을 저장하기 위해서는 * -1
            heapq.heappush(max_heap, supplies[last_dates_index] * -1)
            # 탈출 조건
            last_dates_index += 1

        # 예외 처리 공급할 수 있는 일이 없거나 공급량이 부족할경이 while 문을 거치지 않기 때문에
        if len(max_heap) == 0:  # not max_heap
            return '공급일 or 공급량이 부족합니다.'

        # 가지고있는 stock + 최대 공급량을 더해준다.
        stock += heapq.heappop(max_heap) * -1
        # 위의 while 문을 거치면 공급 1번을 한것이기때문에 answer += 1
        answer += 1

    return answer



print(get_minimum_count_of_overseas_supply(ramen_stock, supply_dates, supply_supplies, supply_recover_k))
print(get_minimum_count_of_overseas_supply(4, [4, 10, 15, 20], [20, 5, 10, 5], 40))
print(get_minimum_count_of_overseas_supply(4, [5, 10, 15, 20], [20, 5, 10, 5], 40))









