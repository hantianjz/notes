# Sidewalk labs
- 2015 founded, Dan.
- Early days operate as thinktank
- 2018 bid on Toronto waterfront properly developer
- 2020 effected the Toronto project, not ready for city scale development
- Doing sustainable development, learned from this exchange
- Become a product company, to over product to builder and developers to build better
- Mesa
- Pebble
- Delve
Senior embedded engineer:
- TL: scope and explore, and implement
- Estimating workload and risk
- Overall company: Topco, centralize corp services
    - Typical 
    - Centralized design team
    - Incubation
    - Consulting service
    - Policy maker
- Sub operating company
    - Product development
    - Lean teams, 20-30 employee, senior director of product
    
# Interview On-site
**Technical**   
Date/Time: Oct 4, 2021 12:00pm-1:00pm EDT  
Interviewers: Noah Greenbaum, Linjia Chang  
- Asked a lot of basic Cpp question, not sure how to react to it
- Noah is a manager of the team

**Technical-System Architecture**  
Date/Time: Oct 4, 2021 2:00pm-3:00pm EDT  
Interviewers: Noah Greenbaum, Louisa Sainz De La Maza  
- 5 SW, 2 HW, 2 FW, 20K sensors
- 5 sensors is not enough for 
- Gateway device, pebble HW
- OMG they are scrappy, are you kidding me, they have 2.5 FW engineer right now?
- Oh I really don't want to be working on low powered product like this anymore.

**4th Dimension**  
Date/Time: Oct 5, 2021 10:30am-11:15am EDT  
Interviewers: Tom George  
- Follow up cultural fit interview, I think I answered all the right questions
- I was blabing a lot, kind of feel bad that I might not want to take this job, honestly it doesn't rank pretty high on my list right now
- The company have a lot of Asian employees

**Working with Others**  
Date/Time: Oct 5, 2021 2:00pm-2:45pm EDT  
Interviewers: Kristine Sarnlertsophon  
- Asked a lot of project balance question, honestly this is not a good way to interview the candidate
  
**Wrap up Conversation**  
Date/Time: Oct 5, 2021 3:00pm-3:30pm EDT  
Interviewers: Krishana House  
  
Please use link for all interviews  
Google Meet: [https://meet.google.com/jog-ghib-wud](https://meet.google.com/jog-ghib-wud)

During the call we plan to share more details on the role and will look to learn more about some of your most relevant achievements.

```c
#include <cstdint>
#include "timer.h"

// void (timer_cb*)();
// timer_set_time(uint32_t ms, timer_cb cb);
// 

class GPIOPin
{

public:
 // ALREADY IMPLEMENTED
 // Get the current state of GPIO pin
 // Returns a bool of the state (true=high, false=low)
 static bool GetPinState() { return true; };
};

class ToggleSwitch
{
public:
 // Constructor for the ToggleSwitch object.
 // pin: What GPIO pin to use
 ToggleSwitch(GPIOPin& pin) : gpio_pin_(pin) {
 curr_state = State::kSwitchLow;
 gpio_val = false;
 };

 // Values returned by GetState()
 enum State : std::uint8_t
 {
 kSwitchLow = 0,
 kSwitchHigh = 1,
 kSwitchUndef = 2,
 };
 
 void UpdateSwitch() {
 // toggle switch have settled here update final switch state 
 bool gv = gpio_pin_.GetPinState();
 if (gv) {
 curr_state = State::kSwitchHigh;
 } else {
 curr_state = State::kSwitchLow;
 }
 gpio_val = gv;
 }

 // Get the current state of the toggle switch.
 State GetSwitchState() const { 
 // Getting current gpio state
 bool gv = gpio_pin_.GetPinState();
 if ((curr_state != State::kSwitchUndef) && (gv != gpio_val)) {
 timer_set_time(500, this::UpdateSwitch);
 curr_state = State::kSwitchUndef;
 gpio_val = gv;
 }

 return curr_state;
 };

private:
 State curr_state;
 bool gpio_val;
 GPIOPin& gpio_pin_;
};

int main()
{
 GPIOPin gpio_pin;
 ToggleSwitch toggle_switch(gpio_pin);
 for (;;)
 {
 if (toggle_switch.GetSwitchState() == ToggleSwitch::kSwitchHigh)
 {
 return 0;
 }
 }
}
```