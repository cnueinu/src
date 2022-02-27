import re
import math

def extract_integers(question):
    regular_expression = re.compile('[0-9]+')
    result = regular_expression.findall(question)
    return [int(i) for i in result], result

def extract_floats(question):
    result = re.findall('\d*\.?\d+', question)
    return [float(i) for i in result], result

def convert_special_characters(question):
    a = "－＋×÷＝"
    b = "-+*/="
    
    new_string = ""

    for c in question:
        for i in range(len(a)):
            if c == a[i]:
                new_string += b[i]
                break
            if i == len(a)-1:
                new_string += c
    
    return new_string

def convert_fraction_to_decimal(question):
    question_ = question
    integers, str_integers = extract_integers(question)
    for i in range(len(str_integers)):
        if i == 0: continue
        before_point = str_integers[i-1]
        after_point = str_integers[i]

        if question[question.find(after_point)-1] == '/':
            str_fraction = before_point + '/' + after_point
            after_replacement = str(eval(str_fraction))
            question_ = question_.replace(str_fraction, after_replacement)
    return question_

def convert_letters_to_digits(question):
    question = question.replace(" 한 ", " 1")
    question = question.replace(" 두 ", " 2")
    question = question.replace(" 세 ", " 3")
    question = question.replace(" 네 ", " 4")
    question = question.replace(" 다섯 ", " 5")
    question = question.replace(" 여섯 ", " 6")
    question = question.replace(" 일곱 ", " 7")
    question = question.replace(" 여덟 ", " 8")
    question = question.replace(" 아홉 ", " 9")
    question = question.replace(" 열 ", " 10")

    question = question.replace(" 일의", " 1의")
    question = question.replace(" 십의", " 10의")    
    question = question.replace(" 백의", " 100의")
    question = question.replace(" 천의", " 1000의")
    question = question.replace(" 만의", " 10000의")
    question = question.replace(" 십만의", " 100000의")
    question = question.replace(" 백만의", " 1000000의")
    question = question.replace(" 천만의", " 10000000의")
    question = question.replace(" 일억의", " 100000000의")
    question = question.replace(" 십억의", " 1000000000의")  

    return question

def convert_numbers_to_digits(question):
    number = ["영", "일", "이", "삼", "사", "오", "육", "칠", "팔", "구", "십",
              "십일", "십이", "십삼", "십사", "십오", "십육", "십칠", "십팔", "십구", "이십",
              "이십일", "이십이", "이십삼", "이십사", "이십오", "이십육", "이십칠", "이십팔", "이십구", "삼십",
              "삼십일", "삼십이", "삼십삼", "삼십사", "삼십오", "삼십육", "삼십칠", "삼십팔", "삼십구", "사십",
              "사십일", "사십이", "사십삼", "사십사", "사십오", "사십육", "사십칠", "사십팔", "사십구", "오십",
              "오십일", "오십이", "오십삼", "오십사", "오십오", "오십육", "오십칠", "오십팔", "오십구", "육십",
              "육십일", "육십이", "육십삼", "육십사", "육십오", "육십육", "육십칠", "육십팔", "육십구", "칠십",
              "칠십일", "칠십이", "칠십삼", "칠십사", "칠십오", "칠십육", "칠십칠", "칠십팔", "칠십구", "팔십",
              "팔십일", "팔십이", "팔십삼", "팔십사", "팔십오", "팔십육", "팔십칠", "팔십팔", "팔십구", "구십",
              "구십일", "구십이", "구십삼", "구십사", "구십오", "구십육", "구십칠", "구십팔", "구십구", "백"]

    digit = []
    for i in range(101):
        digit.append(str(i))
    
    expression = ["각", "면"]

    for i in range(len(number)):
        for e in expression:
            if number[-i]+e in question:
                question = question.replace(number[-i]+e, digit[-i]+e)
    
    return question


def factorial(number):
    if number <= 1: return "1"

    equation = ""

    for i in range(100):
        if equation != "":
            equation += "*"
        equation += str(number)        
        if number <= 1: break
        number -= 1

    return equation    

def combination(number1, number2):
    equation = "(%s) / ((%s) * (%s))" % (factorial(number1), factorial(number2), factorial(number1-number2))
    return equation

def permutation(number1, number2):
    equation = "(%s) / (%s)" % (factorial(number1), factorial(number1-number2))
    return equation

def split_lists(question, integers, postfix1, postfix2):
    question = " " + question

    first = []
    second = []
    others = []

    if postfix2 == "": postfix2 = "qrhpqhwethqwpoerqwoeriqwjroiwm;zlxkmcv"

    for i in range(len(integers)):
        text1 = " " +str(integers[i]) + postfix1
        text2 = " " +str(integers[i]) + postfix2
        if text1 in question:
            first.append(integers[i])
            question = question.replace(text1, "", 1)
        elif text2 in question:
            second.append(integers[i])
            question = question.replace(text2, "", 1)
        else:
            others.append(integers[i])
    return first, second, others

def split_lists2(question, integers, postfix1, postfix2):
    question = " " + question

    first = []
    second = []
    others = []

    if postfix2 == "": postfix2 = "qrhpqhwethqwpoerqwoeriqwjroiwm;zlxkmcv"

    for i in range(len(integers)):
        text1 = "" +str(integers[i]) + postfix1
        text2 = "" +str(integers[i]) + postfix2
        if text1 in question:
            first.append(integers[i])
            question = question.replace(text1, "", 1)
        elif text2 in question:
            second.append(integers[i])
            question = question.replace(text2, "", 1)
        else:
            others.append(integers[i])
    return first, second, others

def get_answer(question, equation):
    if equation == "": return "0", "0"

    if isinstance(eval(equation), str):
        answer = str(eval(equation))
    elif "소수" in question or "소숫" in question:
        equation = '"{:.2f}".format(' + equation + ')'
        answer = "{:.2f}".format(float(eval(equation)))
    #elif "사람" in question or "누구" in question or "수는 어느" in question:
    #    answer = str(eval(equation))
    else:
        equation = "int(%s)" % (equation)
        answer = str(int(eval(equation)))
    return answer, equation

def extract_alphabets(sentence):
    result = ""
    for i in range(len(sentence)):
        if sentence[i] >= 'A' and sentence[i] <= 'Z':
            result += sentence[i] 
    return result

