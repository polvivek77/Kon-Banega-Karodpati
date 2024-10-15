questions=[['What is the capital of Maharashtra?', 'a. mumbai', 'b. pune', 'c. nashik', 'd. buldana', 'a', 1000],
           ['What is the capital of Gujarat?', 'a. mumbai', 'b. Gandhinagar', 'c. nashik', 'd. buldana', 'b', 2000],
           ['What is the capital of Karnataka?', 'a. mumbai', 'b. pune', 'c. Bengaluru', 'd. buldana', 'c', 3000],
           ['What is the capital of Kerala?', 'a. mumbai', 'b. pune', 'c. nashik', 'd. Thiruvananthapuram', 'd', 5000],
           ['What is the capital of Goa?', 'a. mumbai', 'b. Panaji', 'c. nashik', 'd. buldana', 'b', 10000],
           ['What is the capital of Rajastan?', 'a. Jaipur', 'b. pune', 'c. nashik', 'd. buldana', 'a', 20000],
           ['What is the capital of Jharkhand?', 'a. mumbai', 'b. pune', 'c. Ranchi', 'd. buldana', 'c', 40000],
           ['What is the capital of Uttarpradesh?', 'a. mumbai', 'b. pune', 'c. nashik', 'd. Lucknow', 'd', 80000],
           ['What is the capital of Madhyapradesh?', 'a. Bhopal', 'b. pune', 'c. nashik', 'd. buldana', 'a', 160000],
           ['What is the capital of Andhrapradesh?', 'a. mumbai', 'b. Amaravati', 'c. nashik', 'd. buldana', 'b', 320000],
           ['What is the capital of Tamilnadu?', 'a. mumbai', 'b. pune', 'c. Chennai', 'd. buldana', 'c', 640000],
           ['What is the capital of Bihar?', 'a. mumbai', 'b. pune', 'c. nashik', 'd. Patna', 'd', 1250000],
           ['What is the capital of Uttarakhand?', 'a. Dehradun', 'b. pune', 'c. nashik', 'd. buldana', 'a', 2500000],
           ['What is the capital of Manipur?', 'a. mumbai', 'b. pune', 'c. nashik', 'd. Imphal', 'd', 5000000],
           ['What is the capital of Mizoram?', 'a. mumbai', 'b. pune', 'c. Aizawl', 'd. buldana', 'c', 10000000],
           ['What is the capital of Odisa?', 'a. mumbai', 'b. Bhubaneshwar', 'c. nashik', 'd. buldana', 'b', 70000000]]
print('Welcome to KON BANEGA KARODPATI')
for i in range(0, len(questions)):
    question=questions[i][0]
    print(f'\n $$$$$ Question for Rs.{questions[i][-1]} $$$$$')
    print(f'{i+1}. {question}')
    print(f'\n{questions[i][1]}          {questions[i][2]}')
    print(f'{questions[i][3]}          {questions[i][4]}')
    reply=input('\nEnter your answer: ')
    if reply==questions[i][-2]:
        print(f'sahi javab, aap jit gaye ho Rs.{questions[i][-1]}')
        print('-'*90)
    else:
        print('galat javab')
        print(f'dhanyavad, aap jit chuke hai Rs.{questions[i-1][-1]}')
        break