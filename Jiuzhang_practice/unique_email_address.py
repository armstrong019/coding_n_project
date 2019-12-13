class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        name_dict = {}
        for email in emails:
            local_name, global_name = email.split('@')
            local_name = local_name.replace('.','')
            actual_name = local_name.split('+')
            actual_name = actual_name[0]
            address = actual_name+'@'+global_name
            if address not in name_dict:
                name_dict[address] = True
        return len(name_dict)

# 简单逻辑， 主要学习s.replace（'a'，''） replace a with nothing， 这个操作不是inplaced
