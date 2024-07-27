def get_cats_info(path):
    
    try:
        with open(path, 'r', encoding='utf-8') as file:
            cats_info = []
            for line in file:
                cat_id, name, age = line.strip().split(',')
                cats_info.append({"id": cat_id, "name": name, "age": age})
        return cats_info
   
    
    except FileNotFoundError:
        print(f">>> FileNotFoundError файл не знайдено {path}")
        return None
    except Exception as e:
        print(f">>> Exception e {e}")
        return None


cats_info = get_cats_info("cats_Library.txt")
print(cats_info)
