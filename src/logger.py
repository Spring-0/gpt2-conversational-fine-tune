import os
import csv
from datetime import datetime

class Logger:
    def __init__(self, file="discord_gpt_log.csv"):
        self.file = file

        if not os.path.exists(self.file):
            with open(self.file, mode='w', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(['Timestamp', 'Prompt', 'Response', 'IsGood'])

    def log_interaction(self, prompt, response, isGood):
        entry = [self.get_timestamp(), prompt, response, isGood]

        with open(self.file, mode='a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(entry)

    def get_timestamp(self):
        return datetime.now().strftime('%Y-%m-%d %H:%M:%S')