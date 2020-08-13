def main():
    socks_number = int(input())
    socks_list = list(map(int, input().split()))  # make str numbers to list of number
    socks_heap = [[socks_list[j], j+1] for j in range(socks_number)]
    socks_heap.sort(key=lambda  x: x[0])

    useless = []
    useful = []
    helper = [-1, -1]
    for i in range(socks_number):

        if helper[0] == -1:
            helper = socks_heap[i]
        else:

            amount_pop = socks_heap[i]
            if amount_pop[0] == helper[0]:
                if(helper[1]< amount_pop[1]):
                    useful.append([helper[1], amount_pop[1]])
                    helper[0] = -1
                else:
                    useful.append([amount_pop[1], helper[1]])
                    helper[0] = -1
            else:

                useless.append(helper)
                helper = amount_pop
    useful.sort(key= lambda x: x[0])
    print(len(useful))
    for item in useful:
        print(str(item[0])+" "+str(item[1]))

if __name__ == "__main__":
    main()