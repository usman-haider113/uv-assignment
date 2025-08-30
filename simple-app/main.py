def main():
    # Required prints as per assignment
    print("=" * 50)
    print("Name: Usman Haider")
    print("PIAIC Registration Number: PIAIC121722") 
    print("=" * 50)
    
    # Simple calculator functionality
    print("\n🔢 Simple Calculator App")
    print("This app demonstrates basic arithmetic operations")
    
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        operation = input("Enter operation (+, -, *, /): ")
        
        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 == 0:
                print("❌ Error: Cannot divide by zero!")
                return
            result = num1 / num2
        else:
            print("❌ Invalid operation!")
            return
            
        print(f"✅ Result: {num1} {operation} {num2} = {result}")
        
    except ValueError:
        print("❌ Please enter valid numbers!")
    except KeyboardInterrupt:
        print("\n👋 Goodbye!")


if __name__ == "__main__":
    main()
