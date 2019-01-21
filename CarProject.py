import pymysql
#This will be for the list
# Mysql data connections
conn = pymysql.connect(host='127.0.0.1', port=3306, user= "root", passwd="av233880", db='datascience' )
cur = conn.cursor()

desc = None # create a variable but without a value
while desc != 'quit':
    print("\n")
    carmake = input("Enter in a Car Make\nFord \t Chevrolet \t Dodge\n")
    loop = True
    while loop:
        if carmake == "Ford":
            #print("You picked Ford")
            carModel = input("Mustang or F150\n")
            if carModel == 'Mustang':
                break
            elif carModel == 'F150':
                break
            else:
                print("Enter in value from F150 or Mustang")
        elif carmake == "Dodge":
            #print("You picked Ford")
            carModel = input("Challenger or Charger or Ram\n")
            if carModel == 'Challenger':
                break
            elif carModel == 'Charger':
                break
            elif carModel == 'Ram':
                break
        elif carmake == 'Chevrolet':
            carModel = input("Camaro or Silverado\n")
            if carModel =='Camaro':
                break
            elif carModel =='Silverado':
                break
        else:
            carmake = input("Enter in a Car Make\nFord \t Chevrolet \t Dodge\n")
    print("\n")
    choice = input("1:Average MPG\n2:Sum of Total Cars Sold\n"+
                    "3:Average HorsePower\n4:0-60 Speed\n"+
                    "5:Lowest HoresePower\n6:Highest HoresePower\n"+
                    "7:Average Curb Weight\n8:Average MPG for All Model\n\nCompare Each Model\n" + 
                    "9:Average HP for All Model\n" +
                    "10:Average Sales for All Mode\n11:Average Curb Weight for All Models\nQ:Use Q to quit\n")
    if choice == "1":
        sql_beh = ("Select avg(MPG) from CarInfo where Make = '%s' and Model = '%s'" %(carmake,carModel))
        cur.execute(sql_beh)
        for row in cur:
            curbweight = row[0]
            print("Average MPG:  " + str(curbweight) +" " + carmake + " " + carModel)
    elif choice == "2":
        sql_beh = ("Select sum(Sales_Price) from CarInfo where Make = '%s' and Model = '%s'" %(carmake,carModel))
        cur.execute(sql_beh)
        for row in cur:
            curbweight = row[0]
            print("Total Cars sold:  " + str(curbweight) +" " + carmake + " " + carModel)

    elif choice == "3":
        sql_beh = ("Select avg(HP) from CarInfo where Make = '%s' and Model = '%s'" %(carmake,carModel))
        cur.execute(sql_beh)
        for row in cur:
            curbweight = row[0]
            print("Average HorsePower:  " + str(curbweight) +" " + carmake + " " + carModel)
            print("\n")

    elif choice == "4":
        sql_beh = ("Select HP,CurbWeight,Year from CarInfo where Make = '%s' and Model = '%s'" %(carmake,carModel))
        cur.execute(sql_beh)
        for row in cur:
            hp = row[1]
            curbweight = row[0]
            Year = row[2]
            zerotosixty = (float(hp) / int(curbweight))
            print("0-60 speed:  " + str(zerotosixty) +" seconds  \tfor  " + carmake + " " + carModel + " " + Year) 

    elif choice == "5":
        sql_beh = ("Select min(HP) from CarInfo where Make = '%s' and Model = '%s'" %(carmake,carModel))
        cur.execute(sql_beh)
        for row in cur:
            curbweight = row[0]
            print("Min HorsePower:  " + curbweight +" " + carmake + " " + carModel)

    elif choice == "6":
        sql_beh = ("select max(HP) from CarInfo where Make = '%s' and Model = '%s'" %(carmake,carModel))
        cur.execute(sql_beh)
        for row in cur:
            curbweight = row[0]
            print("Max HorsePower:  " + curbweight +" " + carmake + " " + carModel)

    elif choice == "7":
        sql_beh = ("select avg(CurbWeight) from CarInfo where Make = '%s' and Model = '%s'" %(carmake,carModel))
        cur.execute(sql_beh)
        for row in cur:
            avcw = row[0]
            print("Average Curb Weight: " + str(avcw) + " " + carmake + " "+ carModel) 

    elif choice == "8":
        sql_beh = ("select avg(MPG),Model from CarInfo  group by Model")
        cur.execute(sql_beh)
        for row in cur:
            mpg = row[0]
            model = row[1]
            print(str(mpg)+"\tMPG " + model)

    elif choice == "9":
        sql_beh = ("select avg(HP),Model from CarInfo group by Model")
        cur.execute(sql_beh)
        for row in cur:
            hp = row[0]
            model = row[1]
            print(str(hp)+ " HP " +  " " +  model)

    elif choice == "10":
        sql_beh = ("select avg(Sales_Price),Model from CarInfo group by Model")
        cur.execute(sql_beh)
        for row in cur:
            sales_price = str(row[0])
            year = row[1]
            print("Sales Price: " + str(sales_price) + "\t" + year)
    elif choice == "11":
        sql_beh = ("select avg(CurbWeight),Model from CarInfo group by Model")
        cur.execute(sql_beh)
        for row in cur:
            curbweight = str(row[0])
            model = row[1]
            print("CurbWeight : " + str(curbweight) + "\t" + model)
    elif choice == 'Q':
        desc = 'quit'
print("Thank you for getting the data")
    