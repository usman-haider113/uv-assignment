def main():
    # Required prints as per assignment
    print("=" * 50)
    print("Name: Usman Haider")
    print("PIAIC Registration Number: PIAIC121722")
    print("=" * 50)
    
    # Task Manager functionality
    print("\n📋 Task Manager App")
    print("This app demonstrates task management with a simple todo list")
    
    tasks = []
    
    while True:
        print("\n" + "=" * 30)
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task Complete")
        print("4. Exit")
        print("=" * 30)
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == '1':
            task = input("Enter task description: ")
            if task.strip():
                tasks.append({"description": task, "completed": False})
                print("✅ Task added successfully!")
            else:
                print("❌ Task description cannot be empty!")
                
        elif choice == '2':
            if not tasks:
                print("📝 No tasks found. Add some tasks first!")
            else:
                print("\n📋 Your Tasks:")
                for i, task in enumerate(tasks, 1):
                    status = "✅" if task["completed"] else "⏳"
                    print(f"{i}. {status} {task['description']}")
                    
        elif choice == '3':
            if not tasks:
                print("📝 No tasks to mark complete!")
            else:
                try:
                    task_num = int(input("Enter task number to mark complete: ")) - 1
                    if 0 <= task_num < len(tasks):
                        tasks[task_num]["completed"] = True
                        print(f"✅ Task '{tasks[task_num]['description']}' marked complete!")
                    else:
                        print("❌ Invalid task number!")
                except ValueError:
                    print("❌ Please enter a valid number!")
                    
        elif choice == '4':
            print("👋 Goodbye! Thanks for using Task Manager!")
            break
            
        else:
            print("❌ Invalid choice! Please enter 1-4.")


if __name__ == "__main__":
    main()
