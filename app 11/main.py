import pandas as pd

df = pd.read_csv("hotels.csv", dtype={"id": str})
df_cards = pd.read_csv("cards.csv", dtype = str).to_dict(orient="records")
df_security = pd.read_csv("card_security.csv" , dtype = str)

class Hotel:
    def __init__(self,hotel_id):
        self.hotel_id = hotel_id
        self.name = df.loc[df["id"] == self.hotel_id,"name"].squeeze()

    def book(self):
        df.loc[df["id"] == self.hotel_id,"available"] = "no"
        df.to_csv("hotels.csv",index=False)

    def available(self):
        availability = df.loc[df["id"] == self.hotel_id,"available"].squeeze()
        return availability == "yes"


class ReservationTickets:
    def __init__(self, name, hotel_object):
        self.name = name
        self.hotel = hotel_object
        

    def generate(self):
        content ="""
        thanks for the reservation
        Name :{self.name}
        Hotel Name :{self.hotel.name}
        """

        return content



class CreditCard:
    def __init__(self,number):
        self.number = number

    
    def validation(self,expiration,holder,cvc):
        card_data ={"number":self.number,"expiration":expiration,"holder":holder,"cvc":cvc}

        if card_data in df_cards:
            return True
        else:
            return False

class SerureCreditCard(CreditCard):
    def authenticate(self,password_given):
        password = df_security.loc[df_security["number"] == self.number,"password"].squeeze()
        if password == password_given:
            return True
        else:
            return False


print(df)
hotel_id =input("Enter the Id of the Hotel: ")
hotel = Hotel(hotel_id)


if hotel.available():
    card_number = input("Enter the card number : ")
    expDate = input("Enter the card expDate : ")
    holder_name = input("Enter the card holder_name : ")
    cvc = input("Enter the card cvc : ")
    password =input("Enter the card password : ")

    credit_card = SerureCreditCard(number =card_number)
    if credit_card.validation(expiration =expDate ,holder = holder_name,cvc= cvc):
        if credit_card.authenticate(password_given=password):
            hotel.book()
            name = input("user name :")
            resveration = ReservationTickets(name=name,hotel_object=hotel)
            print(resveration.generate())
        else:
            print("credit card authentication fails")
    else:
        print("problem with payment")
else:
    print("hotel is not avilable")
