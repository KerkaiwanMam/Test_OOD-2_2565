"""
Chapter : 2 - item : 2 - Class BUS
การทำงานไม่ถูกต้อง มีจุดผิดดังนี้
- ไม่มีการใช้ self
- เมท็อด people_in, people_out และ change_fare ต้องไม่คืนค่า
- เมท็อด people_out ไม่ได้ตรวจสอบว่า จำนวนคนน้อยกว่าศูนย์หรือไม่
    Testcase : #1 1
        Enter people in Bus1, Bus2, fare Bus1, Bus2 : 10 8 7 3
        this bus has 8 people with fare = 3
        this bus has 7 people with fare = 12
    Testcase : #2 2
        Enter people in Bus1, Bus2, fare Bus1, Bus2 : 1 4 3 6
        this bus has 1 people with fare = 3
        this bus has 0 people with fare = 12
"""
