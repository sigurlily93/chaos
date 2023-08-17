# this tool gives recommended downtilt angel based on antenna heights and distance
#输入BS和UE的天线高度、主覆盖点到BS距离，输出推荐的BS天线下倾角

import math
def para_input():
    bs_height = float(input("please input base station height(m): "))
    ue_height = float(input("please input user equipment height(m):"))
    distance = float(input("please input distance between BS and UE(m):"))
    return bs_height,ue_height,distance

def antenna_downtilt(bs_height,ue_height,distance):
    delt_h = bs_height-ue_height
    downtilt= math.degrees(math.atan(delt_h/distance))
    return downtilt

if __name__ == '__main__':
    bs_height,ue_height,distance = para_input()
    downtilt = antenna_downtilt(bs_height,ue_height,distance)
    print("the recommended downtilt angle is:",downtilt,"degrees")
