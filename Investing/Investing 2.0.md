Using PE & ROA (price to Earnings and Return on Assets)

Use OpenBB to get stock info

I believe Magic Formula is based on PE vs ROA.

Current ration
https://stockanalysis.com/

BKE https://www.google.com/finance/quote/BKE:NYSE
KFY https://www.google.com/finance/quote/KFY:NYSE
CPRX https://www.google.com/finance/quote/CPRX:NASDAQ


To recreate, or simplify what I had done with Stock before.

So each time to define exits.
If stock performs worse than 30% than S&P within the first year.
If stock performs worse than 50% than S&P within the first three years.
Any time after four years and I mostly think negatively.
Anytime I think ethics and honesty are a hard fail.
My worst stock, or smallest position anytime I cross the simple dozen.

Define the too good to be true

Questrade Edge is where you can set alerts

- [x] Compare SCHD dividend 👎 to S&P ✅ 2024-01-24
SCHD Schwab US Dividend Equity ETF
SCHD https://www.google.com/finance/quote/SCHD:NYSEARCA

When it is time to invest.

Review rules for stock exit.
1. Get short list, Magic Formula, Edit image, Export csv from
2. Figure out what exchange the entries are in
3. Create a google batch to open main page
5. Create start script
4. Look for reasonable growth history and purpose
5. Eliminate by ethics
6. mkdir(s)
8. Identify top picks on history and business story that I hear, and get from Google
7. OpenBB
8. Create review of top picks

Key technique
```
stocks
load
quote -csv
candle -png
fa
	dcf -xls
	ratios -csv
	income -csv
	balance -csv
	cash -csv
    fraud M-score 0-1.7? AlphaVantage -csv
	metrics key financial metrics over time -csv
	dupont breakdown for Return on Equity (RoE) -png
	analysis analyse SEC filings with the help of machine learning -csv
```

helpful ideas
mkdir MLI
mkdir GPOR
load --ticker MLI
load --ticker GPOR

# Are Evaluations Excessive
https://www.multpl.com/