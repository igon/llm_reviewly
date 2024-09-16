import os

def read_guest_record(file_path):
    if not os.path.exists(file_path):
        print(f"File {file_path} does not exist. Creating a new file with default content.")
        default_content = """
# Guest Record

## Guest Information
**Name:** Bob

## Points of Interest
_No interest yet._

"""
        with open(file_path, "w") as file:
            file.write(default_content)
        return default_content

    with open(file_path, "r") as file:
        return file.read()

def write_guest_record(file_path, content):
    with open(file_path, "w") as file:
        file.write(content)

def format_guest_record(guest_info, points_of_interest):
    record = "# Guest Record\n\n## Guest Information\n"
    for key, value in guest_info.items():
        record += f"**{key}:** {value}\n"
    
    record += "\n## Points of Interest\n"
    if points_of_interest:
        for key, value in points_of_interest.items():
          record += f"- **{key}:** {value}\n"
    else:
        record += "_No interest yet._\n"
    
    return record

def parse_guest_record(markdown_content):
    student_info = {}
    points_of_interest = {}
    
    current_section = None
    lines = markdown_content.split("\n")
    
    for line in lines:
        line = line.strip()  # Strip leading/trailing whitespace
        if line.startswith("## "):
            current_section = line[3:].strip()
        elif current_section == "Guest Information" and line.startswith("**"):
            if ":** " in line:
                key, value = line.split(":** ", 1)
                key = key.strip("**").strip()
                value = value.strip()
                student_info[key] = value
        elif current_section == "Points of Interest":
            if "_No interest yet._" in line:
                points_of_interest = {}
            elif line.startswith("- **"):        
                if ":** " in line:
                    key, value = line.split(":** ", 1)
                    key = key.strip("- **").strip()
                    value = value.strip()
                    points_of_interest[key] = value
    
    final_record = {
        "Guest Information": student_info,
        "Points of Interest": points_of_interest
    }
    print(f"Final parsed record: {final_record}")
    return final_record