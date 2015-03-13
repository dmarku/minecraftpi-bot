# A moving "Robot" for the Minecraft RPi Edition

Currently implemented:

*   `Robot` class to store robot state, move around and draw its state with minecraft blocks
    *   `draw()` draws the robot in the minecraft world
    *   `forward()` moves the robot one block in the direction of the torch
    *   `backward()` moves the robot one block back
    *   `left()` turns the robot 90 degrees to the left. It will stay in its current position.
    *   `right()` turns the robot 90 degrees to the right. It will stay in its current position.

The "robot" is drawn as a stone block at its current position and a torch indicating its direction. Drawing updates have to be done manually. "Undrawing" elements is not yet implemented.
