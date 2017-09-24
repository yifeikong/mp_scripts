# coding: utf-8

import pyb

class MorseCode:

    char_map = {
        'a': '01',
        'b': '1000',
        'c': '1010',
        'd': '100',
        'e': '0',
        'f': '0010',
        'g': '110',
        'h': '0000',
        'i': '00',
        'j': '0111',
        'k': '101',
        'l': '0100',
        'm': '11',
        'n': '10',
        'o': '111',
        'p': '0110',
        'q': '1101',
        'r': '010',
        's': '000',
        't': '1',
        'u': '001',
        'v': '0001',
        'w': '011',
        'x': '1001',
        'y': '1011',
        'z': '1100',
        ' ': 'x'
    }

    def __init__(self, led_id, intensity):
        self.led = pyb.LED(led_id)
        self.intensity = intensity

    def translate(self, sequence):
        codes = []
        for ch in sequence:
            if ch not in self.char_map:
                continue
            intermediate = self.char_map[ch]
            intermediate = 'x'.join([c for c in intermediate])
            intermediate = intermediate.replace('0', 'y').replace('1', 'yyy')
            codes.append(intermediate)
        return 'xxx'.join(codes)

    def flash(self, sequence):
        for ch in self.translate(sequence):
            if ch == 'x':
                self.led.off()
                pyb.delay(100)
            elif ch == 'y':
                self.led.on()
                pyb.delay(100)

    def test(self):
        while True:
            self.led.intensity(self.intensity)
            pyb.delay(500)
            self.led.off()
            pyb.delay(500)

morse_code = MorseCode()
while True:
    morse_code.flash('hello world')
    pyb.delay(4000)
#morse_code.test()

