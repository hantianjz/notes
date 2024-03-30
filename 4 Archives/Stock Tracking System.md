---
publish: false
reviewed: 2023-08-15
review-frequency: ignore
tags:
  - diary
link:
  - "[[quant]]"
  - "[[asset management]]"
---
Some reading list [[Algo trading reading]]

**2024-01-13**
- Goal today:
    - Figure out how to send SMS msg programmatically
    - Track stock prices
    - Send closing price at end of day
    - Send opening price at start of day
    - Send notification on sudden price jump, or delta within single day

## Sending notification/SMS

- Twilio, sends sms but might get expensive in the long run.
    - But for outbound only SMS it's only 0.79 cent per sms, which might work
    - 2 sms per day * 5 days a week = 10
    - Set a upper limit to max 1 sms per 1 hour, market is only open for 6.5 hours seems like a okay way to start
    - bandwidth seems to be cheaper https://www.bandwidth.com/pricing/
- There is a Twilio recovery code

# Goal
- Track current total assets, and gain vs loss
- View assets by sector/country/type
- Journal each trade decision, and it's origin
- Calculate cap gain tax
- Correlate stock with market
- Set limit and notification
- Bouns: Calculate risk/volatility somehow and derive sharp ratio

**Raw view of inventory**
- ticker
- Quantity 
- Cost basis
- *# of stocks; Sum cost basis*

**Basic summary view**
- Ticker
- Quantity 
- Price per unit 
- Cost basis
- Market value
- Gain/Lose
- *Total everything in columns*
Refresh time *

Delta view (input: today, yesterday, this week, this month, period of time)
- Ticket
- Quantity
- price per unit
- Cost basis
- Market value delta
- Gain/lose delta
- *Summary of columns*

### Inventory system
- Date
- Tickers
- Quantity
- Cost basis

The system properties:
- Persistent 
- Sort by date
- Lookup by date