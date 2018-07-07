# turo_arbitrage
Finding vehicle arbitrage opportunities in the Turo car rental marketplace
<center><h1><a href="https://www.kaggle.com/theriley106/turo-rental-car-pricing-info">Download the Dataset Here</a></h1></center>


# Model S *Used* Market Prices
| Model   | Market Price   |
| -------------------- |----------:|
|2016.5 AWD 70D | $64,688.71|
|RWD 85 kWh Battery | $59,365.30|
|2016.5 4dr Sedan AWD 60D | $71,496.00|
|90D AWD | $85,877.00|
|AWD 90D Dual Motor | $78,599.00|
|75 RWD | $68,713.08|
|P85D - NAV - SNRF - RRVW | $78,995.00|
|Performance | $54,251.15|
|75D AWD | $78,689.00|
|4dr Sedan Performance | $51,747.00|
|AWD P85D Performance | $71,238.36|
|RWD 70 kWh Battery | $59,738.50|
|2016.5 AWD 90D | $75,068.14|
|P100D AWD | $109,993.00|
|2016.5 4dr Sedan RWD 60 | $61,329.00|
|Sedan | $46,943.38|
|P85D 1 Owner Clean Carfax Autopilot | $76,888.00|
|2016.5 AWD P90D | $94,989.67|
|P85D | $65,309.50|
|4dr Sedan P85D | $65,995.00|
|2016.5 RWD 75 kWh Battery | $66,626.33|
|2016.5 4dr Sedan AWD P100D | $115,561.33|
|100D AWD | $81,497.50|
|2016.5 AWD 75D | $70,492.40|
|4dr Sedan | $46,988.00|
|AWD 70D Dual Motor | $61,823.19|
|4dr Sedan Signature Performance | $48,500.00|
|RWD 60 kWh Battery | $50,832.86|
|4dr Sedan 85 kWh Battery | $52,683.95|
|4dr Sedan Signature | $49,151.60|
|AWD 85D Dual Motor | $64,942.06|

```python
# This is a helper function to convert the floats into dollar amounts
# This was used for creating the README...
def convertMoney(string_val):
	f = re.findall("(\d+.\d+)\|", str(string_val))
	for val in f:
		string_val = string_val.replace(val, '${:,.2f}'.format(float(val)))
	return string_val
```
