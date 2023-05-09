from MotorDriver import Motor
import GetCurve as gc
import Curve
import RPi.GPIO as GPIO

########################################
motor = Motor(2, 3, 4, 22, 17, 27)
########################################

# 초기값설정
old_line = [0,0,0]

def main():
    # 커브값을 배열로 저장
    val = gc.LineTracking()
    line = gc.LineWrite(val)
    print(val)
    if line != [0, 0, 0]:
        old_line = gc.LineSave(line) # 값이 비정상적일때를 대비해서 이전의 값을 저장해줌
    # 라인의 값이 비정상적인 경우
    elif line == [0, 0, 0]:
        line = old_line # 비정상적인경우 이전의 값을 불러옴
    else:
        pass

    if val == [0,1,0]: # 가운데 감지일 경우 직진
        motor.move(0.2,0,0)
    elif val == [1,0,0]: # 왼쪽 감지일 경우 왼쪽으로 회전
        motor.move(0.2,-0.2,0)
    elif val == [0,0,1]: # 오른쪽 감지일 경우 오른쪽으로 회전
        motor.move(0.2,0.2,0)
    elif val == [1,1,0]: # 왼쪽과 가운데를 감지했을 경우
        motor.turn(0.2,1,2) # 반시계 방향으로 회전
    elif val == [0,1,1]: # 가운데와 오른쪽이 감지됐을 경우
        motor.turn(0.2,0,2) # 시계 방향으로 회전
    elif val == [1,1,1]:
        motor.turn(0.2,1,2)


if __name__ == '__main__':
    while True:
        main()

motor.stop()
GPIO.cleanup()




