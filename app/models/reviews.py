class Pitch:

    all_pitches = []

    def __init__(self,pitch_id,pitch_title,pitch_description):
        self.pitch_id = pitch_id
        self.pitch_title = pitch_title
        self.pitch_description = pitch_description


    def save_pitch(self):
        Review.all_pitches.append(self)


    @classmethod
    def clear_itches(cls):
        Review.all_pitches.clear()
