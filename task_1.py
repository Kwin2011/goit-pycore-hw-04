def total_salary(path):
    
    try:
        with open(path, 'r', encoding='utf-8') as file:
            salaries = []
            for line in file:
                _, salary = line.strip().split(',')
                salaries.append(int(salary))
        
        total = sum(salaries)
        average = total // len(salaries) if salaries else 0
        return total, average
    

    except FileNotFoundError:
        print(f">>> FileNotFoundError файл не знайдено {path}")
        return None, None
    except Exception as e:
        print(f">>> Exception e {e}")
        return None, None


total, average = total_salary("employ_Library")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
