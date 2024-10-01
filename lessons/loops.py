from random import randint


def number_gsr(secret_num: int) -> list:
    j = 0
    stats = []
    while j < 432:
        j += 1
        number = 0
        i = 0
        while number != 1:
            number = randint(1, 10)
            # print("Guess " + str(i + 1) + " was: " + str(number))
            i += 1
        print("It took " + str(i) + " random guesses to guess my secret number: 1")
        stats = stats_stor(last_dur=i, prev_stats=stats)
    return stats


def stats_stor(last_dur: int, prev_stats: list) -> list:
    stats = prev_stats
    stats += [last_dur]
    return stats


def data_anal(stats: list) -> None:
    index = 0
    sum = 0
    while index < len(stats):
        sum += stats[index]
        index += 1
    print("total # of rounds " + str((len(stats))))
    print("Average time to guess: " + str(sum / len(stats)))


data_anal(stats=number_gsr(secret_num=1))
