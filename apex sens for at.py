def sens():
    sens = float(input("напиши свою сенсу в апекс >> "))
    sens1x = sens * 0.751654
    sens2xads = sens * 0.656481
    sens2xopt = sens * 0.410291
    sens3x = sens * 0.264755
    sens4x = sens * 0.196342
    sens6x = sens * 0.129851
    sens8x = sens * 0.097117
    sens10x = sens * 0.077593
    print("Сенса 1х =", sens1x, "fov = 93.90", end="\n")
    print("Сенса 2х ads =", sens2xads, "fov = 85.84", end="\n")
    print("Сенса 2х optic =", sens2xopt, "fov = 59.42", end="\n")
    print("Сенса 3х =", sens3x, "fov = 39.59", end="\n")
    print("Сенса 4х =", sens4x, "fov = 29.25", end="\n")
    print("Сенса 6х =", sens6x, "fov = 18.71", end="\n")
    print("Сенса 8х =", sens8x, "fov = 13.38", end="\n")
    print("Сенса 10х =", sens10x, "fov = 10.17", end="\n")
    input()
sens()
