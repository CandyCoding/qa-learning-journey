import csv

# Datos de prueba — simulamos una lista de usuarios
users = [
    {"id": "1", "name": "Ana García", "email": "ana@example.com", "age": "28"},
    {"id": "2", "name": "", "email": "carlos@example.com", "age": "35"},
    {"id": "3", "name": "María López", "email": "no-es-un-email", "age": "22"},
    {"id": "4", "name": "Pedro Ruiz", "email": "pedro@example.com", "age": "-5"},
    {"id": "5", "name": "Laura Sánchez", "email": "laura@example.com", "age": "31"},
]

print("=== Validación de datos de usuarios ===\n")

errors_found = 0

for user in users:
    errors = []

    # Validación 1: nombre no puede estar vacío
    if not user["name"].strip():
        errors.append("nombre vacío")

    # Validación 2: email debe contener @ y .
    if "@" not in user["email"] or "." not in user["email"]:
        errors.append(f"email inválido: {user['email']}")

    # Validación 3: edad debe ser número positivo
    if not user["age"].isdigit() or int(user["age"]) <= 0:
        errors.append(f"edad inválida: {user['age']}")

    # Resultado por usuario
    if errors:
        print(f"❌ Usuario ID {user['id']}: {', '.join(errors)}")
        errors_found += 1
    else:
        print(f"✅ Usuario ID {user['id']} ({user['name']}): OK")

print(f"\n=== Resultado: {errors_found} error(es) encontrado(s) ===")