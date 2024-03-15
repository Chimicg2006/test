from queue import Queue 
def main():
    patient_queue = Queue()

    while True:
        print("\\nMenu:")
        print("1. Register Patient")
        print("2. Remove Patient after Meeting Doctor")
        print("3. Display Patient Queue")
        print("4. Exit")
        choice = input("Enter your name to register:")

        if choice == "1":
            name = input("Enter pateint's name to register:")
            patient_queue.put(name)
            print(f"Patient {name} registered.")
        elif choice == "2":
            if patient_queue.empty():
                print("No patients in queue.")
            else:
                name = patient_queue.get()
                print(f"patient {name} has to met the doctor and is now removed from th queue.")
        elif choice == "3":
            if patient_queue.empty():
                print("No patients in queue.")
            else:
                print("Patients in queue:")
                for index, name in enumerate(list(patient_queue.queue)):
                    print(f"{index + 1}. {name}")
        elif choice == "4":
            print("Exiting program.")
            break
        else:
            print("Invalid input. Please enter a number between 1 and 4.")


if __name__ == "__main__":
   main()
            