def extract_unique_alphabets(sentence):
    result = []
    for i in range(len(sentence)):
        if sentence[i] >= 'A' and sentence[i] <= 'Z':
            if sentence[i] not in result:
                result.append(sentence[i])
    return result


def alphabet_plus_string_exists(question, phrase):
    a = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i in a:
        if i + phrase in question:
            return True
    return False

def extract_equation_from(question):
    equation=""
    equation_candidates=[]
    for a in question:
        if a in "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789+-*/=":
            equation+=a
        else:
            equation_candidates.append(equation)
            equation=""
       
    return sorted(equation_candidates, key=len, reverse=True)[0]


def change_text(text, position, letter):
    new = list(text)
    new[position] = letter
    return ''.join(new)


def erase_leading_zeros(text):
    result = ""
    leading = True
    for i in range(len(text)):
        if text[i] in '+-*/':
            leading = True
            result += text[i]
            continue

        if text[i] == '0':
            if leading == True:
                continue
            else:
                result += text[i]
        else:
            leading = False
            result += text[i]
        
    return result

def find_solution(equation):
    comp = True
    for i in range(len(equation)):
        if equation[i] in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            comp = False
            for j in range(0, 10):
                equation = change_text(equation, i, str(j))
                r = find_solution(equation)
                if r != False:
                    return r
                
    if comp == True:
        e = equation.split("=")

        try:
            if eval(e[0]) == eval(e[1]):
                return equation
            else:
                return False
        except:
            return False
    return False

def find_diff_between(text1, text2):
    length = len(text1)
    result = []
    for i in range(length):
        if text1[i] != text2[i]:
            result.append(text2[i])
    return result

def get_most_freq_alphabets(question):
    alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    freq = [0] * 26
    for i in range(len(question)):
        for j in range(len(alphabets)):
            if question[i] == alphabets[j]:
                freq[j]+=1
    return alphabets[freq.index(max(freq))]

def get_alphanumeric_string(question):
    question = question + " "
    alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers = "0123456789"
    result = ""
    alphabet_exists = False
    number_exists = False

    for i in range(len(question)):
        if question[i] in alphabets:
            result += question[i]
            alphabet_exists = True
        elif question[i] in numbers:
            result += question[i]
            number_exists = True
        else:
            if alphabet_exists == True and number_exists == True:
                return result
            else:
                alphabet_exists = False
                number_exists = False
                result = ""
    return False

def replace_alphabet(alphanumeric, i):
    alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for j in range(len(alphanumeric)):
        if alphanumeric[j] in alphabets:
            alphanumeric = change_text(alphanumeric, j, str(i))
    return alphanumeric

def find_four_calc(question):
    plus = ["뺐", "빼고", "뺀", "더해", "더하는"]
    minus = ["더했", "더한", "더하고", "빼야", "빼는"]
    mul = ["나눴", "나누", "나눈", "곱해야", "곱하는"]
    div = ["곱했", "곱하였", "곱한", "곱하고", "곱해서", "나눠야", "나누어야", "나누는"]
    
    calc = ""

    for i in range(len(question)):
        for j in plus:
            length = len(j)
            if question[i:i+length] == j:
                calc+="+"
        for j in minus:
            length = len(j)
            if question[i:i+length] == j:
                calc+="-"
        for j in mul:
            length = len(j)
            if question[i:i+length] == j:
                calc+="*"
        for j in div:
            length = len(j)
            if question[i:i+length] == j:
                calc+="/"

    return calc

def rreplace(text, A, B):
    return B.join(text.rsplit(A, 1))


def extract_names(question):
    delimeter = "은는이가보"
    names = []
    for j in range(len(question)):
        if question[j] in delimeter:
            if j == 2 or (j > 2 and question[j-3] == " "):
                name = question[j-2:j]
                if name != "사람":
                    if name not in names:
                        if len(name.strip()) == 2: 
                            names.append(name)
    return names

def get_min_key(dic, k=1):
    for i in range(k):
        min_key = ""
        min_value = 9999999
        for key in dic:
            if min_value > dic[key]:
                min_value = dic[key]
                min_key = key
        dic[min_key] = 9999999
    return min_key

def get_max_key(dic, k=1):
    for i in range(k):
        max_key = ""
        max_value = -9999999
        for key in dic:
            if max_value < dic[key]:
                max_value = dic[key]
                max_key = key
        dic[max_key] = -9999999
    return max_key

global_question = ""
global_integers = []

def split(postfix1, postfix2):
    question = global_question
    integers = global_integers
    question = " " + question

    first = []
    second = []
    others = []

    if postfix2 == "": postfix2 = "qrhpqhwethqwpoerqwoeriqwjroiwm;zlxkmcv"

    for i in range(len(integers)):
        text1 = " " +str(integers[i]) + postfix1
        text2 = " " +str(integers[i]) + postfix2
        if text1 in question:
            first.append(integers[i])
            question = question.replace(text1, "", 1)
        elif text2 in question:
            second.append(integers[i])
            question = question.replace(text2, "", 1)
        else:
            others.append(integers[i])
    return first, second, others

def two_equations(question):
    c=0
    for i in range(len(question)):
        if question[i] == '=':
            c+=1
    if c==2: return True
    else: return False

def is_combination_of_number_alphabet(question):
    alphabet=False
    number=False

    alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers = "0123456789"

    for i in range(len(question)):
        if question[i] in alphabets:
            alphabet=True
            if number == True: return True
        else:
            alphabet=False

        if question[i] in numbers:
            number=True
            if alphabet == True: return true
        else:
            number=False

def find_index(list_, string_):
    for i in range(len(list_)):
        if list_[i] == string_:
            return i
    return -1

def replace_ABC(equation, A, B, C):
    equation = equation.replace("A", str(A))
    equation = equation.replace("B", str(B))
    equation = equation.replace("C", str(C))
    equation = equation.replace("=", "==")
    return equation

