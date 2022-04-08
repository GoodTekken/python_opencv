# This is a sample Python script.
# https://www.kancloud.cn/aollo/aolloopencv/259610
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import sys
import cv2

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    print(sys.argv[0])
    img = cv2.imread('.\Image\Luffy.jpg', 1)
    cv2.namedWindow('Image', cv2.WINDOW_NORMAL)
    cv2.imshow('Image', img)
    # cv2.imwrite('./Image/myluffy.png', img)
    k = cv2.waitKey(0)
    # cv2.destroyAllWindows()
    if k==27:
        cv2.destroyAllWindows()  #wait for ESC key to exit
    elif k == ord('s'):
        cv2.destroyAllWindows()


    # 读取视频文件
    cap = cv2.VideoCapture('./Video/vtest.avi')
    while (True):
        # capture frame-by-frame
        ret, frame = cap.read()

        # our operation on the frame come here
        # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # cv2.imshow('frame', gray)

        color =  cv2.cvtColor(frame, cv2.COLOR_BGR2BGRA)
        # display the resulting frame
        cv2.imshow('frame', color)


        if cv2.waitKey(1) & 0xFF == ord('q'):  # 按q键退出
            break
    # when everything done , release the capture
    cap.release()
    cv2.destroyAllWindows()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
