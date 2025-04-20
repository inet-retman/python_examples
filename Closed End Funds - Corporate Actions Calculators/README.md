# Closed End Fund Calc Scripts

I wrote scripts to assist in analyzing/managing opportunities for CEF corporate actions. These scripts were meant to be run fairly idiosyncratically and adjusted to suit each situation as they developed. Often I batch ran a collection of modified scripts inside a larger control script that reflected what I was interested in that day/week of trading, outputting a large text block of summary information. I was generally unconcerned with aesthetic presentation for the output.

I wrote these scripts mostly in 2020-21 and used Yahoo! Stocks, cefconnect.com, and the Interactive Brokers Trader Workstation API as input data sources.

*DISCLAIMER:* **Trading in closed end funds undergoing corporate actions requires more complex analysis then the scripts here perform, risk of loss or profit is impacted by a myriad of valuation factors including trading volume, the make-up of shareholders, corporate action processing, stock/loan borrow availability and rates, distributions, and NAV price volatility, among many other factors**    

- [merger_arb_opportunity.py](#merger_arb_opportunity)
- [merger_arb_pnl.py](#merger_arb_pnl)
- [tender_offer_opportunity.py](#tender_offer_opportunity)

Depending on available data sources, scripts were amended to auto-update prices, NAVs, positions, etc. or required manual update.

## merger_arb_opportunity.py

The script compares two funds that are being merged into a single fund. The acquirer fund and the target fund.
The user must edit the script to input the values for

- symbol identifiers/fund names
- fund market prices
- fund NAV prices
- trading commissions per share

I generally tend to copy the script for each instance of a merger, appending the target fund's symbol to the script filename.
Since deal terms vary, this also helps to incorporate idiosyncratic elements of each corporate action, and the user can extend the pricing and analytic logic to accommodate the deal if it's not vanilla.

```
# Input data
acquirer = "BLE"
target   = "BBF"

acquirer_mkt_px = 15.60
acquirer_nav_px = 15.01

target_mkt_px   = 14.43
target_nav_px   = 14.37
```
In this scenario BLE will aquire BBF, and both funds are currently trading at a premium.
Since BLE's premium is larger then BBF, it is a profitable opportunity at current market prices and NAVs
```
$ ./merger_arb_opportunity_BBF.py
                    Funds             BBF             BLE
                 Mkt Px $           14.43            15.6
                 NAV Px $           14.37           15.01
                    P/D %    0.41753653444676075      3.9307128580946094
            Merger Diff %        3.5131763236478486
       NAV Exchange Ratio   0.9573617588274483
         Number of Shares                1000
           Risk Capital $               14435.0
         Expected Profit $     489.41499999999905
      Return on Capital %   3.3904745410460615

```

## merger_arb_pnl.py

The script computes the current Mark to Market PnL and the projected PnL based on the merger completing at the current values. The position is assumed as long the target's shares.
The user must edit the script to input the values for

- symbol identifiers/fund names
- fund market prices
- fund NAV prices
- position share size
- cost basis per share
- cost basis of entire position
- position accumulated distributions during holding period (input as 0, if you are not concerned with total return)

```
# Input data
acquirer = "BLE"
target   = "BBF"

acquirer_mkt_px = 15.50
acquirer_nav_px = 14.95

target_mkt_px   = 14.10
target_nav_px   = 14.30

position_number_shares        = 2000
position_average_share_price  = 13.781     #includes comissions, excludes distributions
position_cost_basis           = 27560      #includes commissions, excludes distributions
position_distributions        = 185.89     # dividends, distributions, accumulated/accrued so far
```

In this scenario, we hold 2000 shares of "BBF" which will be acquired by "BLE". Since the acquiring fund's premium is larger then the target fund's current discount and the target fund has appreciated in market price since the shares were acquired, both the MTM and projected post-merger values are profitable.

```
$ ./merger_arb_pnl_BBF.py
                    Funds             BBF             BLE
                 Mkt Px $            14.1            15.5
                 NAV Px $            14.3           14.95
                    P/D %    -1.3986013986014068      3.678929765886285
            Merger Diff %        5.0775311644876915
       NAV Exchange Ratio        0.9565217391304349
          Position Shares              2000
Position Average Share Price          13.781
      Position Cost Basis                 27560
        Expected Profit $     2081.9350000000013
      Return on Capital %   7.554190856313503
MTM Unrealized Gain/Loss $            640.0
MTM Unrealized Gain/Loss %  2.3222060957910013
MTM Distrib. Adj. Gain/Loss $          825.89
MTM Distrib. Adj. Gain/Loss %  2.996698113207547
```
## tender_offer_opportunity.py

This script runs and prints out a summary of what the expected PnL and remaining shares would be if a closed end fund tender offer corporate action was conducted based on acquiring shares at the given market price, NAV, and pro-rata.

The user must edit the script to input the values for

- symbol identifier/fund name
- fund market prices
- fund NAV prices
- the tender offer repurchase rate as a decimal percentage of NAV
- the amount of the fund to be repurchased expressed as a decimal rate

```
target   = "BRW"
target_mkt_px   = 4.70
target_nav_px   = 4.91
tender_offer_amount_rate = 0.30
tender_offer_nav_rate = 0.995
```
In this scenario, fund ticker "BRW" will re-purchase 30% of it's outstanding shares at a purchase price of 99.5% of NAV. The fund is trading on the market at a discount to both it's NAV and the repurchase price, therefore the projection of a profitable repurchase on 30% of the position, if purchased at today's market price.

```
$ ./tender_offer_opportunity_BRW.py
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
target      =  BRW
target_pd   =  -4.276985743380857
target_tender_offer_pd =  -3.7959655712370477

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
target_shares =  1000
target_value =  4705.0
tender_offer_shares_repurchased =  300
tender_offer_proceeds =  1465.6350000000002
target_shares_post_tender =  700
target_shares_proceeds =  3286.5
target_shares_post_tender_cost_basis =  2.601235714285714
pnl =  47.13500000000022
```
