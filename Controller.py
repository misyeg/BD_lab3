import View
import Model
import time

while 1==1:
    View.hello()
    choice = input("Оберіть варіант: ")
    #model = Model.db_model("lab", "postgres", "111", "")

    match choice:
        case "1":
            table = input("Введіть назву таблиці: ")
            val = input("Введіть відповідні значення: ").split(' ')

            match table:
                case "driver":
                    s = Model.Session()
                    driver = Model.Driver(name=val[0])
                    s.add(driver)
                    s.commit()
                    s.close()
                case "train":
                    s = Model.Session()
                    train = Model.Train(datetime=val[0])
                    s.add(train)
                    s.commit()
                    s.close()
                case "carriage":
                    s = Model.Session()
                    carriage = Model.Carriage(train_id=val[0], carriage_type=val[1])
                    s.add(carriage)
                    s.commit()
                    s.close()
                case "place":
                    s = Model.Session()
                    place = Model.Place(carriage_id=val[0])
                    s.add(place)
                    s.commit()
                    s.close()
                case "ticket":
                    s = Model.Session()
                    ticket = Model.Ticket(place_id=val[0])
                    s.add(ticket)
                    s.commit()
                    s.close()

            time.sleep(4)

        case "2":
            table = input("Введіть назву таблиці: ")
            val = input("Введіть id: ").split(' ')
            znach = input("Введіть відповідні значення: ").split(' ')

            match table:
                case "driver":
                    s = Model.Session()
                    driver = s.query(Model.Driver).filter(Model.Driver.drier_id == val[0]).first()
                    driver.name = znach[0]
                    s.commit()
                    s.close()

                case "train":
                    s = Model.Session()
                    train = s.query(Model.Train).filter(Model.Train.train_id == val[0]).first()
                    train.datetime = znach[0]
                    s.commit()
                    s.close()

                case "carriage":
                    s = Model.Session()
                    carriage = s.query(Model.Carriage).filter(Model.Carriage.carriage_id == val[0]).first()
                    carriage.carriage_type = znach[0]
                    carriage.train_id = znach[1]
                    s.commit()
                    s.close()

                case "place":
                    s = Model.Session()
                    place = s.query(Model.Place).filter(Model.Place.place_id == val[0]).first()
                    place.carriage_id = znach[0]
                    s.commit()
                    s.close()

                case "ticket":
                    s = Model.Session()
                    ticket = s.query(Model.Ticket).filter(Model.Ticket.ticket_id == val[0]).first()
                    ticket.place_id = znach[0]
                    s.commit()
                    s.close()

            time.sleep(4)

        case "3":
            table = input("Введіть назву таблиці: ")
            val = input("Введіть відповідні значення: ").split(' ')

            match table:
                case "driver":
                    s = Model.Session()
                    driver = s.query(Model.Driver).filter(Model.Driver.driver_id == val[0]).first()
                    s.delete(driver)
                    s.commit()
                    s.close()

                case "train":
                    s = Model.Session()
                    train = s.query(Model.Train).filter(Model.Train.train_id == val[0]).first()
                    s.delete(train)
                    s.commit()
                    s.close()

                case "carriage":
                    s = Model.Session()
                    carriage = s.query(Model.Carriage).filter(Model.Carriage.carriage_id == val[0]).first()
                    s.delete(carriage)
                    s.commit()
                    s.close()

                case "place":
                    s = Model.Session()
                    place = s.query(Model.Place).filter(Model.Place.place_id == val[0]).first()
                    s.delete(place)
                    s.commit()
                    s.close()

                case "ticket":
                    s = Model.Session()
                    ticket = s.query(Model.Ticket).filter(Model.Ticket.ticket_id == val[0]).first()
                    s.delete(ticket)
                    s.commit()
                    s.close()

            time.sleep(4)

        case _:
            print("Error")




