hour, minute = map(int, input().split())  # 시작 시간 정보 입력받기
time = int(input())  # 소요 시간 입력받기

if (minute + time) < 60:  # 분 정보가 0~59 사이가 되도록 만들어줌
  end_minute = minute + time
  end_hour = hour
else:
  end_minute = (minute + time) % 60
  if hour + (minute + time) // 60 < 24:  # 시간 정보가 0~23 사이가 되도록 만들어줌
    end_hour = hour + (minute + time) // 60
  else:
    end_hour = (hour + (minute + time) // 60) % 24

print(end_hour, end_minute)  # 종료 시간 출력