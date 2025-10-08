from build_profile import build_profile as bp

user_profile = bp('albert', 'einstein',
                  location='princeton',
                  field='physics',)

my_profile = bp('ben', 'wright',
                location='leesburg',
                birth_town='nam dinh',
                favorite_foods=["pizza", "mac n' cheese", "pho"])

print(user_profile)
print(my_profile)