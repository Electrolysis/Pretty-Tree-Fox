import os
import platform
import sys
import errno

root_dir = os.path.dirname(os.path.abspath(__file__))

# Copy file function by Vadim Vladimirovich
def copyfile(from_path, to_path):
    with open(from_path, 'r') as input_file:
        input_lines = input_file.readlines()
    with open(to_path, 'w') as output_file:
        output_file.writelines(input_lines)

# Define OS
if platform.system() == 'Darwin':
    profiles_path = os.environ['HOME'] + '/Library/Application Support/Firefox/Profiles'
elif platform.system() == 'Windows':
    profiles_path = os.environ['APPDATA'] + '/Mozilla/Firefox/Profiles'
else:
    sys.exit('fuck u, buy a mac')

print('WARNING!\nCLOSE FIREFOX BEFORE THE INSTALL!\n')

profiles = os.listdir(profiles_path)
full_path_list = []
index = 0
print('Founded profiles:')
for profile in profiles:
    full_path = os.path.join(profiles_path, profile)
    if os.path.isdir(full_path):
        full_path_list.append(full_path)
        print('  profile #{}: {}'.format(index, profile))
        index += 1

user_choice = int(input('Choose your profile (you can find name of your using profile at about:profiles page): '))
profile_choice = full_path_list[user_choice]

# Enabling userchrome support in prefs.js
with open(os.path.join(profile_choice,'prefs.js'), 'a') as file:
    file.write('user_pref("toolkit.legacyUserProfileCustomizations.stylesheets", true);')

# Copy content of userChrome files to profile
if not os.path.exists(os.path.join(profile_choice, 'Chrome')):
    os.makedirs(os.path.join(profile_choice, 'Chrome'))

copyfile(os.path.join(root_dir, 'Chrome/userChrome.css'), os.path.join(profile_choice, 'Chrome/userChrome.css'))