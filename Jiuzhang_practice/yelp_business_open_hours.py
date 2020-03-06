class Open_range:
    def __init__(self, start, end):
        self.start = start
        self.end = end


def business_open_ratio(open_hours,qs,qe):
    # 大概分四个类型讨论
    if open_hours ==[]:
        return 0.0
    total_overlap = 0
    total_range = qe-qs
    for hours in open_hours:
        start = hours.start
        end = hours.end
        if qs<start and qe > start and qe<=end: # query 开始在外边， 结束在两个之间 包含在 end 的边界
            total_overlap += qe-start
        elif qs>= start and qs<end and qe>end: # query 结束在外边， 开始在两个之间， 包含在start的边界情况
            total_overlap += end-qs
        elif qs<start and qe>end: # query 开始结束都在外边
            total_overlap += end -start
        elif qs>= start and qe <= end: # query 开始结束都在里边 包含边缘情况
            total_overlap += qe-qs
        else:
            print('check algorithm')
    print(total_overlap, total_range)
    ratio = float(total_overlap)/float(total_range)
    return ratio

open_hours =[Open_range(9,17)]
qs = 7
qe = 11
print(business_open_ratio(open_hours,qs,qe))
