from ecommerce.customer import contact
from ..customer import contact

# print("Sales initialized")
print("Sales initialized", __name__)
# Sales initialized __main__

contact.contact_customer()


def calc_tax():
    pass


def calc_shipping():
    pass


if __name__ == "__main__":
    print("Sales started")
    calc_tax()
