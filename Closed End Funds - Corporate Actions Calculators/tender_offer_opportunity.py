# Purpose of this script is gauge the Pnl opportunity
# of a closed end fund tender offer given the current market price, NAV
# in conjunction with the buy back price and rate

import math

# Input initial data

# Fund Trading Symbols
target   = ""

target_mkt_px   =
target_nav_px   =

# percentage of outstanding shares to purhcase
tender_offer_amount_rate =


# percentage of NAV to be paid for shares
# expressed as a decimal
tender_offer_nav_rate =

# absolute price to be paid for shares
tender_offer_price  = target_nav_px * tender_offer_nav_rate

# calculate the premium/discount of the fund
target_pd   = (target_mkt_px/target_nav_px)-1

# calculate premium/discount of market price to tender offer purchase price
target_tender_offer_pd = (target_mkt_px/tender_offer_price)-1



# do a pnl run for X shares
# include comissions

commission_per_share = 0.005
number_shares        = 1000

# buy the target
target_shares = number_shares
target_value = (target_shares*commission_per_share) + (target_shares * target_mkt_px)
target_shares_cost_basis = (target_value/target_shares)

# tender offer occurs, do not assume fractional shares
tender_offer_shares_repurchased = math.floor(tender_offer_amount_rate * target_shares)
tender_offer_proceeds           = tender_offer_shares_repurchased * tender_offer_price
tender_offer_pnl                = tender_offer_proceeds - (tender_offer_shares_repurchased * target_shares_cost_basis)

#sell returned shares not accepted at market price include comissions
target_shares_post_tender       = target_shares - tender_offer_shares_repurchased
target_shares_proceeds          = (target_shares_post_tender * target_mkt_px) - (target_shares_post_tender * commission_per_share)
target_shares_pnl               = target_shares_proceeds - (target_shares_post_tender*target_shares_cost_basis)

#compute PnL
pnl = (tender_offer_proceeds+target_shares_proceeds) - target_value

# compute break even on target shares market price, post tender

target_shares_post_tender_cost_basis =  (target_shares_proceeds - tender_offer_proceeds)/target_shares_post_tender


print("\n%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
print("target      = ",target)
print("target_pd   = ",target_pd*100)
print("target_tender_offer_pd = ",target_tender_offer_pd*100)

print("\n%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
print("target_shares = ",target_shares)
print("target_value = ",target_value)

print("tender_offer_shares_repurchased = ",tender_offer_shares_repurchased)
print("tender_offer_proceeds = ",tender_offer_proceeds)

print("target_shares_post_tender = ",target_shares_post_tender)
print("target_shares_proceeds = ",target_shares_proceeds)
print("target_shares_post_tender_cost_basis = ",target_shares_post_tender_cost_basis)

print("pnl = ",pnl)
print("tender_offer_pnl = ",tender_offer_pnl)
print("target_shares_pnl =",target_shares_pnl)
print("pnl %   = ",(pnl/target_value)*100)
