from record import MarriageRecord, DeathRecord


class RegistryService:

    def __init__(self, db):
        self.db = db
        self.records = db.load()

    def add_records(self, record):
        if self.find_by_registry_no(record.registry_no):
            raise ValueError("Registry nummber already exists!")

        if self.find_by_registry_no(record.registry_no):
            raise ValueError("Registry number already exists!")

        if isinstance(record, MarriageRecord):  # Marriage Rrules

            if not self.exists(record.groom_id):
                raise ValueError("Groom does not exist!")
            if not self.exists(record.bride_id):
                raise ValueError("Bride does not exist!")

            if self.is_person_dead(record.groom_id):
                raise ValueError("Groom is already deaceased!")
            if self.is_person_dead(record.bride_id):
                raise ValueError("Bride is already deaceased!")

        if isinstance(record, DeathRecord):
            if not self.exists(record.person_id):
                raise ValueError("Person does not exists!")

        self.records.append(record)
        self.db.save(self.records)

    def get_all_records(self):
        return self.records

    def find_by_registry_no(self, registry_no):
        for record in self.records:
            if record.registry_no == registry_no:
                return record

        return None

    def search_by_last_name(self, last_name):
        results = []

        for record in self.records:
            if hasattr(record, "last_name") and record.last_name.lower() == last_name.lower():
                results.append(record)

        return results

    def delete_record(self, registry_no):
        record = self.find_by_registry_no(registry_no)\

        if record:
            self.records.remove(record)
            self.db.save(self.records)
            return True

        return False

    def get_person(self, registry_no):
        return self.find_by_registry_no(registry_no)

    def exists(self, registry_no):
        return self.find_by_registry_no(registry_no) is not None

    def is_person_dead(self, person_id):
        for record in self.records:
            if isinstance(record, DeathRecord) and record.person_id == person_id:
                return True
        return False
