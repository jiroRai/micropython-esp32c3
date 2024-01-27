from machine import SPI, Pin  # 导入 SPI 和 Pin 类模块
from ST7735 import TFT, bitSwap, FontLib  # 导入 TFT、bitSwap 和 FontLib 类模块
import time  # 导入 time 模块
import framebuf  # 导入 framebuf 模块
import random  # 导入 random 模块

USE_FRAME_BUFFER = True  # 设置使用帧缓冲器（frame buffer）

# 初始化 SPI 接口，设置波特率、极性、相位和引脚号
spi = SPI(1, baudrate=40000000, polarity=0, phase=0, sck=Pin(2), mosi=Pin(3), miso=Pin(10))#无需修改

tft = TFT(spi, '/combined.bin', 6, 10, 7)  # 创建 TFT 对象，指定 SPI、字库文件路径和引脚配置
#由于直接应用了/combined.bin字体库可以直接写中文
tft.init_7735(tft.GREENTAB80x160)  # 初始化 TFT，设置显示类型为 80x160 像素
tft.fill(TFT.BLACK)  # 填充屏幕为白色，实际显示为黑色

#上述都无需改动

#不停显示字符
text=['你好！','世界！','在干嘛？','上号！','氪不改非']
font_width = 11
font_height = 14
def show_text():
    x,y=random.randint(0,120),random.randint(0,60)+1
    r = random.randint(0,4)
    tft.fillrect((x,y),(font_width*len(text[r]),font_height),TFT.color(random.randint(0,255),random.randint(0,255),random.randint(0,255)))
    tft.text(
        (x,y),
        text[r],
        TFT.color(random.randint(0,255),random.randint(0,255),random.randint(0,255)),
        1
    )
    time.sleep_ms(200)
if __name__=="__main__":

    while True:
        time.sleep(1)
        for i in range(100):
            show_text()
        tft.fill(TFT.BLACK) 
