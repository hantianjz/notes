# Latch
- Latch product, software ecosystem of building, 8 product.
- Property management assistance
- 3rdparty app integration with home automation integration
- Senior firmware role, smart access business unit.
- Cross functional team, 3 manager's team.
- AA battery, 32bit arm, FreeRTOS, Bluetooth, AWS
- TI/Nordic
- ~400 people currently looking to grow 90 more company wide
- 09/20: Phone screen with David Webster. Asked prime finding question, forgot how to efficiently find prime, this was a Doh moment.
- Mostly C shop, didn't want me to use different programming language.
- David Webster: 
    - Joined 3-4 months ago
    - Very Good ramp up to the company so far, impressed with the process
    - Lack of casual encounters, good team of people
    - LatchOS is marketing term
    - Some devices in the field, target multi residency buildings

# Onsite interview
**Schedule**  
10:00AM (EDT) - 10:45AM (EDT): Coding interview #1 with [Adam Incera](https://www.linkedin.com/in/adamincera/) (Senior Firmware Engineer)  
- First interview of the day, don't have any coderpad links setup yet like phone screening, wonder how will this go
- really dragged on the consumer producer problem more than I should have, not sure why I didn't see the solution in the first place, I probably should refresh my concurrency  

10:45AM (EDT) - 11:30AM (EDT): Coding interview #2 with [Sam Friedman](https://www.linkedin.com/in/sam-friedman-8a7571a3/) (Staff Firmware Engineer)  
- I think I did okay, this was a decent interview, but required way to much help
- The overall interview process was very nice and honestly smooth, the interview process is a good sell.
```c
#include <stdio.h>
#include <stddef.h>
#include <stdbool.h>
#include <stdint.h>

// To execute C, please define "int main()"
// start: [ 9, 3, 5, 7, 8 ]
// end:   [10, 4, 6, 8, 9 ]

bool chk_overlap(uint8_t *start, size_t start_size, uint8_t * end, size_t end_size) {
  if (start_size != end_size) {
    return false;
  }
  
  for (int i = 0; i < start_size; i++) {
    uint8_t s = start[i];
    uint8_t e = end[i];
    
    for (int j = i+1; j < start_size; j++) {
      uint8_t so = start[j];
      uint8_t eo = end[j];
      //                  so - eo
      //        s  - e
      //   so--eo
      printf("s:%d; e:%d; so:%d; eo:%d\n", s, e, so, eo);
      bool over = !((e <= so) || (eo <= s));
      if (over) {
        return true;
      }
    }
  }
  return false;
}

int main() {
  uint8_t start[] = { 1, 1 };
  uint8_t end[]=   { 10, 10 };
  //uint8_t start[] = { 3, 5  };
  //uint8_t end[]=   {  4, 6 };
  bool ret = chk_overlap(start, sizeof(start), end, sizeof(end));
  printf("ret: %d", ret);
  return 0;
}
```



11:45AM (EDT) - 12:25PM (EDT):  Hiring manager chat with Tyler Wickenhauser  
- Asked me a lot of behaviour questions, seems interesting
- He is only been at company at 7month, feels some what fresh
- Getting a very by the book ridge read from him, I wonder what is his background
- 

12:45PM (EDT) - 1:30PM (EDT): System design interview with Tyler Gage.
(Engineering Manager, Firmware)  
- 30 people
- 5 legacy product, by old people
- old product hw is over complex, sunset older product
- data driven of fleet device
- no more china trips also

1:30PM (EDT) - 2:00PM (EDT): Interview with Lauren Schnee, [Nico Gonzalez](https://www.linkedin.com/in/nicocgonzalez/) (Technical Recruiter)
- Update Oct 7th.