from Drawer import DrawObj
from imgurUploader import uploadImage
import os, sys, inspect, thread, time
src_dir = os.path.dirname(inspect.getfile(inspect.currentframe()))
arch_dir = '../LeapDeveloperKit_3.2.0+45899_win/LeapSDK/lib/x64' if sys.maxsize > 2**32 else '../LeapDeveloperKit_3.2.0+45899_win/LeapSDK/lib/x86'
sys.path.insert(0, os.path.abspath(os.path.join(src_dir, arch_dir)))
sys.path.append('../LeapDeveloperKit_3.2.0+45899_win/LeapSDK/lib')
import Leap
import pygame
import pyimgur
import requests

from Leap import CircleGesture, KeyTapGesture, ScreenTapGesture, SwipeGesture

def is_horizontal(direction):
    return abs(direction[0]) > abs(direction[1])

def is_notplane(direction):
    return (abs(direction[2]) > abs(direction[0])) & (abs(direction[2]) > abs(direction[1]))

def get_direction(swipe):
    """
    Returns true if the swipe is horizontal.
    """
    swipe = Leap.SwipeGesture(swipe)
    return swipe.direction

def swipe_helper(gestures):
    """
    A helper function.

    Determines whether or not the gesture was a horizontal swipe.
    """
    horizontal = False
    is_left = False
    is_swipe = False
    is_up = False
    is_forward = False
    nonplanar = False
    if len(gestures) > 2:
        for gesture in gestures:
            is_swipe = gesture.type is Leap.Gesture.TYPE_SWIPE
            if is_swipe:
                directions = get_direction(gesture)
                horizontal = is_horizontal(directions)
                nonplanar = is_notplane(directions)
                is_left = directions[0] < 0
                is_up = directions[1] > 0.6
                is_forward = directions[2] < 0
                #Regarding Swipe event, fix only a certain flatness of horizontal
                #swipes to be the correct swipe.
                return (horizontal, is_left, is_up, is_swipe, nonplanar, is_forward)
    return (horizontal, is_left, is_up, is_swipe, nonplanar, is_forward)

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
    draw = False
    past_up = False
    is_forward = False
    nonplanar = False
    is_swipe = False
    is_up = False
    is_left = False
    horizontal = False
    radius = 10

    x = 0
    y = 0
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
                        
                        self.x = int((pos[0] + 200) * 2.5)
                        self.y = int((pos[2] + 200) * 2.5)

                        if self.x < 50:
                            if self.y < 50:
                                self.radius = 5
                            elif self.y < 100:
                                self.radius = 10
                            elif self.y < 150:
                                self.radius = 15
                        if self.drawer.isDrawing:
                            if self.draw:
                                if hand.pinch_strength == 0:
                                    self.drawer.erase(int((pos[0] + 200) * 2.5), int((pos[2] + 200) * 2.5), self.radius)	
                                else:
                                    self.drawer.draw(int((pos[0] + 200) * 2.5), int((pos[2] + 200) * 2.5), self.radius)
                            else:
                                self.drawer._lastX =  None 
                                self.drawer._lastY = None
                                
            #Swipe commands for the left hand.
            if hand.is_left:
                flags = swipe_helper(frame.gestures())
                self.is_forward = flags[5]
                self.nonplanar = flags[4]
                self.is_swipe = flags[3]
                self.past_up = self.is_up
                self.is_up = flags[2]
                self.is_left = flags[1]
                self.horizontal = flags[0]

                self.draw = hand.grab_strength == 1
                
                if self.is_swipe:
                    if self.nonplanar:
                        if self.is_forward:
                            if self.drawer.isDrawing:
                                print "Swipe Forward Clear"
                                self.drawer.clear()
                    elif self.horizontal & self.drawer.isDrawing:
                        if self.is_left:
                            print "Send Facebook Left"
                        else:
                            print "Send Twitter Right"
                        self.drawer.end()
                        uploadImage("./output.png", self.is_left)
                    else:
                        if self.is_up:
                            if not self.drawer.isDrawing:
                                print "Start Draw"
                                self.drawer.start()
                            else:
                                if not self.past_up:
                                    self.drawer.undo()




def main():
    # Create a sample listener and controller
    listener = LeapListener()
    controller = Leap.Controller()

    # Have the sample listener receive events from the controller
    controller.add_listener(listener)

    # Keep this process running until Enter is pressed
    print "Press Enter to quit..."

    RED = 255, 0, 0
    WHITE = 255, 255, 255
    pygame.init()
    screen = pygame.display.set_mode((1000, 1000))
    pygame.display.set_caption("Moving Box")
    clock = pygame.time.Clock()
    while 1:
        clock.tick(50)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        screen.fill(WHITE)
        if(listener.drawer._image != None):
            mode = listener.drawer._image.mode
            size = listener.drawer._image.size
            data = listener.drawer._image.tobytes()

            py_image = pygame.image.fromstring(data, size, mode)

            screen.blit(py_image, (10, 10))
            
        
        pygame.draw.circle(screen, RED, (listener.x-5, listener.y-5), listener.radius)
        pygame.draw.rect(screen, RED, (0, 0, 50, 50), 5)
        pygame.draw.rect(screen, RED, (0, 50, 50, 50), 5)
        pygame.draw.rect(screen, RED, (0, 100, 50, 50), 5)
        pygame.display.flip()
    try:
        sys.stdin.readline()
    except KeyboardInterrupt:
        pass
    finally:
        # Remove the sample listener when done
        controller.remove_listener(listener)
    
    # Send image to server
    






if __name__ == "__main__":
    main()



