from collections import Counter
import datetime as dt

tweet_names = ["sachin tweet_id_1",
                "sehwag tweet_id_2",
                "sachin tweet_id_3",
                "sehwag tweet_id_4",
                "kohli tweet_id_5",
                "kohli tweet_id_6"] 
    
uniq_names = [pref_names.split()[0] for
              pref_names in tweet_names]
  
times = Counter(uniq_names)
repeat = times.values()
  
for element in set(repeat):
    dupl = ([(key, value) for
             key, value in sorted(times.items()) if
             value == element])
      
    if len(dupl) > 1:
        for (key, value) in dupl:
            print (key,'',value)
    max_value = max(times.values())
    temp_max_result = [(key, value) for 
                       key, value in sorted(times.items()) if
                       value == max_value]
      
    if temp_max_result != dupl:
        for (key,value) in temp_max_result:
            print (key,'',value)
             