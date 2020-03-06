#https://www.1point3acres.com/bbs/forum.php?mod=viewthread&tid=554308&highlight=yelp%2BOA

# active business
class Event(object):
    def __init__(self, type, times, biz_id):
        self.type = type
        self.times = times
        self.biz_id = biz_id


def findActiveBusiness(events):
   businesses = {'photo_views':[], 'ads':[], 'page_views':[], 'reviews':[]}
   businesses_counts = {} # 计算平均值
   for i in range(len(events)):  # 第一步， map event type to list of occurence
       if events[i].type in businesses:
           if events[i].times != 0: # 安全起见考虑0 的情况
               businesses[events[i].type].append(events[i].times)
   for key in businesses # 第二步，计算平均count
       vals = businesses[key]
       if vals == []:
           businesses_counts[key] = 0
       else:
           businesses_counts[key] = float(sum(vals))/ float(len(vals))
   active_business_id = {}
   for event in events: # 第三步 map id to list of events that's active
       if event.times!=0 and event.times>= businesses_counts[event.type]:
            if event.biz_id not in active_business_id:
                active_business_id[event.biz_id]= [event.type]
            else:
                active_business_id[event.biz_id].append(event.type)

   res = []
   print(active_business_id )
   for key in active_business_id: # 第四步骤， 看谁大于2
       if len(active_business_id[key])>=2:
           res.append(key)
   return sorted(res)

events = []
events.append(Event("ads",7,3))
events.append(Event("ads", 8,2))
events.append(Event("ads", 5,1))
events.append(Event("page_views", 11,2))
events.append(Event("page_views", 12,3))
events.append(Event("photo_views", 10,3))
events.append(Event("reviews", 0,2))
res = findActiveBusiness(events)
print(res)

