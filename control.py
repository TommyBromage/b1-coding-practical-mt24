class PDController:
    def __init__(self, Kp=0.15, Kd=0.6):
        self.Kp = Kp
        self.Kd = Kd  
        self.prev_error = 0

    def compute(self, reference, output):
        error = reference - output
        control = self.Kp * error + self.Kd * (error - self.prev_error)
        self.prev_error = error
        return control