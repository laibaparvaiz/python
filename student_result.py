class StudentsDataException(Exception):
    """Base exception for student data errors."""
    pass

class BadLine(StudentsDataException):
    """Exception raised for invalid"""
    pass

class FileEmpty(StudentsDataException):
    """Exception raised when file is empty"""
    pass

def process_file(filename):
    student_scores = {}
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            if not lines:
                raise FileEmpty("the file is empty.")
            
            for line_num, line in enumerate(lines, 1):
                line = line.strip()

                if not line:
                    raise BadLine(f"Empty line at line (line_num).")

                parts = line.split()
                if len(parts) != 3:
                    raise BadLine(f"Line {line_num} is incorrectly fortamtted: {line}")
                first_name, last_name, score_str = parts

                try:
                    score = float(score_str)
                except ValueError:
                    raise BadLine(f"Inavlid score at line {line_num}: {score_str}")
                
                full_name = f"{first_name} {last_name}"
                student_scores[full_name] = student_scores.get(full_name, 0) + score

    except FileNotFoundError:
        print('Error: file not found.')
        return
    
    except StudentsDataException as e:
        print(f"Data error: {e}")
        return
    
    for name in sorted(student_scores):
        print(f"{name:<20} {student_scores[name]}")

filename = input("Enter the name of Prof. Jekyll's file:  ")
process_file(filename)