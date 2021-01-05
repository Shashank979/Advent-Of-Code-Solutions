
def part1():
    with open('day2part1.txt') as f:
        advent_text = [line.strip() for line in f.readlines()]
    print(advent_text)
    counter_2 = 0
    counter_3 = 0
    a = 0
    b = 0
    c = 0
    d = 0
    e = 0
    f = 0
    g = 0
    h = 0
    i = 0
    j = 0
    k = 0
    l = 0
    m = 0
    n = 0
    o = 0
    p = 0
    q = 0
    r = 0
    s = 0
    t = 0
    u = 0
    v = 0
    w = 0
    x = 0
    y = 0
    z = 0
    for string1 in advent_text:
        for char1 in string1:
            if char1 == "a":
                a += 1
            elif char1 == "b":
                b += 1
            elif char1 == "c":
                c += 1
            elif char1 == "d":
                d += 1
            elif char1 == "e":
                e += 1
            elif char1 == "f":
                f += 1
            elif char1 == "g":
                g += 1
            elif char1 == "h":
                h += 1
            elif char1 == "i":
                i += 1
            elif char1 == "j":
                j += 1
            elif char1 == "k":
                k += 1
            elif char1 == "l":
                l += 1
            elif char1 == "m":
                m += 1
            elif char1 == "n":
                n += 1
            elif char1 == "o":
                o += 1
            elif char1 == "p":
                p += 1
            elif char1 == "q":
                q += 1
            elif char1 == "r":
                r += 1
            elif char1 == "s":
                s += 1
            elif char1 == "t":
                t += 1
            elif char1 == "u":
                u += 1
            elif char1 == "v":
                v += 1
            elif char1 == "w":
                w += 1
            elif char1 == "x":
                x += 1
            elif char1 == "y":
                y += 1
            elif char1 == "z":
                z += 1
        if a == 2 or b == 2 or c == 2 or d == 2 or e == 2 or f == 2 or g == 2 or h == 2 or i == 2 or j == 2 or k == 2 or l == 2 or m == 2 or n == 2 or o == 2 or p == 2 or q == 2 or r == 2 or s == 2 or t == 2 or u == 2 or v == 2 or w == 2 or x == 2 or y == 2 or z == 2:
            counter_2 += 1
            '''
            print(string1)
            print(
            string1.count("a"),
            string1.count("b"),
            string1.count("c"),
            string1.count("d"),
            string1.count("e"),
            string1.count("f"),
            string1.count("g"),
            string1.count("h"),
            string1.count("i"),
            string1.count("j"),
            string1.count("k"),
            string1.count("l"),
            string1.count("m"),
            string1.count("n"),
            string1.count("o"),
            string1.count("p"),
            string1.count("q"),
            string1.count("r"),
            string1.count("s"),
            string1.count("t"),
            string1.count("u"),
            string1.count("v"),
            string1.count("w"),
            string1.count("x"),
            string1.count("y"),
            string1.count("z"))'''
        if a == 3 or b == 3 or c == 3 or d == 3 or e == 3 or f == 3 or g == 3 or h == 3 or i == 3 or j == 3 or k == 3 or l == 3 or m == 3 or n == 3 or o == 3 or p == 3 or q == 3 or r == 3 or s == 3 or t == 3 or u == 3 or v == 3 or w == 3 or x == 3 or y == 3 or z == 3:
            counter_3 += 1
            print(string1)
            print(
            string1.count("a"),
            string1.count("b"),
            string1.count("c"),
            string1.count("d"),
            string1.count("e"),
            string1.count("f"),
            string1.count("g"),
            string1.count("h"),
            string1.count("i"),
            string1.count("j"),
            string1.count("k"),
            string1.count("l"),
            string1.count("m"),
            string1.count("n"),
            string1.count("o"),
            string1.count("p"),
            string1.count("q"),
            string1.count("r"),
            string1.count("s"),
            string1.count("t"),
            string1.count("u"),
            string1.count("v"),
            string1.count("w"),
            string1.count("x"),
            string1.count("y"),
            string1.count("z"))
        a = 0
        b = 0
        c = 0
        d = 0
        e = 0
        f = 0
        g = 0
        h = 0
        i = 0
        j = 0
        k = 0
        l = 0
        m = 0
        n = 0
        o = 0
        p = 0
        q = 0
        r = 0
        s = 0
        t = 0
        u = 0
        v = 0
        w = 0
        x = 0
        y = 0
        z = 0
            
    print("Counter 2: ", counter_2)
    print("Counter 3: ", counter_3)
    checksum = counter_2 * counter_3
    print("Checksum: ", checksum)



def part2():
    with open('day2part1.txt') as f:
        advent_text = [line.strip() for line in f.readlines()]
    compare_s = advent_text[0]
    incorrect = 0
    del advent_text[0]
    while incorrect != 1:
        for s1 in advent_text:
            for num in range(len(s1)):
                if compare_s[num] != s1[num]:
                    incorrect += 1
            if incorrect == 1:
                print(compare_s)
                print(s1)
                break
            incorrect = 0
        compare_s = advent_text[0]
        del advent_text[0]
        
part2()
