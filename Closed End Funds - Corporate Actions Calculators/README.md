# Closed End Fund Calc Scripts

I wrote scripts to assist in analyzing/managing opportunities for CEF corporate actions. These scripts were meant to be run fairly idionsyncritically and adjusted to suit each situation as they developed. Often I batch ran a collection of modified scripts inside a larger control script that reflected what I was interested in that day/week of trading, outputting a large text block of summary information. I was generally unconcerned with aesthetic presentation for the output.

- [merger_arb_opportunity.py](#merger_arb_opportunity)
- [merger_arb_pnl.py](#merger_arb_pnl)

Depending on available data sources, scripts were amended to auto-update prices, NAVs, positions, etc. or required manual update. 

## merger_arb_opportunity.py

The script compares two funds that are being mergered into a single fund. The aquirer fund and the target fund.
The user must edit the script to input the values for 

- symbol indentifiers/fund names
- fund market prices
- fund NAV prices
- trading commissions per share

I generally tend to copy the script for each instance of a merger, appending the target fund's symbol to the script filename. 
Since deal terms vary, this also helps to incorporate idiosyncratic elements of each corporate action, and the user can extend the pricing and analytic logic to accomodate the deal if it's not vanilla.

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
         Epected Profit $     489.41499999999905
      Return on Capital %   3.3904745410460615

```

## merger_arb_pnl.py

The script computes the current Mark to Market PnL and the projected PnL based on the merger completing at the current values. The position is assumed as long the target's shares. 
The user must edit the script to input the values for 

- symbol indentifiers/fund names
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

In this scenario, we hold 2000 shares of "BBF" which will be aquired by "BLE". Since the aquiring fund's premium is larger then the target fund's current discount and the target fund has appreciated in market price since the shares were aquired, both the MTM and projected post-merger values are profitable.

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
