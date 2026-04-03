class Record:

    def __init__(self, registry_no):
        self.registry_no = registry_no

    def to_dict(self):
        return {
            "registry_no": self.registry_no,
            "type": self.__class__.__name__
        }

    def __str__(self):
        return f"Registry No. {self.registry_no}"

    @classmethod
    def create_from_dict(cls, data):
        record_type = data["type"]

        if record_type == "BirthRecord":
            return BirthRecord.from_dict(data)
        elif record_type == "MarriageRecord":
            return MarriageRecord.from_dict(data)
        elif record_type == "DeathRecord":
            return DeathRecord.from_dict(data)
        else:
            raise ValueError("Unknown record type")


class BirthRecord(Record):

    def __init__(self, registry_no, first_name, middle_name, last_name,
                 birth_date, place_birth, fathers_name, mothers_name):

        super().__init__(registry_no)

        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.birth_date = birth_date
        self.place_birth = place_birth
        self.fathers_name = fathers_name
        self.mothers_name = mothers_name

    def __str__(self):
        return (
            f"[BIRTH RECORD]\n"
            f"Registry No.: {self.registry_no}\n"
            f"Name: {self.first_name} {self.middle_name} {self.last_name}\n"
            f"Birth Date: {self.birth_date}\n"
            f"Place of Birth: {self.place_birth}\n"
            f"Father's Name: {self.fathers_name}\n"
            f"Mother's Name: {self.mothers_name}"
        )

    def to_dict(self):
        data = super().to_dict()
        data.update({
            "first_name": self.first_name,
            "middle_name": self.middle_name,
            "last_name": self.last_name,
            "birth_date": self.birth_date,
            "place_birth": self.place_birth,
            "fathers_name": self.fathers_name,
            "mothers_name": self.mothers_name
        })
        return data

    @classmethod
    def from_dict(cls, data):
        return cls(
            data["registry_no"],
            data["first_name"],
            data["middle_name"],
            data["last_name"],
            data["birth_date"],
            data["place_birth"],
            data["fathers_name"],
            data["mothers_name"]
        )


class MarriageRecord(Record):

    def __init__(self, registry_no, groom_id, bride_id,
                 marriage_date, place_marriage):

        super().__init__(registry_no)

        self.groom_id = groom_id
        self.bride_id = bride_id
        self.marriage_date = marriage_date
        self.place_marriage = place_marriage

    def __str__(self):
        return (
            f"[MARRIAGE RECORD]\n"
            f"Registry No.: {self.registry_no}\n"
            f"Groom: {self.groom_id}\n"
            f"Bride: {self.bride_id}\n"
            f"Date of Marriage: {self.marriage_date}\n"
            f"Place of Marriage: {self.place_marriage}"
        )

    def to_dict(self):
        data = super().to_dict()
        data.update({
            "groom_id": self.groom_id,
            "bride_id": self.bride_id,
            "marriage_date": self.marriage_date,
            "place_marriage": self.place_marriage

        })
        return data

    def display(self, service):
        groom = service.get_person(self.groom_id)
        bride = service.get_person(self.bride_id)

        groom_name = f"{groom.first_name} {groom.last_name}" if groom else "Unknown"
        bride_name = f"{bride.first_name} {bride.last_name}" if bride else "Unknown"

        return (
            f"[MARRIAGE RECORD]\n"
            f"Registry No.: {self.registry_no}\n"
            f"Groom: {groom_name}\n"
            f"Bride: {bride_name}\n"
            f"Date of Marriage: {self.marriage_date}\n"
            f"Place of Marriage: {self.place_marriage}"
        )

    @classmethod
    def from_dict(cls, data):
        return cls(
            data["registry_no"],
            data["groom_id"],
            data["bride_id"],
            data["marriage_date"],
            data["place_marriage"]
        )


class DeathRecord(Record):

    def __init__(self, registry_no, person_id, death_date,
                 place_death, cause_death):

        super().__init__(registry_no)

        self.person_id = person_id
        self.death_date = death_date
        self.place_death = place_death
        self.cause_death = cause_death

    def __str__(self):
        return (
            f"[DEATH RECORD]\n"
            f"Registry No.: {self.registry_no}\n"
            f"Name: {self.person_id}\n"
            f"Date of Death: {self.death_date}\n"
            f"Place of Death: {self.place_death}\n"
            f"Cause of Death: {self.cause_death}\n"
        )

    def to_dict(self):
        data = super().to_dict()
        data.update({
            "person_id": self.person_id,
            "death_date": self.death_date,
            "place_death": self.place_death,
            "cause_death": self.cause_death
        })
        return data

    def display(self, service):
        person = service.get_person(self.person_id)

        name = f"{person.first_name} {person.last_name}" if person else "Unknown"

        return (
            f"[DEATH RECORD]\n"
            f"Registry No.: {self.registry_no}\n"
            f"Name: {name}\n"
            f"Date of Death: {self.death_date}\n"
            f"Place of Death: {self.place_death}\n"
            f"Cause of Death: {self.cause_death}\n"
        )

    @classmethod
    def from_dict(cls, data):
        return cls(
            data["registry_no"],
            data["person_id"],
            data["death_date"],
            data["place_date"],
            data["cause_death"]

        )
