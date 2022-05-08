## Midterm 1 Practice Tasks 2021
#### **1. Zoo ticket price**

Output:
```
How many visitors?: 3
Total price is 300 baht.
```
#### **2. Can you sleep?**

If this day was a vacation day and a weekday. You can sleep.

If this day was a vacation day but not a weekday. You can sleep.

If this day was not a vacation day and not a weekday. You can sleep.

If this day not a vacation day and this day was a weekday. You can't sleep.

Output:
```
Is a week day?(y/n): y
Is a vacation?(y/n): y
You can sleep.
```
```
Is a week day?(y/n): n
Is a vacation?(y/n): n
You can sleep.
```
```
Is a week day?(y/n): y
Is a vacation?(y/n): n
You cannot sleep.
```
```
Is a week day?(y/n): n
Is a vacation?(y/n): y
You can sleep.
```
#### **3. Above Average**
Output:
```
Please enter a: 3
Please enter b: 1
Please enter c: 5
Please enter d: 4
2 of these numbers are above average:
5.0
4.0
```
```
Please enter a: -1.2
Please enter b: 4.2
Please enter c: 15
Please enter d: 5
1 of these numbers are above average:
15.0
```
```
Please enter a: 1
Please enter b: 1
Please enter c: 1
Please enter d: 1
0 of these numbers are above average:

```
```
Please enter a: -100
Please enter b: 1
Please enter c: 3
Please enter d: 2
3 of these numbers are above average:
1.0
3.0
2.0
```
#### **4. Water Unit Calculator**

0-7 units = 110฿/unit (เหมาจ่าย)

8-18 units = 18฿/unit

19-43 units = 21.5฿/unit

44-80 units = 25฿/unit

more than 80 units = 10.5฿/unit

Output:

```
Unit: 7
Cost: 110.00 baht
```
```
Unit: 14
Cost: 236.00 baht
```
```
Unit: 31
Cost: 587.50 baht
```
```
Unit: 50
Cost: 1020.00 baht
```
Shell Mode:
```
>>> find_cost(14)
236
```
