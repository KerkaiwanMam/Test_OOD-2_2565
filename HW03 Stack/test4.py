"""
Chapter : 3 - item : 4 - Stack Calculator
ให้เขียน class calculator  ที่มีการทำงานผ่านฟังก์ชัน run(instructions) โดยมี instructions ดังนี้
    +: Pop 2 ค่าออกจาก stack, นำมาบวกกัน และ push ผลลัพธ์ลง stack
    -: Pop 2 ค่าออกจาก stack, นำค่าที่อยู่ข้างบนลบด้วยค่าที่อยู่ข้างล่าง และ push ผลลัพธ์ลง stack
    *: Pop 2 ค่าออกจาก stack, นำมาคูณกัน และ push ผลลัพธ์ลง stack
    /: Pop 2 ค่าออกจาก stack, นำค่าที่อยู่ข้างบนหารด้วยค่าที่อยู่ข้างล่าง และ push ผลลัพธ์ลง stack
    DUP: Duplicate (not double) ค่าบนสุดของ stack
    POP: Pop ค่าบนสุดออกจาก stack และ discard.
    PSH: ทำการ push ตัวเลขลง stack
หมายเหตุ คำสั่งอื่น ๆ (เช่นตัวอักษร) ควรทำให้เกิดค่า "Invalid instruction: [instruction]"
*************************************************
    Testcase : #1
        * Stack Calculator *
        Enter arguments : 5 6 +
        11
    Testcase : #2
        * Stack Calculator *
        Enter arguments : 3 DUP +
        6
    Testcase : #3
        * Stack Calculator *
        Enter arguments : 6 5 5 7 * - /
        5
    Testcase : #4
        * Stack Calculator *
        Enter arguments : a b c +
        Invalid instruction: a
"""