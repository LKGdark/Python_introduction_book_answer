class Battery:
    def __init__(self,battery=40):
        self.battery = battery
    
    def get_range(self):
        if self.battery == 40:
            range = 150
        elif self.battery == 65:
            range = 225
    
        print(f"This car can go about {range} miles on a full charge.\n")

    def upgrade_battery(self):
        print("barrery upgrade finish!\n")
        self.battery = 65
    

battery_carbon = Battery()
battery_carbon.get_range()
battery_carbon.upgrade_battery()
battery_carbon.get_range()