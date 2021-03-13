# Winter Hardcastle
# Neopixel visualizer using stock program

# needs neopixel installed, and needs to be in the same directory as stockisup.py
import stockisup as stonks
import time
import board
import neopixel


pixel_pin = board.D18  # Neopixel I/O pin on RPI

num_pixels = 567  # Total Num of pixels

num_room_pixels = 510  # Total num of pixels I want to use for the visualizer

ORDER = neopixel.GRB  # RGB order

# defining pixels
pixels = neopixel.NeoPixel(
    pixel_pin, num_pixels, brightness=1, auto_write=False, pixel_order=ORDER
)


# Create a list of indexes for each stock
# Size of section depending of num stocks in portfolio
def sections():

    ticker_list = stonks.tickers()
    sect_length = num_room_pixels // len(ticker_list)
    sect_dict = {}
    total = 0

    for ticker in ticker_list:
        sect_dict.update({ticker: []})
        for j in range(1, sect_length):
            total += 1
            sect_dict[ticker].append(total)

    return sect_dict


# iterates over the sections dictionary and sets the different sections to
# green or red depending on if their assigned stock is up or down


def visualizer(wait):
    sect_dict = sections()
    for ticker in sect_dict:
        color = stonks.red_or_green(ticker)
        if color == "down":
            for i in sect_dict[ticker]:
                pixels[i] = (255, 0, 0)
        if color == "up":
            for i in sect_dict[ticker]:
                pixels[i] = (0, 255, 0)
    pixels.show()
    time.sleep(wait)
    return


# refresh rate
how_long = int(input("Enter refresh interval (seconds)") or "60")

while True:
    visualizer(how_long)
