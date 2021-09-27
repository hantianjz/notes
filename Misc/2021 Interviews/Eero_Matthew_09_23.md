```python

 #  # Your previous Plain Text content is preserved below: # 
# Welcome, James!
# 
# Parse a file with profiling events formatted as [ $timestamp_in_seconds ] event $event_name (START|STOP) and output stats (max and average) for each event type.
# 
# For example:
# [    0.000000] event foo.bar START
# [    0.500000] some other generic log that should be ignored
# [    1.000000] event foo.bar STOP
# [    2.000000] event foo.bar START
# [    5.000000] event foo.bar STOP
# [    6.000000] event foo.qux START
# [    7.000000] event foo.qux STOP
# 
# 
# Would output something like:
# foo.bar: max = 3, average = 2
# foo.qux: max = 1, average = 1
# 
# 
# Enjoy your interview!
# 

class EvtStat():
    
    def __init__(self, evt_name):
        self.evt_name = evt_name
        self.max = 0
        self.avg = 0
        self.cnt = 0
        
        self.start_time = 0.0
        
    def __repr__(self):
        return f"max:{self.max}, average:{self.avg}"
    
    def start(self, time):
        self.start_time = time
    
    def stop(self, time):
        dur = time - self.start_time
        self.max = max(dur, self.max)
        self.avg = (dur + (self.avg * self.cnt)) / (self.cnt + 1)
        self.start_time = 0
        self.cnt += 1

def parse_line(line):
    if not line:
        return None, None, None
    # TODO: Find the start [ for proper start string
    time = float(line.split("]")[0][2:].strip())
    log_str = line.split("]")[1].strip()
    log = log_str.split()
    if log[0] == "event":
        return time, *log[1:]
    else:
        return None, None, None

def parse_file(fstr):
    tb = {}
    for line in fstr.split('\n'):
        time, evt, act = parse_line(line)
        if not evt:
            continue
        if evt not in tb:
            tb[evt] = EvtStat(evt)
        if act == "STOP":
            tb[evt].stop(time)
        elif act == "START":
            tb[evt].start(time)
    return tb
                
        
print(parse_file("""
 [    0.000000] event foo.bar START
 [    0.500000] some other generic log that should be ignored
 [    1.000000] event foo.bar STOP
 [    2.000000] event foo.bar START
 [    5.000000] event foo.bar STOP
 [    6.000000] event foo.qux START
 [    7.000000] event foo.qux STOP"""))
```