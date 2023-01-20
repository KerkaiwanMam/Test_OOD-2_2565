"""
Chapter : 3 - item : 2 - Parenthesis Matching
จงเขียนโปรแกรมเพื่อตรวจสอบว่า นิพจน์มีวงเล็บครบถ้วนหรือไม่ โดยใช้ Stack ช่วยในการแก้ปัญหา
โดยสามารถแจ้งได้ว่าข้อผิดพลาดที่เกิดขึ้นเกิดจากสาเหตุใด
1. มี วงเปิดไม่ตรงชนิดกับวงเล็บปิด
2. วงเล็บปิดเกิน
3. วงเล็บเปิดเกิน
    Testcase : #1 
        Enter expresion : [[)))))
        [[))))) Unmatch open-close  
    Testcase : #2 
        Enter expresion : [[))
        [[)) Unmatch open-close  
    Testcase : #3
        Enter expresion : (())))
        (()))) close paren excess
    Testcase : #4 
        Enter expresion : )}]
        )}] close paren excess
    Testcase : #5 
        Enter expresion : (((
        ((( open paren excess   3 : (((
    Testcase : #6 
        Enter expresion : (a+c)(a-b)*c(-a
        (a+c)(a-b)*c(-a open paren excess   1 : (
"""