def convert_counters(question):
    counters = ["벌", "분", "단", "채", "개비",
    "그루", "자루", "켤레", "마리", "포기", "푼", "송이", "톨",
    "갑", "과", "권", "대", "량", "명", "장", "척", "통", "필"]
    
    numbers = "0123456789"

    found_int = False
    new_question = ""
    i=0
    while True:
        if i >= len(question): break

        if question[i] in numbers:
            found_int=True
            new_question += question[i]
        else:
            found = False
            for j in range(len(counters)):
                counter = counters[j]
                if found_int == True and question[i:i+len(counter)] == counter:
                    new_question += "개"
                    i+=(len(counter)-1)
                    found=True
            if found == False:
                new_question += question[i]
            
            found_int=False
        i+=1


    return new_question


def solver(question):
    question = " " + question

    # 전처리    
    question = convert_fraction_to_decimal(question)
    question = convert_letters_to_digits(question)
    question = convert_special_characters(question)
    question = convert_numbers_to_digits(question)
    question = convert_counters(question)

    integers, str_integers = extract_integers(question)
    floats, str_floats = extract_floats(question)

    global global_question, global_integers
    global_question = question
    global_integers = integers

    # 기본 값
    answer = "0"
    equation = "0"

    if False:
        pass

    elif "어떤 수" in question and "되었습니다" in question and "얼마" in question:
        questions = question.split("되었습니다")
        floats = extract_floats(questions[0])[0]

        calc = find_four_calc(questions[0])
        calc = calc[::-1]
        floats = floats[::-1]
        
        calc_index=0

        equation = ""
        for i in range(len(calc)+1):
            equation += "("

        for num in floats:
            equation+=str(num) + ")"
            if calc_index < len(calc):
                equation+=calc[calc_index]
                calc_index+=1
            else:
                break
        
        if len(questions) >= 2:
            floats = extract_floats(questions[1])[0]
            if len(floats) == 1:
                if "빼" in questions[1]:
                    equation += ("-" + str(floats[0]))
                if "더" in questions[1]:
                    equation += ("+" + str(floats[0]))
                if "곱" in questions[1]:
                    equation += ("*" + str(floats[0]))
                if "나누" in questions[1] or "나눠" in questions[1] or "나눴" in questions[1]:
                    equation += ("/" + str(floats[0]))                    

        answer, equation = get_answer(question, equation)

    elif two_equations(question) and not is_combination_of_number_alphabet(question) and "A를 구" in question:
        questions = question.split(",")
        equations = []

        for q in questions:
            if "=" in q:
                e = extract_equation_from(q)
                equations.append(e)
        
        for A in range(100):
            for B in range(100):
                for C in range(1):
                    c=0
                    for e in equations:
                        if eval(replace_ABC(e, A, B, C)) == True:
                            c+=1
                    if c == 2:
                        equation = "[%s, %s, %s][0]" % (A, B, C)
        
        answer, equation = get_answer(question, equation)

    elif two_equations(question) and not is_combination_of_number_alphabet(question) and "B를 구" in question:
        questions = question.split(",")
        equations = []

        for q in questions:
            if "=" in q:
                e = extract_equation_from(q)
                equations.append(e)
        
        for A in range(100):
            for B in range(100):
                for C in range(1):
                    c=0
                    for e in equations:
                        if eval(replace_ABC(e, A, B, C)) == True:
                            c+=1
                    if c == 2:
                        equation = "[%s, %s, %s][1]" % (A, B, C)
        
        answer, equation = get_answer(question, equation)

    elif two_equations(question) and not is_combination_of_number_alphabet(question) and "합" in question and "A" in question and "B" in question:
        questions = question.split(",")
        equations = []

        for q in questions:
            if "=" in q:
                e = extract_equation_from(q)
                equations.append(e)
        
        for A in range(100):
            for B in range(100):
                for C in range(1):
                    c=0
                    for e in equations:
                        if eval(replace_ABC(e, A, B, C)) == True:
                            c+=1
                    if c == 2:
                        equation = "[%s, %s, %s][0] + [%s, %s, %s][1]" % (A, B, C, A, B, C)
        
        answer, equation = get_answer(question, equation)

    elif two_equations(question) and not is_combination_of_number_alphabet(question) and "곱" in question and "A" in question and "B" in question:
        questions = question.split(",")
        equations = []

        for q in questions:
            if "=" in q:
                e = extract_equation_from(q)
                equations.append(e)
        
        for A in range(100):
            for B in range(100):
                for C in range(1):
                    c=0
                    for e in equations:
                        if eval(replace_ABC(e, A, B, C)) == True:
                            c+=1
                    if c == 2:
                        equation = "[%s, %s, %s][0] * [%s, %s, %s][1]" % (A, B, C, A, B, C)
        
        answer, equation = get_answer(question, equation)

    elif len(split("자리 수", "")[0]) >= 2 and "뺄" in question and \
            (split("자리 수", "")[0][0] + split("자리 수", "의")[0][1]) <= 6 and \
            "결과" in question:
        
        first, second, others = split("자리 수", "의")
        first_number_length = first[0]
        second_number_length = first[1]
        
        others.sort()

        first_iteration = pow(10, first_number_length)
        second_iteration = pow(10, second_number_length)
        stop=False
        for i in range(first_iteration):
            for j in range(second_iteration):
                if i-j == others[-1]:
                    A=str(i)
                    B=str(j)

                    one_digit = False
                    two_digit = False
                    A_changed = False
                    B_changed = False
                    for k in range(len(others)):
                        if len(str(others[k])) == 1:
                            one_digit = True
                        if len(str(others[k])) == 2:
                            two_digit = True

                    for k in range(len(others)-1):
                        if len(str(others[k])) == 2:
                            if str(others[k]) in A:
                                A_ = A.replace(str(others[k]), str(others[k])[::-1], 1)
                                two_digit = False
                                A_changed = True
                            elif str(others[k]) in B:
                                B_ = B.replace(str(others[k]), str(others[k])[::-1], 1)
                                two_digit = False
                                B_changed = True
                    
                    for k in range(len(others)-1):
                        if len(str(others[k])) == len(str(others[k+1])):
                            if A_changed == False:
                                if str(others[k]) in A:
                                    A_ = A.replace(str(others[k]), str(others[k+1]), 1)
                                    one_digit = False
                                elif str(others[k+1]) in A:
                                    A_ = A.replace(str(others[k+1]), str(others[k]), 1)
                                    one_digit = False
                            if B_changed == False:
                                if str(others[k]) in B:
                                    B_ = B.replace(str(others[k]), str(others[k+1]), 1)
                                    one_digit = False
                                elif str(others[k+1]) in B:
                                    B_ = B.replace(str(others[k+1]), str(others[k]), 1)
                                    one_digit = False   

                    if one_digit == False and two_digit == False:
                        A = A_
                        B = B_
                        stop=True
                        break
            if stop==True: break 
        equation = "%s-%s" % (A, B)
        answer, equation = get_answer(question, equation)
    
    elif len(split("자리 수", "")[0]) >= 2 and "덧" in question and \
            (split("자리 수", "")[0][0] + split("자리 수", "의")[0][1]) <= 6 and \
            "결과" in question:
        
        first, second, others = split("자리 수", "의")
        first_number_length = first[0]
        second_number_length = first[1]
        
        others.sort()

        first_iteration = pow(10, first_number_length)
        second_iteration = pow(10, second_number_length)
        stop=False
        for i in range(first_iteration):
            for j in range(second_iteration):
                if i+j == others[-1]:
                    A=str(i)
                    B=str(j)

                    one_digit = False
                    two_digit = False
                    A_changed = False
                    B_changed = False
                    for k in range(len(others)):
                        if len(str(others[k])) == 1:
                            one_digit = True
                        if len(str(others[k])) == 2:
                            two_digit = True

                    for k in range(len(others)-1):
                        if len(str(others[k])) == 2:
                            if str(others[k]) in A:
                                A_ = A.replace(str(others[k]), str(others[k])[::-1], 1)
                                two_digit = False
                                A_changed = True
                            elif str(others[k]) in B:
                                B_ = B.replace(str(others[k]), str(others[k])[::-1], 1)
                                two_digit = False
                                B_changed = True
                    
                    for k in range(len(others)-1):
                        if len(str(others[k])) == len(str(others[k+1])):
                            if A_changed == False:
                                if str(others[k]) in A:
                                    A_ = A.replace(str(others[k]), str(others[k+1]), 1)
                                    one_digit = False
                                elif str(others[k+1]) in A:
                                    A_ = A.replace(str(others[k+1]), str(others[k]), 1)
                                    one_digit = False
                            if B_changed == False:
                                if str(others[k]) in B:
                                    B_ = B.replace(str(others[k]), str(others[k+1]), 1)
                                    one_digit = False
                                elif str(others[k+1]) in B:
                                    B_ = B.replace(str(others[k+1]), str(others[k]), 1)
                                    one_digit = False   

                    if one_digit == False and two_digit == False:
                        A = A_
                        B = B_
                        stop=True
                        break
            if stop==True: break 
        equation = "%s+%s" % (A, B)
        answer, equation = get_answer(question, equation)
        
    elif len(split("자리 수", "")[0]) >= 2 and "곱" in question and \
            (split("자리 수", "")[0][0] + split("자리 수", "의")[0][1]) <= 6 and \
            "결과" in question:
        
        first, second, others = split("자리 수", "의")
        first_number_length = first[0]
        second_number_length = first[1]
        
        others.sort()

        first_iteration = pow(10, first_number_length)
        second_iteration = pow(10, second_number_length)
        stop=False
        for i in range(first_iteration):
            for j in range(second_iteration):
                if i*j == others[-1]:
                    A=str(i)
                    B=str(j)

                    one_digit = False
                    two_digit = False
                    A_changed = False
                    B_changed = False
                    for k in range(len(others)):
                        if len(str(others[k])) == 1:
                            one_digit = True
                        if len(str(others[k])) == 2:
                            two_digit = True

                    for k in range(len(others)-1):
                        if len(str(others[k])) == 2:
                            if str(others[k]) in A:
                                A_ = A.replace(str(others[k]), str(others[k])[::-1], 1)
                                two_digit = False
                                A_changed = True
                            elif str(others[k]) in B:
                                B_ = B.replace(str(others[k]), str(others[k])[::-1], 1)
                                two_digit = False
                                B_changed = True
                    
                    for k in range(len(others)-1):
                        if len(str(others[k])) == len(str(others[k+1])):
                            if A_changed == False:
                                if str(others[k]) in A:
                                    A_ = A.replace(str(others[k]), str(others[k+1]), 1)
                                    one_digit = False
                                elif str(others[k+1]) in A:
                                    A_ = A.replace(str(others[k+1]), str(others[k]), 1)
                                    one_digit = False
                            if B_changed == False:
                                if str(others[k]) in B:
                                    B_ = B.replace(str(others[k]), str(others[k+1]), 1)
                                    one_digit = False
                                elif str(others[k+1]) in B:
                                    B_ = B.replace(str(others[k+1]), str(others[k]), 1)
                                    one_digit = False   

                    if one_digit == False and two_digit == False:
                        A = A_
                        B = B_
                        stop=True
                        break
            if stop==True: break 
        equation = "%s*%s" % (A, B)
        answer, equation = get_answer(question, equation)

    elif len(split("자리 수", "")[0]) >= 2 and "나눗" in question and \
            (split("자리 수", "")[0][0] + split("자리 수", "의")[0][1]) <= 6 and \
            "결과" in question:
        
        first, second, others = split("자리 수", "의")
        first_number_length = first[0]
        second_number_length = first[1]
        
        others.sort()

        first_iteration = pow(10, first_number_length)
        second_iteration = pow(10, second_number_length)
        stop=False
        for i in range(first_iteration):
            for j in range(second_iteration):
                if i/j == others[-1]:
                    A=str(i)
                    B=str(j)

                    one_digit = False
                    two_digit = False
                    A_changed = False
                    B_changed = False
                    for k in range(len(others)):
                        if len(str(others[k])) == 1:
                            one_digit = True
                        if len(str(others[k])) == 2:
                            two_digit = True

                    for k in range(len(others)-1):
                        if len(str(others[k])) == 2:
                            if str(others[k]) in A:
                                A_ = A.replace(str(others[k]), str(others[k])[::-1], 1)
                                two_digit = False
                                A_changed = True
                            elif str(others[k]) in B:
                                B_ = B.replace(str(others[k]), str(others[k])[::-1], 1)
                                two_digit = False
                                B_changed = True
                    
                    for k in range(len(others)-1):
                        if len(str(others[k])) == len(str(others[k+1])):
                            if A_changed == False:
                                if str(others[k]) in A:
                                    A_ = A.replace(str(others[k]), str(others[k+1]), 1)
                                    one_digit = False
                                elif str(others[k+1]) in A:
                                    A_ = A.replace(str(others[k+1]), str(others[k]), 1)
                                    one_digit = False
                            if B_changed == False:
                                if str(others[k]) in B:
                                    B_ = B.replace(str(others[k]), str(others[k+1]), 1)
                                    one_digit = False
                                elif str(others[k+1]) in B:
                                    B_ = B.replace(str(others[k+1]), str(others[k]), 1)
                                    one_digit = False   

                    if one_digit == False and two_digit == False:
                        A = A_
                        B = B_
                        stop=True
                        break
            if stop==True: break 
        equation = "%s/%s" % (A, B)
        answer, equation = get_answer(question, equation)
               
    elif "더" in question and "모두 몇" in question:
        answer = str(sum(integers))
        equation = "+".join(str_integers)

    elif "남았" in question and "처음" in question:
        answer = str(sum(integers))
        equation = "+".join(str_integers)

    elif "더 적다" in question and len(integers) == 2:
        if integers[0] < integers[1]:
            s, l = integers[0], integers[1]
        else:
            s, l = integers[1], integers[0]
        answer = str(l - s)
        equation = str(l) + "-" + str(s)

    elif len(split_lists(question, integers, "개", "")[0]) >= 4 and \
        "똑같" in question and (("나누" in question) or ("나눈" in question)):
        first, second, others = split_lists(question, integers, "개", "")
        equation = "int((" + str(first[1]) + "*" + str(first[2]) + "+" + str(first[3]) + ")/" + str(first[0]) + ")"
        answer = str(int(eval(equation)))

    elif "전체의" in question:
        answer = str(int(math.prod(floats)))
        equation = "*".join(str_floats)
        equation = "int(" + equation + ")"

    elif len(question.split(',')) >= 4 and len(integers) == 1 and len(question.split(',')[1]) == len(question.split(',')[2]):
        tokens = question.split(',')
        for i in range(len(tokens)):
            tokens[i] = tokens[i].strip()
        num_letters = len(tokens[1])
        names = []
        names.append(tokens[0][-num_letters:])
        for i in range(1, len(tokens)-1):
            names.append(tokens[i])
        names.append(tokens[len(tokens)-1][:num_letters])
        answer = names[integers[0]-1]
        equation = str(names) + "[" + str(integers[0]-1) + "]"

    elif "등" in question and "잘했" in question and "못했" in question and len(integers) == 2:
        integers.sort()
        answer = str(integers[1]-1)
        equation = str(integers[1]) + "-1"

    elif "사이에" in question and \
            len(split_lists(question, integers, "번째", "개")[0]) == 1 and \
            len(split_lists(question, integers, "번째", "개")[1]) == 1:
        first, second, others = split_lists(question, integers, "번째", "개")
        equation = str(first[0]) + "+" + str(second[0]) + "+1"
        answer = str(int(eval(equation)))

    elif "왼쪽" in question and "오른쪽" in question and "앞" in question and "뒤" in question and len(integers) == 4:
        answer = str((integers[0]+integers[1]-1)*(integers[2]+integers[3]-1))
        equation = "(%s+%s-1)*(%s+%s-1)" % (str(integers[0]), str(integers[1]), str(integers[2]), str(integers[3])) 

    elif "서로 다른" in question and "합이" in question and "경우" in question and \
            len(split_lists(question, integers, "보다 작은", "수")[0]) >= 1 and \
            len(split_lists(question, integers, "보다 작은", "수")[1]) >= 1 and \
            len(split_lists(question, integers, "보다 작은", "수")[2]) >= 1 and \
            split_lists(question, integers, "보다 작은", "수")[1][0] >= 2 and \
            split_lists(question, integers, "보다 작은", "수")[1][0] <= 5 and \
            split_lists(question, integers, "보다 작은", "수")[0][0] <= 100:
        first, second, others = split_lists(question, integers, "보다 작은", "수")
        max_ = first[0]
        numbers = second[0]
        sum_ = others[0]
        
        equation = ""
        if numbers == 2:
            for i in range(1, max_):
                count = 0
                for j in range(i+1, max_):
                    if i+j == sum_:
                        count+=1

                if i != 1: equation += "+"
                equation += str(count)
        if numbers == 3:
            for i in range(1, max_):
                count = 0
                for j in range(i+1, max_):
                    for k in range(j+1, max_):
                        if i+j+k == sum_:
                            count+=1

                if i != 1: equation += "+"
                equation += str(count)
        if numbers == 4:
            for i in range(1, max_):
                count = 0
                for j in range(i+1, max_):
                    for k in range(j+1, max_):
                        for l in range(k+1, max_):
                            if i+j+k+l == sum_:
                                count+=1

                if i != 1: equation += "+"
                equation += str(count)                
        if numbers == 5:
            for i in range(1, max_):
                count = 0
                for j in range(i+1, max_):
                    for k in range(j+1, max_):
                        for l in range(k+1, max_):
                            for m in range(l+1, max_):
                                if i+j+k+l+m == sum_:
                                    count+=1

                if i != 1: equation += "+"
                equation += str(count)  
        
        answer, equation = get_answer(question, equation)

    elif "서로 다른" in question and "곱이" in question and "경우" in question and \
            len(split_lists(question, integers, "보다 작은", "수")[0]) >= 1 and \
            len(split_lists(question, integers, "보다 작은", "수")[1]) >= 1 and \
            len(split_lists(question, integers, "보다 작은", "수")[2]) >= 1 and \
            split_lists(question, integers, "보다 작은", "수")[1][0] >= 2 and \
            split_lists(question, integers, "보다 작은", "수")[1][0] <= 5 and \
            split_lists(question, integers, "보다 작은", "수")[0][0] <= 100:
        first, second, others = split_lists(question, integers, "보다 작은", "수")
        max_ = first[0]
        numbers = second[0]
        sum_ = others[0]
        
        equation = ""
        if numbers == 2:
            for i in range(1, max_):
                count = 0
                for j in range(i+1, max_):
                    if i*j == sum_:
                        count+=1

                if i != 1: equation += "+"
                equation += str(count)
        if numbers == 3:
            for i in range(1, max_):
                count = 0
                for j in range(i+1, max_):
                    for k in range(j+1, max_):
                        if i*j*k == sum_:
                            count+=1

                if i != 1: equation += "+"
                equation += str(count)
        if numbers == 4:
            for i in range(1, max_):
                count = 0
                for j in range(i+1, max_):
                    for k in range(j+1, max_):
                        for l in range(k+1, max_):
                            if i*j*k*l == sum_:
                                count+=1

                if i != 1: equation += "+"
                equation += str(count)                
        if numbers == 5:
            for i in range(1, max_):
                count = 0
                for j in range(i+1, max_):
                    for k in range(j+1, max_):
                        for l in range(k+1, max_):
                            for m in range(l+1, max_):
                                if i*j*k*l*m == sum_:
                                    count+=1

                if i != 1: equation += "+"
                equation += str(count)  
        answer, equation = get_answer(question, equation)

    elif "뽑아" in question and "작은" in question and "큰" not in question and \
            len(split_lists(question, integers, "개", "자리")[0]) >= 1 and \
            len(split_lists(question, integers, "개", "자리")[1]) >= 1:
        digits = split_lists(question, integers, "개", "자리")[0][0]
        others = split_lists(question, integers, "개", "자리")[2]

        others.sort()
        if len(others) >= 2:
            if others[0] == 0:
                others[0], others[1] = others[1], others[0]
        equation = ""
        for i in range(digits):
            if i != 0: equation += "+"
            equation += "str(" + str(others[i]) + ")"
        answer, equation = get_answer(question, equation)

    elif "뽑아" in question and "큰" in question and "작은" not in question and \
            len(split_lists(question, integers, "개", "자리")[0]) >= 1 and \
            len(split_lists(question, integers, "개", "자리")[1]) >= 1:
        digits = split_lists(question, integers, "개", "자리")[0][0]
        others = split_lists(question, integers, "개", "자리")[2]

        others.sort(reverse=True)
        if len(others) >= 2:
            if others[0] == 0:
                others[0], others[1] = others[1], others[0]
        equation = ""
        for i in range(digits):
            if i != 0: equation += "+"
            equation += "str(" + str(others[i]) + ")"
        answer, equation = get_answer(question, equation)

    elif "뽑아" in question and "큰" in question and "작은" not in question and len(numbers_counter) == 1 and len(numbers_not_counter) >= 2:
        numbers_not_counter.sort()
        index = len(numbers_not_counter)-1
        answer = ""
        equation = ""
        for i in range(numbers_counter[0]):
            answer += str(numbers_not_counter[index])
            if index != len(numbers_not_counter)-1:
                equation += "+"
            equation += "str(%s)" % (numbers_not_counter[index])
            index-=1
    
    elif "뽑아" in question and "작은" in question and "큰" not in question and len(numbers_counter) == 1 and len(numbers_not_counter) >= 2:
        numbers_not_counter.sort(reverse=True)
        index = len(numbers_not_counter)-1
        answer = ""
        equation = ""
        for i in range(numbers_counter[0]):
            answer += str(numbers_not_counter[index])
            if index != len(numbers_not_counter)-1:
                equation += "+"
            equation += "str(%s)" % (numbers_not_counter[index])
            index-=1
    
    elif "뽑아" in question and "작은" in question and "큰" in question and \
        len(split_lists(question, integers, "자리", "개")) >= 1:

        first, second, others = split_lists(question, integers, "자리", "개")
        ndigits = first[0]

        others.sort()
        index = len(others)-1
        answer1 = ""
        for i in range(ndigits):
            answer1 += str(others[index])
            index-=1

        others.sort(reverse=True)
        index = len(others)-1
        answer2 = ""
        for i in range(ndigits):
            answer2 += str(others[index])
            index-=1

        answer = str(int(answer1) - int(answer2))
        equation = "str(int(%s) - int(%s))" % (answer1, answer2)
    
    elif "가장 큰" in question and "가장 작은" in question and ("뺀" in question or "빼" in question or "뺐" in question):
        equation = "%s-%s" % (str(max(floats)), str(min(floats)))
        answer, equation = get_answer(question, equation)

    elif "가장 큰" in question and "가장 작은" in question and "더" in question:
        equation = "%s+%s" % (str(max(floats)), str(min(floats)))
        answer, equation = get_answer(question, equation)

    elif "가장 큰" in question and "가장 작은" in question and "곱" in question and \
            len(split("개", "")[0]) == 0:
        equation = "%s*%s" % (str(max(floats)), str(min(floats)))
        answer, equation = get_answer(question, equation)

    elif "가장 큰" in question and "가장 작은" in question and ("나눈" in question or "나누" in question):
        equation = "%s/%s" % (str(max(floats)), str(min(floats)))
        answer, equation = get_answer(question, equation)

    elif "보다" in question and "큰" in question and "모두" in question and "같" not in question and \
            len(split_lists(question, integers, "개", "보다")[0]) >= 1 and \
            (len(split_lists(question, integers, "개", "보다")[1]) >= 1 or \
            len(split_lists(question, floats, "개", "보다")[1]) >= 1) and \
            len(split_lists(question, floats, "개", "보다")[2]) >= 1:

        a, b, c = split_lists(question, integers, "개", "보다")
        a_, b_, c_ = split_lists(question, floats, "개", "보다")
        
        first = a
        if len(b) >= 1:
            second = b
        else:
            second = b_
        others = c_

        for i in range(len(first)):
            others.remove(float(first[i]))
        for i in range(len(second)):
            others.remove(float(second[i]))

        threshold = second[0]
        equation = "0"
        for i in range(len(others)):
            if others[i] > threshold:
                equation += "+1"
        answer, equation = get_answer(question, equation)

    elif "보다" in question and ("큰" in question or "크" in question) and "같" in question and "모두" in question and \
            len(split_lists(question, integers, "개", "보다")[0]) >= 1 and \
            (len(split_lists(question, integers, "개", "보다")[1]) >= 1 or \
            len(split_lists(question, floats, "개", "보다")[1]) >= 1) and \
            len(split_lists(question, floats, "개", "보다")[2]) >= 1:

        a, b, c = split_lists(question, integers, "개", "보다")
        a_, b_, c_ = split_lists(question, floats, "개", "보다")
        
        first = a
        if len(b) >= 1:
            second = b
        else:
            second = b_
        others = c_

        for i in range(len(first)):
            others.remove(float(first[i]))
        for i in range(len(second)):
            others.remove(float(second[i]))

        threshold = second[0]
        equation = "0"
        for i in range(len(others)):
            if others[i] >= threshold:
                equation += "+1"
        answer, equation = get_answer(question, equation)

    elif "보다" in question and "작" in question and "모두" in question and "같" not in question and \
            len(split_lists(question, integers, "개", "보다")[0]) >= 1 and \
            (len(split_lists(question, integers, "개", "보다")[1]) >= 1 or \
            len(split_lists(question, floats, "개", "보다")[1]) >= 1) and \
            len(split_lists(question, floats, "개", "보다")[2]) >= 1:

        a, b, c = split_lists(question, integers, "개", "보다")
        a_, b_, c_ = split_lists(question, floats, "개", "보다")
        
        first = a
        if len(b) >= 1:
            second = b
        else:
            second = b_
        others = c_

        for i in range(len(first)):
            others.remove(float(first[i]))
        for i in range(len(second)):
            others.remove(float(second[i]))

        threshold = second[0]
        equation = "0"
        for i in range(len(others)):
            if others[i] < threshold:
                equation += "+1"
        answer, equation = get_answer(question, equation)

    elif "보다" in question and "작" in question and "같" in question and "모두" in question and \
            len(split_lists(question, integers, "개", "보다")[0]) >= 1 and \
            (len(split_lists(question, integers, "개", "보다")[1]) >= 1 or \
            len(split_lists(question, floats, "개", "보다")[1]) >= 1) and \
            len(split_lists(question, floats, "개", "보다")[2]) >= 1:

        a, b, c = split_lists(question, integers, "개", "보다")
        a_, b_, c_ = split_lists(question, floats, "개", "보다")
        
        first = a
        if len(b) >= 1:
            second = b
        else:
            second = b_
        others = c_

        for i in range(len(first)):
            others.remove(float(first[i]))
        for i in range(len(second)):
            others.remove(float(second[i]))

        threshold = second[0]
        equation = "0"
        for i in range(len(others)):
            if others[i] <= threshold:
                equation += "+1"
        answer, equation = get_answer(question, equation)

    elif len(split_lists(question, integers, "쪽", "")[0]) >= 1 and \
            len(split_lists(question, integers, "쪽", "")[2]) >= 1 and \
            "합" in question and "큰" in question:
        first, second, others = split_lists(question, integers, "쪽", "")
        equation = "(%s+1)/2" % (int(others[0]))
        answer, equation = get_answer(question, equation)
    
    elif len(split_lists(question, integers, "쪽", "")[0]) >= 1 and \
            len(split_lists(question, integers, "쪽", "")[2]) >= 1 and \
            "합" in question and "작은" in question:
        first, second, others = split_lists(question, integers, "쪽", "")
        equation = "(%s+1)/2-1" % (int(others[0]))
        answer, equation = get_answer(question, equation)
            
    elif len(split_lists(question, integers, "자리", "만큼")[0]) >= 1 and \
            len(split_lists(question, floats, "자리", "만큼")[1]) >= 1 and \
            "왼쪽" in question:
        num_moves = split_lists(question, integers, "자리", "만큼")[0][0]
        difference = split_lists(question, floats, "자리", "만큼")[1][0]

        equation = "(" + str(difference) + "*" + str(pow(10, num_moves)) + ") / (" + str(pow(10, num_moves)) + "-1)"
        answer, equation = get_answer(question, equation)

    elif len(split_lists(question, integers, "자리", "만큼")[0]) >= 1 and \
            len(split_lists(question, floats, "자리", "만큼")[1]) >= 1 and \
            "오른쪽" in question:
        num_moves = split_lists(question, integers, "자리", "만큼")[0][0]
        difference = split_lists(question, floats, "자리", "만큼")[1][0]

        equation = "-(" + str(difference) + "*" + str(pow(10, -num_moves)) + ") / (" + str(pow(10, -num_moves)) + "-1)"
        answer, equation = get_answer(question, equation)

    elif len(extract_alphabets(question)) >= 2 and len(integers) >= 2 and \
            len(split_lists(question, integers, "자리", "")[0]) >= 1 and "보다" in question and ("큰" in question or "작은" in question):
        equation = "0"
        integers = split_lists(question, integers, "자리", "")[2]

        for i in range(len(integers)):
            equation += "+" + str(integers[i])
        answer, equation = get_answer(question, equation)

    elif "=" in question and len(extract_alphabets(question)) >= 1 and "합" in question:
        e = extract_equation_from(question)
        diff = find_diff_between(e, find_solution(e))
        equation = "0"
        for i in range(len(diff)):
            equation += '+' + diff[i]
        answer, equation = get_answer(question, equation)

    elif "=" in question and len(extract_alphabets(question)) >= 1 and "차" in question:
        e = extract_equation_from(question)
        diff = find_diff_between(e, find_solution(e))
        equation = "0"
        for i in range(len(diff)):
            if i == 0:
                equation += '+' + diff[i]
            else:
                equation += '-' + diff[i]
        answer, equation = get_answer(question, equation)

    elif "=" in question and len(extract_alphabets(question)) >= 1 and "합" not in question and "차" not in question:
        e = extract_equation_from(question)
        diff1 = find_diff_between(e, find_solution(e))
        diff2 = find_diff_between(find_solution(e), e)
        
        max_freq_alphabet = get_most_freq_alphabets(question)

        for i in range(len(diff2)):
            if diff2[i] == max_freq_alphabet:
                equation = str(diff1) + "[" + str(i) + "]"
                answer, equation = get_answer(question, equation)
                break

    elif len(split_lists(question, integers, "로 나누면", "이")[0]) == 1 and \
            len(split_lists(question, integers, "로 나누면", "이")[1]) == 1 and \
            "가장 큰 수" in question:
        first, second, others = split_lists(question, integers, "로 나누면", "이")
        equation = "%s*%s+%s" % (str(first[0]), str(second[0]), str(first[0]-1))
        answer, equation = get_answer(question, equation)

    elif "의 자리에서" in question and "부터" in question and "까지" in question and "모두" in question and "반올림" in question and \
            len(split_lists(question, integers, "의 자리에서", "")[0]) >= 1 and \
            len(split_lists(question, integers, "이", "")[0]) >= 1 and \
            len(split_lists(question, integers, "부터", "까지")[0]) >= 1 and \
            len(split_lists(question, integers, "부터", "까지")[1]) >= 1:   
        round_number = split_lists(question, integers, "의 자리에서", "")[0][0]
        result_number = split_lists(question, integers, "이", "")[0][0]
        from_number = split_lists(question, integers, "부터", "까지")[0][0]
        to_number = split_lists(question, integers, "부터", "까지")[1][0]
        alphanumeric = get_alphanumeric_string(question)

        pos_converter = {1: -1, 10: -2, 100: -3, 1000: -4, 10000: -5, 100000: -6, 1000000: -7}

        equation = "0"

        for i in range(from_number, to_number+1):
            a = replace_alphabet(alphanumeric, i)      
            if round(eval(a), pos_converter[round_number]) == result_number:
                equation += "+1"
        
        answer, equation = get_answer(question, equation)
        
    elif "어떤 수" in question:
        calc = find_four_calc(question)
        calc = calc[::-1]
        floats = floats[::-1]
        
        calc_index=0

        equation = ""
        for i in range(len(calc)+1):
            equation += "("

        for num in floats:
            equation+=str(num) + ")"
            if calc_index < len(calc):
                equation+=calc[calc_index]
                calc_index+=1
            else:
                break
        answer, equation = get_answer(question, equation)

    elif "작은" in question and "곱셈" in question and \
            len(split_lists(question, integers, "일 때", "")[0]) == 1 and \
            split_lists(question, integers, "자리", "")[0][0] == 2 and \
            len(split_lists(question, integers, "의 자리", "")[0]) >= 1 and \
            (len(split_lists(question, integers, "을", "를")[0]) == 1 or
            len(split_lists(question, integers, "을", "를")[1]) == 1):

        pos = split_lists(question, integers, "의 자리", "")[0][0]
        if pos == 10: pos = 0
        elif pos == 1: pos = 1

        equation=""
        result = split_lists(question, integers, "일 때", "")[0][0]
        correct_number=split_lists(question, integers, "을", "를")
        if len(correct_number[0]) == 1:
            correct_number = correct_number[0][0]
        else:
            correct_number = correct_number[1][0] 

        for a in range(10, 100):
            for b in range(10, 100):
                if a*b == result:
                    if str(correct_number) == str(a)[pos] or str(correct_number) == str(b)[pos]:
                        equation = "int(%s/%s)" % (result, b)
                        break
            if equation != "": break

        answer, equation = get_answer(question, equation)

    elif "큰" in question and "곱셈" in question and \
            len(split_lists(question, integers, "일 때", "")[0]) == 1 and \
            split_lists(question, integers, "자리", "")[0][0] == 2 and \
            len(split_lists(question, integers, "의 자리", "")[0]) >= 1 and \
            (len(split_lists(question, integers, "을", "를")[0]) == 1 or
            len(split_lists(question, integers, "을", "를")[1]) == 1):

        pos = split_lists(question, integers, "의 자리", "")[0][0]
        if pos == 10: pos = 0
        elif pos == 1: pos = 1

        equation=""
        result = split_lists(question, integers, "일 때", "")[0][0]
        correct_number=split_lists(question, integers, "을", "를")
        if len(correct_number[0]) == 1:
            correct_number = correct_number[0][0]
        else:
            correct_number = correct_number[1][0] 

        for a in range(10, 100):
            for b in range(10, 100):
                if a*b == result:
                    if str(correct_number) == str(a)[pos] or str(correct_number) == str(b)[pos]:
                        equation = "int(%s/%s)" % (result, a)
                        break
            if equation != "": break

        answer, equation = get_answer(question, equation)

    elif "작은" in question and "덧셈" in question and \
            len(split_lists(question, integers, "일 때", "")[0]) == 1 and \
            split_lists(question, integers, "자리", "")[0][0] == 2 and \
            len(split_lists(question, integers, "의 자리", "")[0]) >= 1 and \
            (len(split_lists(question, integers, "을", "를")[0]) == 1 or
            len(split_lists(question, integers, "을", "를")[1]) == 1):

        pos = split_lists(question, integers, "의 자리", "")[0][0]
        if pos == 10: pos = 0
        elif pos == 1: pos = 1

        equation=""
        result = split_lists(question, integers, "일 때", "")[0][0]
        correct_number=split_lists(question, integers, "을", "를")
        if len(correct_number[0]) == 1:
            correct_number = correct_number[0][0]
        else:
            correct_number = correct_number[1][0] 

        for a in range(10, 100):
            for b in range(10, 100):
                if a+b == result:
                    if str(correct_number) == str(a)[pos] or str(correct_number) == str(b)[pos]:
                        equation = "int(%s-%s)" % (result, b)
                        break
            if equation != "": break

        answer, equation = get_answer(question, equation)

    elif "큰" in question and "덧셈" in question and \
            len(split_lists(question, integers, "일 때", "")[0]) == 1 and \
            split_lists(question, integers, "자리", "")[0][0] == 2 and \
            len(split_lists(question, integers, "의 자리", "")[0]) >= 1 and \
            (len(split_lists(question, integers, "을", "를")[0]) == 1 or
            len(split_lists(question, integers, "을", "를")[1]) == 1):

        pos = split_lists(question, integers, "의 자리", "")[0][0]
        if pos == 10: pos = 0
        elif pos == 1: pos = 1

        equation=""
        result = split_lists(question, integers, "일 때", "")[0][0]
        correct_number=split_lists(question, integers, "을", "를")
        if len(correct_number[0]) == 1:
            correct_number = correct_number[0][0]
        else:
            correct_number = correct_number[1][0] 

        for a in range(10, 100):
            for b in range(10, 100):
                if a+b == result:
                    if str(correct_number) == str(a)[pos] or str(correct_number) == str(b)[pos]:
                        equation = "int(%s-%s)" % (result, a)
                        break
            if equation != "": break

        answer, equation = get_answer(question, equation)

    return answer, equation