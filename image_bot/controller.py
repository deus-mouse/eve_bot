from playback import initialize_pyautogui, countdown_timer, play_actions
from time import sleep
import pyautogui

DELAY_BETWEEN_LOOPS = 20.00


def main():
    initialize_pyautogui()
    countdown_timer()

    LOOP_REPITITIONS = 4
    for i in range(0, LOOP_REPITITIONS):
        # get_starting_pos() should return an integer that corresponds with which
        # recorded action script should be played
        try:
            found = confirm_position("open_space")
            if found:
                play_actions('open_space_go_to_nearest_doc.json')
        except Exception as ex:
            print('Exception', ex)
        finally:
            print('sleep')
            sleep(DELAY_BETWEEN_LOOPS)

        # Completed loop
        print("Completed loop")

    print("Done")


# def create_screenshot():
#     filename = 'test_screenshot.png'
#     script_dir = os.path.dirname(__file__)
#     filepath = os.path.join(script_dir, 'images', filename)
#     image = pyautogui.screenshot(filepath)


def confirm_position(position_name):
    if position_name == "open_space":
        x, y = (958, 973)
        rgb = (48, 207, 75)
    else:
        raise Exception("Position to confirm not recognized")

    pixel_matches = pyautogui.pixelMatchesColor(x, y, rgb, tolerance=10)
    if not pixel_matches:
        debug_str = "Pos: {} RGB expected: {} RGB found: {}".format(
            (x, y),
            rgb,
            pyautogui.pixel(x, y)
        )
        raise Exception("Detected off course for {}. Debug: {}".format(
            position_name,
            debug_str
        ))

    print("On track for {}".format(position_name))
    return True


if __name__ == "__main__":
    main()
