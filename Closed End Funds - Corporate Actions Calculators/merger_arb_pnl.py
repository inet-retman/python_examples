# Purpose of this script was to track PnL for positions
# PnL based on Mark to Market
# Pnl Projections post-merger
# Outputs a column text summary

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

# calculate the premium/discount of each fund
acquirer_pd = (acquirer_mkt_px/acquirer_nav_px)-1
target_pd   = (target_mkt_px/target_nav_px)-1

# calculate the differential in value between the premuims/discounts
merger_differential =  acquirer_pd - target_pd

# calculate the NAV exchange ratio
# it is assumed the merger is 1:1
nav_exchange_ratio = target_nav_px/acquirer_nav_px

# input data for your current position
# it is assumed your position is in the target fund
# so the variable is not explicitly named

position_number_shares        =
position_average_share_price  =          #includes comissions, excludes distributions
position_cost_basis           =          #includes commissions, excludes distributions
position_distributions        =          # dividends, distributions, accumulated so far

commission_per_share          = 0.005    #default half a cent a share

# merger occurs
acquirer_shares = position_number_shares * nav_exchange_ratio;

#round down, cash out fractional value at NAV
acquirer_fractional_shares = acquirer_shares - math.floor(acquirer_shares)
acquirer_shares = math.floor(acquirer_shares)
acquirer_fractional_value = acquirer_fractional_shares * acquirer_nav_px

#sell shares at market price include comissions
acquirer_value = (acquirer_shares * acquirer_mkt_px) - (acquirer_shares*commission_per_share)

#compute PnL
pnl = acquirer_value - position_cost_basis

# compute acquirer_mkt_px break_even

acquirer_cost_basis_per_share = position_cost_basis / acquirer_shares

# MTM Position Value

position_value = position_number_shares * target_mkt_px

mark_to_market_unrealized_value = position_value - position_cost_basis



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
print(f"{'Position Shares':>25}     {position_number_shares:>15}")
print(f"{'Position Average Share Price'} {position_average_share_price:>15}")
print(f"{'Position Cost Basis':>25}       {position_cost_basis:15}")
print(f"{'Expected Profit $':>25}     {pnl:15}")
print(f"{'Return on Capital %':>25}   {(pnl/position_cost_basis)*100:15}")
print(f"{'MTM Unrealized Gain/Loss $'}  {mark_to_market_unrealized_value:15}")
print(f"{'MTM Unrealized Gain/Loss %'}  {(mark_to_market_unrealized_value/position_cost_basis)*100:15}")
print(f"{'MTM Distrib. Adj. Gain/Loss $'} {mark_to_market_unrealized_value+position_distributions:15}")
print(f"{'MTM Distrib. Adj. Gain/Loss %'}  {((mark_to_market_unrealized_value+position_distributions)/position_cost_basis)*100:15}")
