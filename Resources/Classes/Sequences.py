class Sequences:
    def __init__(self, string):
        self.sequence=string
        self.metric_Satisfied=False
    def get_string(self):
        return self.sequence
    def is_satisfied(self):
        return self.metric_Satisfied
    def change_satisfied(self,boolean):
        self.metric_Satisfied=boolean
    def get_char(self,index):
        return self.sequence[index]
    def get_len(self):
        return len(self.sequence)
