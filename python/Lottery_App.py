import random

prize_pool = 0


def menu():
    # set prize pool
    set_prize_pool(input("Enter the Total Prize Pool:: "))
    print("The Prize Pool is:: {}".format(prize_pool))
    # Calculate lottery numbers
    lotto_nums = create_lottery_numbers()
    # Ask Player for numbers
    user_nums = get_player_numbers()
    # Print out the winnings
    amount_of_matched_nums = len(get_matched_nums(user_nums, lotto_nums))
    print("Matched Numbers:: {}".format(amount_of_matched_nums))
    winnings = get_winnings(amount_of_matched_nums)
    print("You won ..... ${}".format(winnings))


# User can pick 6 numbers
def get_player_numbers():
    numbers_csv = raw_input("Enter 6 numbers, seperated by commas: ")
    # print("Numbers_CSV:: {}".format(numbers_csv))
    # Create a set of integers from this numbers_csv
    # integer_set = {int(num) for num in numbers_csv.split(",")}
    # return integer_set
    return {int(num) for num in numbers_csv.split(",")}


def create_lottery_numbers():
    # initialise an empty set
    values = set()  # can not initialise like so: {}
    while len(values) < 6:
        values.add(random.randint(1, 20))
    print("The winning numbers is:: {}".format(values))
    return values


def get_matched_nums(set1, set2):
    return set1.intersection(set2)


def set_prize_pool(total):
    global prize_pool
    prize_pool = total


def get_winnings(matched_nums):
    if matched_nums == 6:
        return prize_pool * 0.42
    elif matched_nums == 5:
        return prize_pool * 0.25
    elif matched_nums == 4:
        return prize_pool * 0.15
    elif matched_nums == 3:
        return prize_pool * 0.05
    elif matched_nums == 2:
        return prize_pool * 0.02
    elif matched_nums == 1:
        return prize_pool * 0.01
    else:
        return 0


# Then we match the user numbers to the lottery numbers
# Calculate the winnings based on how many numbers the user matched
if __name__ == '__main__':
    menu()
