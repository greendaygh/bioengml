def average(input):
    if len(input) == 0:
        return None
    return sum(input) / len(input)


if __name__ == "__main__":
    test_input = [1,2,3,4,5,6,7,8,9,10]
    if average(test_input) == 5.5:
        print("average function is working well")
    else:
        print("Something wrong!")


        