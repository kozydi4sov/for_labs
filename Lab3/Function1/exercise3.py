def math(head, leg):
    rab = leg / 2 - head
    chick = head - rab
    return int(rab), int(chick)
head = int(input())
leg = int(input())
print(math(head, leg))