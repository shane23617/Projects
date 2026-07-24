from datetime import datetime
import pandas as pd
class TimeManagement:
    def __init__(self):
        self.time_table = pd.DataFrame()

class StudySession:
    def __init__(self):
        self.session_id = None
        self.topic_id = None
        self.module_id = None
        self.schedule_date = None
        self.start_time = None
        self.end_time = None
        self.duration = None
        self.is_completed = False
        self.priority_score = None
    def study_duration(self):
        self.duration = self.end_time - self.start_time
        if self.duration > 0:
            self.is_completed = False
        else :
            self.is_completed = True









