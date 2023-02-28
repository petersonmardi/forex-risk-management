import prettytable

table = [["10%","11%"],["20%","25%"],["30%","43%"],["40%","67%"],["50%","100%"],["60%","150%"],["70%","233%"],["80%","400%"],["90%","900%"]]

# Win Rate | R:R
risk_reward = [['50%', '1:1'],['33%', '1:2'],['25%', '1:3'],['17%', '1:5']]

class DrawdownAndROI:

    def drawdown(self, loss, initial_capital):
        self.drawdown = loss / initial_capital * 100
        print(self.drawdown)
    
    def return_on_investment(self, loss, current_capital):
        self.roi = loss / current_capital * 100
        print(self.roi)
    
    def show_table(self, table):
        x = prettytable.PrettyTable()
        x.field_names = ["Drawdown","ROI Required to Breakeven"]
        x.add_rows(table)
        print(x)
  
  
       
class LotSizeCalculation:
    
    def value_per_pip(self, decimal_places, current_price, units_of_currency):
        """
        Nano lot: [value in dollars -> 100, Decimal -> 0.001, Value per pip in Dollars -> $0.01]
      
        Micro lot: [value in dollars -> 1000, Decimal -> 0.01, Value per pip in Dollars -> $0.10]
      
        Mini lot: [value in dollars -> 10,000, Decimal -> 0.1, Value per pip in Dollars -> $1.00]
      
        Standard lot: [value in dollars -> 100,000, Decimal -> 1, Value per pip in Dollars -> $10.00]
      
        5 Nano lots: [value in dollars -> 500, Decimal -> 0.005, Value per pip in Dollars -> $0.05]
      
        5 Micro lots: [value in dollars -> 5000, Decimal -> 0.05, Value per pip in Dollars -> $0.50]
      
        5 Mini lots: [value in dollars -> 50,000, Decimal -> 0.5, Value per pip in Dollars -> $5.00]
      
        5 Standard lots: [value in dollars -> 500,000, Decimal -> 5, Value per pip in Dollars -> $50.00]
        """
        value = decimal_places / current_price * units_of_currency
        print(value)
    
    def position_size(self, capital, risk_per_trade, stop_loss, value_per_pip):
        risk = risk_per_trade / 100
        size = capital * risk / stop_loss * value_per_pip
        print(size)