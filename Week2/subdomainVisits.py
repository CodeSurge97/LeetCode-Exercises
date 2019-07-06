def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        dic = {}
        for item in cpdomains:
            cp = item.split()
            
            count = int(cp[0])  # <- at first, I forgot `int()`: easy to miss
            dom = cp[1].split(".")
            
            for j in range(len(dom)):
                subdomain = ".".join(dom[j:])
                if subdomain in dic:
                    dic[subdomain] += count
                else:
                    dic[subdomain] = count
        
        
        return [str(val)+" "+str(key) for key, val in dic.items()]