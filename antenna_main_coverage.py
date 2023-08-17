# this tool calculates main coverage area based on antenna heights,downtilt and vertical main lobe beamwidth
# recommended value of main lobe beamwidth is 30~35 degrees
#输入BS和UE的天线高度、BS天线下倾角和垂直主瓣宽度，输出主覆盖区域内外半径

import math
def para_input():
    bs_height = float(input("please input base station height(m):"))
    ue_height = float(input("please input user equipment height(m):"))
    downtilt = float(input("please input antenna downtilt(degree):"))
    beamwidth=float(input("please input vertical main lobe beamwidth(degree):"))
    return bs_height,ue_height,downtilt,beamwidth

def main_coverage(bs_height,ue_height,downtilt,beamwidth):
    delt_h = bs_height-ue_height
    inner_r = delt_h/math.tan(math.radians(downtilt+beamwidth/2))
    if downtilt-beamwidth/2 >0:
        outer_r = delt_h/math.tan(math.radians(downtilt-beamwidth/2))
    else:
        outer_r = "infinity"
    return inner_r,outer_r

if __name__ == '__main__':
    bs_height,ue_height,downtilt,beamwidth = para_input()
    inner_r,outer_r = main_coverage(bs_height,ue_height,downtilt,beamwidth)
    print("the inner radius of main coverage area is:", inner_r,"(m)")
    print("the outer radius of main coverage area is:",outer_r,"(m)")


