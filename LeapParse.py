import os, sys, inspect, thread, time
src_dir = os.path.dirname(inspect.getfile(inspect.currentframe()))
arch_dir = 'C:/Users/Kevin Zheng/Documents/HackValley/LeapDeveloperKit_3.2.0+45899_win/LeapSDK/lib/x64' if sys.maxsize > 2**32 else 'C:/Users/Kevin Zheng/Documents/HackValley/LeapDeveloperKit_3.2.0+45899_win/LeapSDK/lib/x86'
sys.path.insert(0, os.path.abspath(os.path.join(src_dir, arch_dir)))
sys.path.append('C:/Users/Kevin Zheng/Documents/HackValley/LeapDeveloperKit_3.2.0+45899_win/LeapSDK/lib')
import Leap
import Image, color, numpy


from Leap import CircleGesture, KeyTapGesture, ScreenTapGesture, SwipeGesture

#Private helper function, true if swiping
def __swipehelper__(frame):
	if len(frame.gestures()) > 3:
		for gesture in frame.gestures():
			if gesture.type is Leap.Gesture.TYPE_SWIPE:
				swipe = Leap.SwipeGesture(gesture)
				direction = swipe.direction
				isHorizontal = abs(direction[0]) > abs(direction[1])
				#Regarding Swipe event, fix only a certain flatness of horizontal
				#swipes to be the correct swipe.
				if(isHorizontal):
					return True
				
	return False

class SampleListener(Leap.Listener):
    finger_names = ['Thumb', 'Index', 'Middle', 'Ring', 'Pinky']
    bone_names = ['Metacarpal', 'Proximal', 'Intermediate', 'Distal']
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
			# Get fingers
            if not hand.is_left:
				for finger in hand.fingers:
					if finger.type == 1:
						pos = finger.stabilized_tip_position
			if hand.is_left:
		
				actionPast = self.action
				self.action = __swipehelper__(frame)
				if not self.action:
					if(actionPast):
						#Swiped event call here.
						print "Swiped"
		
		
		

def main():
    # Create a sample listener and controller
    listener = SampleListener()
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
