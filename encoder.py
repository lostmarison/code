import matplotlib.pyplot as plt


# 74HC148优先编码器
class Encoder:
    # 默认：s'=1，即所有的输出端均被所在高电平
    def __init__(self, s=1, input=[1, 1, 1, 1, 1, 1, 1, 1]):
        self.s = s
        self.input = input

    def output(self):
        seven, six, five, four, three, two, one, zero = self.input[:8]
        # Y2'
        Y2_ = (((four ^ 1) | (five ^ 1) | (six ^ 1) | (seven ^ 1)) & (self.s ^ 1)) ^ 1
        # Y1'
        Y1_ = (
            (
                ((two ^ 1) & four & five)
                | ((three ^ 1) & four & five)
                | (six ^ 1)
                | (seven ^ 1)
            )
            & (self.s ^ 1)
        ) ^ 1
        # Y0'
        Y0_ = (
            (
                ((one ^ 1) & two & four & six)
                | ((three ^ 1) & four & six)
                | ((five ^ 1) & six)
                | (seven ^ 1)
            )
            & (self.s ^ 1)
        ) ^ 1
        # Ys'
        Ys_ = (
            (zero & one & two & three & four & five & six & seven & (self.s ^ 1))
        ) ^ 1
        # Yex'
        Yex_ = (Ys_ & (self.s ^ 1)) ^ 1
        return [Y2_, Y1_, Y0_, Ys_, Yex_]


# BCD-七段显示译码器
class Decoder:
    def __init__(self, input):
        self.input = input

    def output(self):
        [three, two, one, zero] = self.input[:4]
        # Ya
        Ya = (
            ((three ^ 1) & (two ^ 1) & (one ^ 1) & zero)
            | (three & one)
            | (two & (zero ^ 1))
        ) ^ 1
        # Yb
        Yb = ((three & one) | (two & one & (zero ^ 1)) | (two & (one ^ 1) & zero)) ^ 1
        # Yc
        Yc = ((three & two) | ((two ^ 1) & one & (zero ^ 1))) ^ 1
        # Yd
        Yd = (
            (two & one & zero)
            | (two & (one ^ 1) & (zero ^ 1))
            | ((two ^ 1) & (one ^ 1) & zero)
        ) ^ 1
        # Ye
        Ye = ((two & (one ^ 1)) | zero) ^ 1
        # Yf
        Yf = (((three ^ 1) & (two ^ 1) & zero) | ((two ^ 1) & one) | (one & zero)) ^ 1
        # Yg
        Yg = (((three ^ 1) & (two ^ 1) & (one ^ 1)) | (two & one & zero)) ^ 1
        return [Ya, Yb, Yc, Yd, Ye, Yf, Yg]


# 7输入显示器
class Screen:
    def __init__(self, input):
        self.input = input

    def display(self):
        [a, b, c, d, e, f, g] = self.input[:7]
        if a == 1:
            plt.plot([-2, 2], [4, 4], "k-")  # a
        if b == 1:
            plt.plot([2, 2], [4, 0], "k-")  # b
        if c == 1:
            plt.plot([2, 2], [0, -4], "k-")  # c
        if d == 1:
            plt.plot([2, -2], [-4, -4], "k-")  # d
        if e == 1:
            plt.plot([-2, -2], [-4, 0], "k-")  # e
        if f == 1:
            plt.plot([-2, -2], [0, 4], "k-")  # f
        if g == 1:
            plt.plot([-2, 2], [0, 0], "k-")  # g
        ax = plt.gca()
        ax.set_aspect(1)
        plt.axis("off")  # 隐藏坐标轴
        plt.show()


# 独热码
# 为与74HC148输入I7'~I0'匹配，改为输入7，独热码为0010000000->1101111111
def convert(num):
    codes = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    codes[9 - num] = 0
    return codes


if __name__ == "__main__":
    # 输入数只能是0~9之间
    while True:
        try:
            num = int(input("请输入一个0到9之间的数字: "))
            if 0 <= num <= 9:
                print(f"你输入的数字是: {num}")
                break
            else:
                print("输入的数字不在0到9之间，请重新输入。")
        except ValueError:
            print("输入无效，请输入一个整数。")
    onehotcodes = convert(num)  # 转换为独热码
    # 用2片74HC148优先编码器接成二-十进制编码器
    encoder1 = Encoder(0)  # (1)片编码器
    # (1)片编码器s'接地，输入I1'，I0'，其余全部接高电平
    encoder_input1 = onehotcodes[:2]
    encoder1.input[6:8] = encoder_input1
    [Y2, Y1, Y0, Ys, Yex] = encoder1.output()
    encoder_input2 = onehotcodes[2:10]  # (2)片编码器输入
    # (1)片Ys'接(2)片S'
    encoder2 = Encoder(Ys, encoder_input2)
    [Y2_, Y1_, Y0_, Ys_, Yex_] = encoder2.output()
    Z3 = Yex ^ 1
    Z2 = (Y2 & Y2_) ^ 1
    Z1 = (Y1 & Y1_) ^ 1
    Z0 = (Y0 & Y0_) ^ 1
    decoder_input = [Z3, Z2, Z1, Z0]
    decoder = Decoder(decoder_input)
    screen = Screen(decoder.output())
    screen.display()
