# 2024-07-11 03:44:01
# 8-13. User Profile: 
# Start with a copy of user_profile.py from page 148.
#  Build a profile of yourself by calling build_profile(),
#  using your first and last names and three other key- value pairs that describe you.

def build_profile(first, last, **user_info):
    user_info['first_name'] = first
    user_info['last_name'] = last 
    return user_info

user_profile = build_profile('albert', 'einstein', location='princeton',field='physics')          
me = build_profile('johnathan', 'hwang', school='csula', city='alhambra', major='computer science')                 
print(user_profile)
print(me)
