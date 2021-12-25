import math

prodolzhit= 'у'

while prodolzhit == 'у':
    i=float(input('Введите первое число\n'))
    j=float(input('Введите второе число\n'))
    oper=input('Введите одну из операций:\nплюс\nминус 1 из 2\nминус 2 из 1\nумножить\nделить 1 на 2\nделить 2 на 1\nстепень 1 из 2\nстепень 2 из 1\nкорень\nкорень плюс\nкорень минус 1 из 2\nкорень минус 2 из 1\nкорень умножить\nкорень разделить 1 на 2\nкорень разделить 2 на 1\nкорень 1 из 2\nкорень 2 из 1\nмодуль\nмодуль плюс\nмодуль минус 1 из 2\nмодуль минус 2 из 1\nмодуль умножить\nмодуль делить 1 на 2\nмодуль делить 2 на 1\nцелое значение >\nцелое значение <\nкосинус\nкосинус плюс\nкосинус минус 1 из 2\nкосинус минус 2 из 1\nкосинус умножить\nкосинус делить 1 на 2\nкосинус делить 2 на 1\nсинус\nсинус плюс\nсинус минус 1 из 2\nсинус минус 2 из 1\nсинус умножить\nсинус делить 1 на 2\nсинус делить 2 на 1\nтангенс\nтангенс плюс\nтангенс минус 1 из 2\nтангенс минус 2 из 1\nтангенс умножить\nтангенс делить 1 на 2\nтангенс делить 2 на 1\nарккосинус\nарккосинус плюс\nарккосинус минус 1 из 2\nарккосинус минус 2 из 1\nарккосинус умножить\nарккосинус делить 1 на 2\nарккосинус делить 2 на 1\nарксинус\nарксинус плюс\nарксинус минус 1 из 2\nарксинус минус 2 из 1\nарксинус умножить\nарксинус делить 1 на 2\nарксинус делить 2 на 1\nарктангенс\nарктангенс плюс\nарктангенс минус 1 из 2\nарктангенс минус 2 из 1\nарктангенс умножить\nарктангенс делить 1 на 2\nарктангенс делить 2 на 1\n\n')

    if oper == 'плюс':
        print(i + j)
    elif oper == 'минус 1 из 2':
        print(i - j)
    elif oper == 'минус 2 из 1':
        print(j - i)
    elif oper == 'умножить':
         print(i * j)

    elif oper == 'степень 1 из 2':
        print(pow(i,j))
    elif oper == 'степень 2 из 1':
        print(pow(j,i))

    elif oper == 'косинус':
        print(math.cos(i),   math.cos(j))
    elif oper == 'косинус плюс':
        print(math.cos(i) + math.cos(j))
    elif oper == 'косинус минус 1 из 2':
        print(math.cos(i) - math.cos(j))
    elif oper == 'косинус минус 2 из 1':
        print(math.cos(j) - math.cos(i))
    elif oper == 'косинус умножить':
        print(math.cos(i) * math.cos(j))
    elif oper == 'косинус делить 1 на 2':
        print(math.cos(i) / math.cos(j))
    elif oper == 'косинус делить 2 на 1':
        print(math.cos(j) / math.cos(i))

    elif oper == 'синус':
        print(math.sin(i),   math.sin(j))
    elif oper == 'синус плюс':
        print(math.sin(i) + math.sin(j))
    elif oper == 'синус минус 1 из 2':
        print(math.sin(i) - math.sin(j))
    elif oper == 'синус минус 2 из 1':
        print(math.sin(j) - math.sin(i))
    elif oper == 'синус умножить':
        print(math.sin(i) * math.sin(j))
    elif oper == 'синус делить 1 на 2':
        print(math.sin(i) / math.sin(j))
    elif oper == 'синус делить 2 на 1':
        print(math.sin(j) / math.sin(i))

    elif oper == 'тангенс':
        print(math.tan(i),   math.tan(j))
    elif oper == 'тангенс плюс':
        print(math.tan(i) + math.tan(j))
    elif oper == 'тангенс минус 1 из 2':
        print(math.tan(i) - math.tan(j))
    elif oper == 'тангенс минус 2 из 1':
        print(math.tan(j) - math.tan(i))
    elif oper == 'тангенс умножить':
        print(math.tan(i) * math.tan(j))
    elif oper == 'тангенс делить 1 на 2':
        print(math.tan(i) / math.tan(j))
    elif oper == 'тангенс делить 2 на 1':
        print(math.tan(j) / math.tan(i))

    elif oper == 'арккосинус':
        print(math.acos(i),   math.acos(j))
    elif oper == 'арккосинус плюс':
        print(math.acos(i) + math.acos(j))
    elif oper == 'арккосинус минус 1 из 2':
        print(math.acos(i) - math.acos(j))
    elif oper == 'арккосинус минус 2 из 1':
        print(math.acos(j) - math.acos(i))
    elif oper == 'арккосинус умножить':
        print(math.acos(i) * math.acos(j))
    elif oper == 'арккосинус делить 1 на 2':
        print(math.acos(i) / math.acos(j))
    elif oper == 'арккосинус делить 2 на 1':
        print(math.acos(j) / math.acos(i))

    elif oper == 'арксинус':
        print(math.asin(i),   math.asin(j))
    elif oper == 'арксинус плюс':
        print(math.asin(i) + math.asin(j))
    elif oper == 'арксинус минус 1 из 2':
        print(math.asin(i) - math.asin(j))
    elif oper == 'арксинус минус 2 из 1':
        print(math.asin(j) - math.asin(i))
    elif oper == 'арксинус умножить':
        print(math.asin(i) * math.asin(j))
    elif oper == 'арксинус делить 1 на 2':
        print(math.asin(i) / math.asin(j))
    elif oper == 'арксинус делить 2 на 1':
        print(math.asin(j) / math.asin(i))

    elif oper == 'арктангенс':
        print(math.atan(i),   math.atan(j))
    elif oper == 'арктангенс плюс':
        print(math.atan(i) + math.atan(j))
    elif oper == 'арктангенс минус 1 из 2':
        print(math.atan(i) - math.atan(j))
    elif oper == 'арктангенс минус 2 из 1':
        print(math.atan(j) - math.atan(i))
    elif oper == 'арктангенс умножить':
        print(math.atan(i) * math.atan(j))
    elif oper == 'арктангенс делить 1 на 2':
        print(math.atan(i) / math.atan(j))
    elif oper == 'арктангенс делить 2 на 1':
        print(math.atan(j) / math.atan(i))

    elif oper == 'модуль':
         print(math.fabs(i),   math.fabs(j))
    elif oper == 'модуль плюс':
        print(math.fabs(i) + math.fabs(j))
    elif oper == 'модуль минус 1 из 2':
        print(math.fabs(i) - math.fabs(j))
    elif oper == 'модуль минус 2 из 1':
        print(math.fabs(j) - math.fabs(i))
    elif oper == 'модуль умножить':
        print(math.fabs(i) * math.fabs(j))
    elif oper == 'модуль делить 1 на 2':
        print(math.fabs(i) / math.fabs(j))
    elif oper == 'модуль делить 2 на 1':
        print(math.fabs(j) / math.fabs(i))

    elif oper == 'целое значение >':
        print(math.ceil(i), math.ceil(j))
    elif oper == 'целое значение <':
        print(math.floor(i), math.floor(j))
        
    while i>0 and j>0 :
        if oper == 'корень':
            print(math.sqrt(i),   math.sqrt(j))
        elif oper == 'корень плюс':
            print(math.sqrt(i) + math.sqrt(j))
        elif oper == 'корень минус 1 из 2':
            print(math.sqrt(i) - math.sqrt(j))
        elif oper == 'корень минус 2 из 1':
            print(math.sqrt(j) - math.sqrt(i))
        elif oper == 'корень умножить':
            print(math.sqrt(i) * math.sqrt(j))
        elif oper == 'корень разделить 1 на 2':
            print(math.sqrt(i) / math.sqrt(j))
        elif oper == 'корень разделить 2 на 1':
            print(math.sqrt(j) / math.sqrt(i))
        break

    while i>0:
        if oper == 'корень 1 из 2':
            print(i**(1/j))
        break

    while  j>0:
        if oper == 'корень 2 из 1':
            print(j**(1/i))
        break

    while j>0:
        if oper == 'делить 1 на 2':
            print(i / j)
        break

    while i>0:
        if oper == 'делить 2 на 1':
            print(j / i)
        break
    prodolzhit=input("Ввдеите 'у', чтобы продолжить, или 'n', чтобы завершить\n")
    

     
