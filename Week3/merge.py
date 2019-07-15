def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        
        if not intervals:
            return []
        
        # sort by x-value
        sorted_intervals = sorted(intervals)
        
        # initialize merged list
        merged_intervals = [sorted_intervals[0]]
        
        for current_interval_x, current_interval_y in sorted_intervals[1:]:
            last_merged_interval_x, last_merged_interval_y = merged_intervals[-1]
            
            # if the current interval overlaps with the last merged interval,
            # use the larger y value of the two
            if (current_interval_x <= last_merged_interval_y):
                merged_intervals[-1] = [last_merged_interval_x, max(last_merged_interval_y, current_interval_y)]
            else:
                # add the current interval since it doesn't overlap
                merged_intervals.append([current_interval_x, current_interval_y])
                
        return merged_intervals