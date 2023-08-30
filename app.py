import os, time
os.system("clear")

tempo = 0.5

for i in range(11):
    if i == 5:
        text = "::FIRST APP::"
        print(f'{text:^25}')
    else:
        print("-------[]-------[]-------")
    time.sleep(tempo)