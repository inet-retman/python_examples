# Purpose of this script is to analyze the pre-trade opportunity
# when two closed end funds are merging

# variables are hardcoded, it is suggested that actual users copy
# the template script into a new execuetable filename
# for managing several trade opportunities or extend the script to handle i/o more gracefully

import math

# Input initial data

# Fund Trading Symbols
acquirer = ""
target   = ""

acquirer_mkt_px =
acquirer_nav_px =

target_mkt_px   =
target_nav_px   =

#End Initial Data

# calculate the premium/discount of each fund
acquirer_pd = (acquirer_mkt_px/acquirer_nav_px)-1
target_pd   = (target_mkt_px/target_nav_px)-1

# calculate the differential in value between the premuims/discounts
merger_differential =  acquirer_pd - target_pd

# calculate the NAV exchange ratio
# it is assumed the merger is 1:1
nav_exchange_ratio = target_nav_px/acquirer_nav_px

# do a pnl run for X shares, default is a thousand
# include comissions, default is half a cent per share

commission_per_share = 0.005
number_shares        = 1000

# buy the target
target_shares = number_shares
target_value = (target_shares*commission_per_share) + (target_shares * target_mkt_px)

# merger occurs
acquirer_shares = target_shares * nav_exchange_ratio;

#round down, cash out fractional value at NAV
acquirer_fractional_shares = acquirer_shares - math.floor(acquirer_shares)
acquirer_shares = math.floor(acquirer_shares)
acquirer_fractional_value = acquirer_fractional_shares * acquirer_nav_px

#sell shares at market price include comissions
acquirer_value = (acquirer_shares * acquirer_mkt_px) - (acquirer_shares*commission_per_share)

#compute PnL
pnl = acquirer_value - target_value

# compute acquirer_mkt_px break_even

acquirer_cost_basis_per_share = target_value / acquirer_shares





debug = False
# pretty print!
if debug:
         print("\n%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
         print("acquirer_pd = ",acquirer_pd)
         print("target_pd   = ",target_pd)
         print("merger_differential = ",merger_differential)
         print("nav_exchange_ratio = ",nav_exchange_ratio)
         print("target_shares = ",target_shares)
         print("target_value = ",target_value)
         print("acquirer_shares = ",acquirer_shares)
         print("acquirer_value = ",acquirer_value)
         print("pnl abs = ",pnl)
         print("pnl %   = ",pnl/target_value)
         print("acquirer_cost_basis_per_share = ",acquirer_cost_basis_per_share)


print(f"{'Funds':>25} {target:>15} {acquirer:>15}")
print(f"{'Mkt Px $':>25} {target_mkt_px:>15} {acquirer_mkt_px:>15}")
print(f"{'NAV Px $':>25} {target_nav_px:>15} {acquirer_nav_px:>15}")
print(f"{'P/D %':>25}    {target_pd*100:>15}      {acquirer_pd*100:>15}")
print(f"{'Merger Diff %':>25}        {merger_differential*100:>15}")
print(f"{'NAV Exchange Ratio':>25}   {nav_exchange_ratio:>15}")
print(f"{'Number of Shares':>25}     {number_shares:>15}")
print(f"{'Risk Capital $':>25}       {target_value:15}")
print(f"{'Epected Profit $':>25}     {pnl:15}")
print(f"{'Return on Capital %':>25}   {(pnl/target_value)*100:15}")
