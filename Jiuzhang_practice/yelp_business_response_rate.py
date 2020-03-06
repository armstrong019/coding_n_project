class Message:
    def __init__(self, sender, recipient, conversation_id):
        self.sender = sender
        self.recipient = recipient
        self.conversation_id = conversation_id

#3
"""
    Sample Input:
        biz_owner_id: 42
        all_messages: [
            {"sender": 1,  "recipient": 42, "conversation_id": 1},
            {"sender": 42, "recipient": 1,  "conversation_id": 1},
            {"sender": 2,  "recipient": 42, "conversation_id": 2},
            {"sender": 2,  "recipient": 42, "conversation_id": 2},
            {"sender": 3,  "recipient": 88, "conversation_id": 3},
            {"sender": 3,  "recipient": 42, "conversation_id": 4},
        ]

    Sample Output:
        33 (Business owner 42 received three conversations total (1, 2, and 4), but only
        responded to one conversation (conversation ID 1)).
"""

def business_responsiveness_rate(bid, all_messages):
    if not all_messages:
        return 0
    request = {}
    response = {}
    res = 0
    for i in range(len(all_messages)):
        if all_messages[i].recipient== bid:
            request_id = str(all_messages[i].sender)+'_'+str(all_messages[i].conversation_id)
            if request_id not in request:
                request[request_id] = i
            else:
                continue
    for j in range(len(all_messages)):
        if all_messages[j].sender==bid:
            response_id = str(all_messages[j].recipient)+'_'+str(all_messages[j].conversation_id)
            if response_id in request and request[response_id]<j:
                if response_id not in response:
                    response[response_id] = True
                    res+=1
    print(request, response)

    if res == 0:
        return 0
    return int(res/len(request)*100)

def business_responsiveness_rate2(biz_owner_id, all_messages):
    #TODO: COMPLETE ME
    if not all_messages:
        return 0
    res = 0
    receive = {}
    response = {}
    for i in range(len(all_messages)):
        if all_messages[i].sender == biz_owner_id:
            if all_messages[i].conversation_id not in response:
                response[all_messages[i].conversation_id] = all_messages[i].recipient
        if all_messages[i].recipient == biz_owner_id:
            if all_messages[i].conversation_id not in receive:
                receive[all_messages[i].conversation_id] = all_messages[i].sender
    for key in receive:
        if key in response:
            if response[key] == receive[key]:
                res += 1
    print(receive, response)
    if not receive:
        return 0
    res = res/len(receive) * 100
    return int(res)

# messages = []
# sender = [1, 42, 2, 2, 3, 3]
# recipient = [42, 1, 42, 42, 88, 42]
# con = [1, 1, 2, 2, 3, 4]
# for i in range(6):
#     messages.append(Message(sender[i], recipient[i], con[i]))
# res = business_responsiveness_rate(42, messages)
# print(res)

messages = []
sender =    [81, 842, 81,  842, 82, 82,  83, 842]
recipient = [842, 81, 842, 81, 842, 842, 842,83]
con =       [81,  81, 81,  81, 82, 82,   83, 83]
for i in range(len(sender)):
    messages.append(Message(sender[i], recipient[i], con[i]))
res = business_responsiveness_rate(842, messages)
print(res)

#3
"""
    Sample Input:
        biz_owner_id: 842
        all_messages: [
            {"sender": 81,  "recipient": 842, "conversation_id": 81},
            {"sender": 842, "recipient": 81,  "conversation_id": 81},
            {"sender": 81,  "recipient": 842, "conversation_id": 81},
            {"sender": 842,  "recipient": 81, "conversation_id": 81},
            {"sender": 82,  "recipient": 842, "conversation_id": 82},
            {"sender": 82,  "recipient": 842, "conversation_id": 82},
            {"sender": 83,  "recipient": 842, "conversation_id": 83},
            {"sender": 842,  "recipient": 83, "conversation_id": 83},
        ]

    Sample Output:
        33 (Business owner 42 received three conversations total (1, 2, and 4), but only
        responded to one conversation (conversation ID 1)).
"""
