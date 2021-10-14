- Gab
- office of the CTO? Really what does that mean and how does it differ from main engineering team
- How is the engineering team organized, software/hardware. Which org does firmware report to.
- Overlap with Amazon
- Role is: software engineer, smart home, low power network, open thread, 
- Level difference for Eero interview, the role is opened for SDE 2, but I should be SDE 3. Should be interviewed at that level maybe
- Zigbee hub solution
- Phone screen for L6 09/23
- Matthew Richards:
    - got drilled in with PR conflict resolution not sure what he was asking for 
    - He was on the phone during some part of the interview 
    - Very hard to get an answer from him
    - Phone screen: 
        - What is your option on Eero's tech debt? If you were given unlimited resource what would you tackle?
        - What do you think about the senior leadership at Eero and it's relationship to Amazon?

[[Eero]] phone screen with Matthew Richards
#interview #techinical_Interview #python

```python

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