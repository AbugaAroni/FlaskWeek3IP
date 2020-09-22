class Pitch:

    all_pitches = []

    def __init__(self,pitch_id,pitch_title,pitch_description,pitch_category):
        self.id = pitch_id
        self.title = pitch_title
        self.category = pitch_category
        self.description = pitch_description



    def save_pitches(self):
        Pitch.all_pitches.append(self)


    @classmethod
    def clear_pitches(cls):
        Pitch.all_pitches.clear()

    @classmethod
    def get_pitches(cls,category):

        response = []

        for pitches in cls.all_pitches:
            if pitch.pitch_category == category:
                response.append(pitch)

        return response