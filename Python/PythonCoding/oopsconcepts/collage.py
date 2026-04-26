class collage:
    def __init__(self, ccode, cname, ccity):
        self.collcode = ccode
        self.collname = cname
        self.collcity = ccity

    def welcome_message(self):
        print('Hello there !!!')

    def display_collage_details(self):
        print('collage code : {} \n  collage name : {} \n city{} ', self.collcode,self.collname,
              self.collcity)
