from json_db import JSONDatabase
from services import RegistryService
from record import BirthRecord, MarriageRecord, DeathRecord

db = JSONDatabase("data/records.json")
service = RegistryService(db)


def main():
    while True:
        print("\n=== CIVIL REGISTRY SYSTEM ===")
        print("1. Add Birth Record")
        print("2. Add Marriage Record")
        print("3. Add Death Record")
        print("4. View All Records")
        print("5. Exit")

        choice = input("Choose: ")

        try:
            if choice == "1":
                record = BirthRecord(
                    input("Registry No: "),
                    input("First Name: "),
                    input("Middle Name: "),
                    input("Last Name: "),
                    input("Birth Date (YYYY-MM-DD): "),
                    input("Place of Birth: "),
                    input("Father's Name: "),
                    input("Mother's Name: ")
                )
                service.add_records(record)
                print("Birth record added!")

            elif choice == "2":
                record = MarriageRecord(
                    input("Registry No: "),
                    input("Groom ID (Birth Registry No): "),
                    input("Bride ID (Birth Registry No): "),
                    input("Marriage Date (YYYY-MM-DD): "),
                    input("Place of Marriage: ")
                )
                service.add_records(record)
                print("Marriage record added!")

            elif choice == "3":
                record = DeathRecord(
                    input("Registry No: "),
                    input("Person ID (Birth Registry No): "),
                    input("Death Date (YYYY-MM-DD): "),
                    input("Place of Death: "),
                    input("Cause of Death: ")
                )
                service.add_records(record)
                print("Death record added!")

            elif choice == "4":
                records = service.get_all_records()

                for record in records:
                    print("-" * 40)
                    if hasattr(record, "display"):
                        print(record.display(service))
                    else:
                        print(record)

            elif choice == "5":
                break

            else:
                print("Invalid choice.")

        except ValueError as e:
            print("Error:", e)


if __name__ == "__main__":
    main()
# elif choice == "2":  # show all records
#     records = service.get_all_records()

#     for record in records:
#         if hasattr(record, "display"):
#             print(record.display(service))
#         else:
#             print(record)
