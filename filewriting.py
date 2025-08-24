# create_file.py
"""with open("input.txt", "w") as f:
    f.write("This is my first Python file.\nI want to see it modified.")
print("✅ input.txt created successfully!")
"""

def main():
    try:
        # Step 1: Ask the user for the file name they want to read
        input_file = input("Enter the filename to read: ")

        # Step 2: Open the file in READ mode and get its content
        with open(input_file, "r") as f:
            content = f.read()

        # Step 3: Modify the content (here we convert it to UPPERCASE)
        modified_content = content.upper()

        # Step 4: Create a new filename by adding "modified_" at the start
        output_file = "modified_" + input_file

        # Step 5: Open the new file in WRITE mode and save the modified content
        with open(output_file, "w") as f:
            f.write(modified_content)

        # Step 6: Tell the user where the new file was saved
        print(f"✅ File processed successfully! Modified content saved in: {output_file}")

    # ERROR HANDLING (if something goes wrong)
    except FileNotFoundError:
        print("❌ Error: File not found. Please check the filename and try again.")
    except PermissionError:
        print("❌ Error: You don’t have permission to read this file.")
    except Exception as e:
        print(f"❌ An unexpected error occurred: {e}")


# This ensures the main() function runs only when you run this script directly
if __name__ == "__main__":
    main()
