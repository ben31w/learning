import json

import pygame.font


filename = 'fonts.json'
with open(filename, 'w') as f:
    # Store the system's default font.
    default_font_msg = f"Default font:\n{pygame.font.get_default_font()}"
    json.dump(default_font_msg, f)

    # Store all fonts available on the system in alphabetical order.
    all_fonts_msg = "\nAll fonts:"
    json.dump(all_fonts_msg, f)

    for font in sorted(pygame.font.get_fonts()):
        font_text = f"\n- {font}"
        json.dump(font_text, f)

# Print the system's default font.
print("\nDefault font:")
print(pygame.font.get_default_font())

# Print all fonts available on the system in alphabetical order.
print("\nAll fonts:")
for font in sorted(pygame.font.get_fonts()):
    print(f"- {font}")