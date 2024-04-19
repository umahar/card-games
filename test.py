def card_average(hand):
    """Calculate and returns the average card value from the list.

    :param hand: list - cards in hand.
    :return: float - average value of the cards in the hand.
    """

    average = sum(hand)/len(hand)
    return average

def approx_average_is_average(hand):
    """Return if the (average of first and last card values) OR ('middle' card) == calculated average.

    :param hand: list - cards in hand.
    :return: bool - does one of the approximate averages equal the `true average`?
    """
    actual_average = card_average(hand)
    average = (hand[0]+hand[-1])/2
    median = hand[len(hand)//2]
    print(actual_average)
    print(average)
    print(median)
    return actual_average == average or actual_average== median


print(approx_average_is_average([1, 2, 4, 5, 8]))