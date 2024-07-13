# 2024-07-12 12:39:43

from privileges import Admin

me = Admin("john", "hwang", 25, 91801, 1 )
me.describe_user()
me.privileges.show_privileges()
priv = ["delete", "add", "edit", "ban"]
me.privileges.show_privileges()

