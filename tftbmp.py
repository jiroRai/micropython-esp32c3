from ST7735 import TFT,TFTColor
from machine import SPI,Pin
spi = SPI(1, baudrate=40000000, polarity=0, phase=0, sck=Pin(2), mosi=Pin(3), miso=Pin(10))
tft = TFT(spi, '/combined.bin', 6, 10, 7)  # 创建 TFT 对象，指定 SPI、字库文件路径和引脚配置
tft.init_7735(tft.GREENTAB80x160)  # 初始化 TFT，设置显示类型为 80x160 像素
tft.rgb(True)
tft.fill(TFT.BLACK)

f=open('cs-chicken.bmp', 'rb')
if f.read(2) == b'BM':  #header
    dummy = f.read(8) #file size(4), creator bytes(4)
    offset = int.from_bytes(f.read(4), 'little')
    hdrsize = int.from_bytes(f.read(4), 'little')
    width = int.from_bytes(f.read(4), 'little')
    height = int.from_bytes(f.read(4), 'little')
    if int.from_bytes(f.read(2), 'little') == 1: #planes must be 1
        depth = int.from_bytes(f.read(2), 'little')
        if depth == 24 and int.from_bytes(f.read(4), 'little') == 0:#compress method == uncompressed
            print("Image size:", width, "x", height)
            rowsize = (width * 3 + 3) & ~3
            if height < 0:
                height = -height
                flip = False
            else:
                flip = True
            w, h = width, height
            if w > 160: w = 160
            if h > 80: h = 80
            tft._setwindowloc((0,0),(w - 1,h - 1))
            for row in range(h):
                if flip:
                    pos = offset + (height - 1 - row) * rowsize
                else:
                    pos = offset + row * rowsize
                if f.tell() != pos:
                    dummy = f.seek(pos)
                for col in range(w):
                    bgr = f.read(3)
                    tft._pushcolor(TFTColor(bgr[0],bgr[1],bgr[2]))
spi.deinit()
