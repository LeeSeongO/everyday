"""
다음과 같이 숫자로 이루어진 배열이 두 개가 있다. 하나는 상품의 가격을 담은 배열이고, 하나는 쿠폰을 담은 배열이다.
쿠폰의 할인율에 따라 상품의 가격을 할인 받을 수 있다. 이 때, 최대한 할인을 많이 받는다면 얼마를 내야 하는가?
쿠폰, 할인율의 단위는 % 입니다.
"""
shop_prices = [30000, 2000, 1500000]
user_coupons = [20, 40]


def get_max_discounted_price(prices, coupons):
    prices.sort(reverse=True)
    coupons.sort(reverse=True)

    price_index = 0
    coupon_index = 0
    max_discount_price = 0

    while price_index < len(prices) and coupon_index < len(coupons):
        max_discount_price += prices[price_index] * (1 - (coupons[coupon_index] * 0.01))
        price_index += 1
        coupon_index += 1

    while price_index < len(prices):
        max_discount_price += prices[price_index]
        price_index += 1

    return int(max_discount_price)


print(get_max_discounted_price([30000, 2000, 1500000], [20, 40]))