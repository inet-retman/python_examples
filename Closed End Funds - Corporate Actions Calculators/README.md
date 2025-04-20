# Closed End Fund Calc Scripts

I have written scripts that helped inform my trading of closed end fund corporate actions.
The frequency of the NAV updates for most closed end funds is daily, for every trading day.

## merger_arb_opportunity.py

The script compares two funds that are being mergered into a single fund. The aquirer fund and the target fund.
The user must edit the script to input the values for 

- symbol indentifiers/fund names
- fund market prices
- fund NAV prices

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
