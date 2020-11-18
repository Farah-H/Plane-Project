from authentication import Authentication
from user_staff import Staff

### Admin can ###
# Do everything a Staff Member can
# Can add a new staff member
# Change Staff Permissions
# Can view all information (sensitive too)
# Can add / remove / edit all flight information


class Admin(Authentication, Staff):
    # These are self explanatory
    # All return True / False

    def add_staff(self, username, password):
        pass

    def remove_staff(self, username):
        pass

    def change_permissions(self, username, new_perm):
        pass

    # View's all information about user
    def view_user(self, username):
        # Returns list
        pass

    # takes flight number string
    # and any new information as dictionary
    def edit_flight(self, flight_ref, **kwargs):
        # Returns True False
        pass

    # Same as above but takes all info as dict
    def add_flight(self, **kwargs):
        # True / False
        pass