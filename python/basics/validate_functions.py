# Validaciones de datos usando funciones
# Cada validación está separada en su propia función reutilizable tambien llamado "single responsibility"
# Autor: Candy | Fecha: mayo 2026

def validate_name(name):
    if not name.strip():
        return "nombre vacío"
    return None

def validate_email(email):
    if "@" not in email or "." not in email:
        return f"email inválido: {email}"
    return None

def validate_age(age):
    if not age.isdigit() or int(age) <= 0:
        return f"edad inválida: {age}"
    return None

def validate_user(user):
    errors = []

    name_error = validate_name(user["name"])
    email_error = validate_email(user["email"])
    age_error = validate_age(user["age"])

    if name_error:
        errors.append(name_error)
    if email_error:
        errors.append(email_error)
    if age_error:
        errors.append(age_error)

    return errors

# --- Programa principal ---
users = [
    {"id": "1", "name": "Ana García", "email": "ana@example.com", "age": "28"},
    {"id": "2", "name": "", "email": "carlos@example.com", "age": "35"},
    {"id": "3", "name": "María López", "email": "no-es-un-email", "age": "22"},
    {"id": "4", "name": "Pedro Ruiz", "email": "pedro@example.com", "age": "-5"},
    {"id": "5", "name": "Laura Sánchez", "email": "laura@example.com", "age": "31"},
]

print("=== Validación de usuarios con funciones ===\n")

errors_found = 0

for user in users:
    errors = validate_user(user)
    if errors:
        print(f"❌ Usuario ID {user['id']}: {', '.join(errors)}")
        errors_found += 1
    else:
        print(f"✅ Usuario ID {user['id']} ({user['name']}): OK")

print(f"\n=== Resultado: {errors_found} error(es) encontrado(s) ===")