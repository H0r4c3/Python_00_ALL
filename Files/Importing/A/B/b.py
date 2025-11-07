from A import a  # absolute import

def function_from_b():
    print("Hello from script b!")
    
    # Test the import
    result_a = a.function_from_a()
    print(f"Got: {result_a}")
    
    return "Data from B"

def main():
    print("Running b.py directly")
    function_from_b()

if __name__ == "__main__":
    main()