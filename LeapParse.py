from Drawer import DrawObj
import os, sys, inspect, thread, time
src_dir = os.path.dirname(inspect.getfile(inspect.currentframe()))
arch_dir = 'C:/Users/Kevin Zheng/Documents/HackValley/LeapDeveloperKit_3.2.0+45899_win/LeapSDK/lib/x64' if sys.maxsize > 2**32 else 'C:/Users/Kevin Zheng/Documents/HackValley/LeapDeveloperKit_3.2.0+45899_win/LeapSDK/lib/x86'
sys.path.insert(0, os.path.abspath(os.path.join(src_dir, arch_dir)))
sys.path.append('C:/Users/Kevin Zheng/Documents/HackValley/LeapDeveloperKit_3.2.0+45899_win/LeapSDK/lib')
import Leap


from Leap import CircleGesture, KeyTapGesture, ScreenTapGesture, SwipeGesture

def is_horizontal(swipe):
    """
    Returns true if the swipe is horizontal.
    """
    swipe = Leap.SwipeGesture(swipe)
    direction = swipe.direction
    return abs(direction[0]) > abs(direction[1])

def swipe_helper(gestures):
    """
    A helper function.

    Determines whether or not the gesture was a horizontal swipe.
    """
    if len(gestures) > 3:
        for gesture in gestures:
            if gesture.type is Leap.Gesture.TYPE_SWIPE:
                horizontal = is_horizontal(gesture)
                #Regarding Swipe event, fix only a certain flatness of horizontal
                #swipes to be the correct swipe.
                if horizontal:
                    return True

    return False

class LeapListener(Leap.Listener):
    """
    Basic listener for Leap Motion interface.

    Implemented motions are swipes for the left hand and drawing
    for the right index finger.
    """

    #Global Constants.
    finger_names = ['Thumb', 'Index', 'Middle', 'Ring', 'Pinky']
    bone_names = ['Metacarpal', 'Proximal', 'Intermediate', 'Distal']
    drawer = DrawObj("./image.jpg")
    action = False

    def on_init(self, controller):
        print "Initialized"

    def on_connect(self, controller):
        controller.enable_gesture(Leap.Gesture.TYPE_SWIPE)

    def on_disconnect(self, controller):
        # Note: not dispatched when running in a debugger.
        print "Disconnected"

    def on_exit(self, controller):
        print "Exited"

    def on_frame(self, controller):
        # Get the most recent frame and report some basic information
        frame = controller.frame()

        for hand in frame.hands:
            #Draw commands for the right hand.
            if not hand.is_left:
                for finger in hand.fingers:
                    if finger.type == 1:

                        #Position is here.
                        #Used for DRAWING.
                        pos = finger.stabilized_tip_position
                        if self.drawer.isDrawing:
                            print "FIRST: %f, SECOND: %f" % (pos[0], pos[1])
                            self.drawer.draw(int((pos[0] + 100) * 5), int((200 - (pos[1] - 200)) * 5), 1)
            #Swipe commands for the left hand.
            if hand.is_left:
                actionPast = self.action
                self.action = swipe_helper(frame.gestures())
                if not self.action:
                    if(actionPast):
                        print "Swiped"
                        if self.drawer.isDrawing:
                            self.drawer.end()
                        else:
                            self.drawer.start()





def main():
    # Create a sample listener and controller
    listener = LeapListener()
    controller = Leap.Controller()

    # Have the sample listener receive events from the controller
    controller.add_listener(listener)

    # Keep this process running until Enter is pressed
    print "Press Enter to quit..."
    try:
        sys.stdin.readline()
    except KeyboardInterrupt:
        pass
    finally:
        # Remove the sample listener when done
        controller.remove_listener(listener)


if __name__ == "__main__":
    main()
