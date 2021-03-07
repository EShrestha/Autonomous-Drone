from djitellopy import tello
from time import sleep

# Connections #
drone = tello.Tello()
drone.connect()
print(drone.get_battery())
drone.takeoff()  # Drone takes off
# Connections #

# rc_control =  (left/right, forward/backward, up/down, turning(left,right))


def verse1():
    # We're no strangers to love
    drone.send_rc_control(0, -10, 0, 0)
    drone.send_rc_control(0, 10, 0, 0)
    # You know the rules and so do I
    drone.send_rc_control(-10, 0, 0, 0)
    drone.send_rc_control(10, 0, 0, 0)
    # A full commitment's what I'm thinkin of
    drone.send_rc_control(0, 0, 20, 100)
    # You wouldn't get this from any other guy
    drone.send_rc_control(10, 0, -20, 0)


def chorus():
    # Never gonna give you up
    drone.send_rc_control(0, 0, 50, 0)
    # Never gonna let you down
    drone.send_rc_control(0, 0, -50, 0)
    # Never gonna run around
    drone.send_rc_control(0, 50, 0, 50)
    drone.send_rc_control(0, 50, 0, 50)
    drone.send_rc_control(0, 50, 0, 50)
    drone.send_rc_control(0, 50, 0, 50)
    # and desert you
    drone.send_rc_control(0, -50, 0, 0)
    drone.send_rc_control(0, 50, 0, 0)
    # Never gonna make you cry
    drone.send_rc_control(0, 0, 0, -20)
    drone.send_rc_control(0, 0, 0, 20)
    # Never gonna say good bye
    drone.send_rc_control(0, -20, 0, 0)
    drone.send_rc_control(0, 20, 0, 0)
    # Never gonna tell a lie and hurt you
    drone.send_rc_control(0, 0, 0, -10)
    drone.send_rc_control(0, 0, 0, 10)
    drone.send_rc_control(0, 30, 0, 0)


# [Pre-Chorus]
# I just wanna tell you how I'm feeling
# Gotta make you understand


def prechorus():
    # rc_control =  (left/right, forward/backward, up/down, turning(left,right))
    drone.send_rc_control(0, 100, 30, 0)
    drone.flip_back()
    drone.flip_back()

    drone.send_rc_control(0, -50, -10, 0)
    drone.flip_forward()
    drone.flip_forward()


def verse2():
    # rc_control =  (left/right, forward/backward, up/down, turning(left,right))
    # We've known each other for so long
    drone.send_rc_control(0, 0, 100, 0)

    # Your heart's been aching, but you're too shy to say it
    drone.send_rc_control(-50, 0, 0, 0)
    drone.flip_right()
    drone.send_rc_control(50, 0, 0, 0)
    drone.flip_left()

    # Inside, we both know what's been going on
    drone.send_rc_control(-50, 0, 0, 0)
    drone.flip_right()
    drone.send_rc_control(50, 0, 0, 0)
    drone.flip_left()

    # We know the game, and we're gonna play it
    drone.send_rc_control(0, 0, -100, 0)

    # [Post-Chorus]
    # Ooh(Give you up)
    # Ooh-ooh(Give you up)
    # Ooh-ooh
    # Never gonna give, never gonna give(Give you up)
    # Ooh-ooh
    # Never gonna give, never gonna give(Give you up)


def postchorus():
    # rc_control =  (left/right, forward/backward, up/down, turning(left,right))
    drone.send_rc_control(100, 0, 100, 0)
    drone.send_rc_control(-100, 0, -100, 0)
    drone.send_rc_control(-100, 0, 100, 0)
    drone.send_rc_control(100, 0, -100, 0)

    drone.send_rc_control(100, 0, 100, 0)
    drone.send_rc_control(-100, 0, -100, 0)
    drone.send_rc_control(-100, 0, 100, 0)
    drone.send_rc_control(100, 0, -100, 0)

    drone.send_rc_control(0, 0, 100, 0)
    drone.send_rc_control(0, 0, -100, 0)
    drone.send_rc_control(0, 0, 100, 0)

sleep(10)
# [Verse 1]
verse1()

# [Pre chorus]
prechorus()

# [Chorus]
chorus()

# [Verse 2]
verse2()

# [Pre chorus]
prechorus()

# [Chorus]
chorus()

# [Post-Chorus]
postchorus()

# [Bridge]
verse2()

# [Pre chorus]
prechorus()

# [Chorus] x3
chorus()
chorus()
chorus()

