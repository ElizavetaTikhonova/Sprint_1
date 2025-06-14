str='1h 45m,360s,25m,30m 120s,2h 60s'
new_list = str.split(sep=',')
sum = 0 

for time in new_list:
    parts_time = time.split(sep=' ')
    

    for part_time in parts_time:
        
        if 'h' in part_time:
            a = int(part_time.replace('h', ''))
            sum += a * 60
        
        if 'm' in part_time:
            a = int(part_time.replace('m', '')) 
            sum += a

        if 's' in part_time:
            a = int(part_time.replace('s', '')) 
            sum += a // 60
print(sum)    
