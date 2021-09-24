import time
import csv
import random
import winsound

name = input("What is your name?")

print("Hi," + name + "! play enjoy!")

print()

time.sleep(1)

print("Start Loading...")
print()
time.sleep(0.5)

# CSV 단어 리스트 선언
words = []

# CSV 파일 로드
with open('./word_list.csv', 'r') as f:
    reader = csv.reader(f)
    # 헤더 스킵
    next(reader)
    for c in reader :
        words.append(c)

# 리스트 섞기
random.shuffle(words)

q = random.choice(words)

# 정답 단어 선언 및 공백제거
word = q[0].strip()

# 입력 단어
guesses = ''

# 정답 기회
turns = 10

# 찬스 카운트가 남아 있을 경우
while turns > 0:
    # 실패 횟수
    failed = 0

    print()

    # 정답 단어 반복
    for char in word:
        # 정답 단어 내에 추측 단어가 포함되어 있는 경우
        if char in guesses:
            # 추측 단어 출력
            print(char, end=' ')

        else:
            # 틀린 경우 대시로 처리
            print("_", end=' ')
            # 실패 횟수 증가
            failed += 1

    # 단어 추측이 성공한 경우
    if failed == 0:
        print()
        print()
        # 사운드 재생
        winsound.PlaySound('./sound/good.wav', winsound.SND_FILENAME)
        print("Congratulations! The word is" , word)
        # while 구문 중단
        break

    print()

    # 추측 단어 글자 단위 입력
    print()
    print('Hint : {}'.format(q[1].strip()))
    guess = input("guess a character : ")

    # 한글자씩만 입력 가능하게
    while len(guess) != 1 :
        print("Please type just one character!")
        print()
        guess = input("guess a character : ")

    # 단어 더하기
    guesses += guess

    # 정답 단어에 추측한 문자가 포함되어 있지 않으면
    if guess not in word:
        # 기회 횟수 감소
        turns -= 1
        # 오류 메시지
        print()
        print("Oops! Wrong.. You have", turns, "more chances!")
        print()
        print("_______________________________________")

        # 기회를 모두 사용하면
        if turns == 0:
            # 실패 메시지
            print()
            # 사운드 재생
            winsound.PlaySound('./sound/bad.wav', winsound.SND_FILENAME)
            print("Game Failed. Bye!")
