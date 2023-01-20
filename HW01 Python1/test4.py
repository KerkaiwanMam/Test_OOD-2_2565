"""
Chapter : 1 - item : 4 - Game Minesweeper
สร้างฟังก์ชันที่รับ input เป็น list(5x5) ของ # และ - โดยแต่ละแฮช (#) แทนทุ่นระเบิดและแต่ละขีด (-) แทนจุดที่ไม่มีทุ่นระเบิด ให้ return list ที่แต่ละขีดถูกแทนที่ด้วยตัวเลขที่ระบุจำนวนของทุ่นระเบิดที่อยู่ติดกับจุดนั้น (แนวนอนแนวตั้งและแนวทแยงมุม)
    Testcase : #1 1
        *** Minesweeper ***
        Enter input(5x5) : - - - - -,- - - - -,- - # - -,- - - - -,- - - - -
        ['-', '-', '-', '-', '-']
        ['-', '-', '-', '-', '-']
        ['-', '-', '#', '-', '-']
        ['-', '-', '-', '-', '-']
        ['-', '-', '-', '-', '-']
        ['0', '0', '0', '0', '0']
        ['0', '1', '1', '1', '0']
        ['0', '1', '#', '1', '0']
        ['0', '1', '1', '1', '0']
        ['0', '0', '0', '0', '0']
    Testcase : #2 2
        *** Minesweeper ***
        Enter input(5x5) : - - - # -,- # - - -,- - # - -,- - - - -,- # - - -
        ['-', '-', '-', '#', '-']
        ['-', '#', '-', '-', '-']
        ['-', '-', '#', '-', '-']
        ['-', '-', '-', '-', '-']
        ['-', '#', '-', '-', '-']
        ['1', '1', '2', '#', '1']
        ['1', '#', '3', '2', '1']
        ['1', '2', '#', '1', '0']
        ['1', '2', '2', '1', '0']
        ['1', '#', '1', '0', '0']
"""