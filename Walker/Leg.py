# Leg class for grouping servos and making things easier
class Leg():
    def __init__(self, name, h_servo, v_servo, adj_leg):
        # h for horizontal shoulder
        # v for vertical shoulder
        # k for knee joint
        self.name = name
        self.h_servo = h_servo
        self.v_servo = v_servo
        self.adj_leg = adj_leg
        #self.k_servo = k_servo
    def step(self):
        #step leg forward
        #v_servo up
        #h_servo forward & adj_leg_servo backward
        #v_sevo down
        print("Stepping forward")
