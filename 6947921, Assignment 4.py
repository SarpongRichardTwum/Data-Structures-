#List of car prices and their sales prices
carInStore={
    'Maruti Alto 800':20000,
    'Toyota Corolla':50000,
    'Toyota Camry':45000,
    'Hyundai i10':48000,
    'Hyundai Accent':40000,
    'Nissan Sentra':35000,
    'Kia Rio':32000,
    'Renalt Duster':23000,
    'Honda Brio':37000,
    'Maruti Ignis':31000,
    'Hyundai i20':54000,
    'Maruti SX4 s Cross':75000,
    'Hyundai Verna':43000,
    'HondaCity':60000,
    'Maruti Vitara':51000,
    'Hyundai Creta':71000,
    'Maruti Swift':63000,
    'Mercedes Benz E Class':100111,
    'Maruti Boleno':71000,
    'Ford Ecosport':200000,
    'Renault Capture':80000,
    'Toyota Landcruiser':350000,
    'Nissan Navara':160000,
    'Lexus RX':270000,
    'Toyota Rav4':193000,
    'Mercedes Benz C class':300000,
    'Hyundai Elandra':84000,
    'Kia Sportage':200000,
    'kia Rhino':207000,
    'Mecedes-Benz Sprinter':350000,
    'Ford Fieta':70000,  }
#get user input for car name
carName= input ("Enter a carName: ")
#to check if car name is in thelist of available cars
if carName in carInStore:
  print(f"Yes, the car {carName} is available for a price of ${carInStore[carName]} ")
else:
    #if a car name is not present , the user should be informed that
    print(f"The {carName} you want at the moment is unavaible "  )
    
    
        