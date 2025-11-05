from utils.runner import run_quiz

def main():
    print("🧪 Generador de Test de Bases de Datos")
    print("Seleccione una unidad:")
    print("1. Unidad 1: Almacenamiento y uso de datos")
    print("2. Unidad 2: Consultas con SQL")
    print("3. Unidad 3: Diseño de Bases de Datos")
    print("4. Unidad 4: Administración de un SGBD")
    print("5. Unidad 5: Administración avanzada de SGBDR")
    print("6. Unidad 6: Consultas avanzadas con SQL")
    print("7. Unidad 7: Programación en el SGBDR")
    print("8. Unidad 8: Bases de Datos NoSQL")

    choice = input("👉 Ingrese el número de la unidad (1–8): ")

    if choice == "1":
        from quizzes.quiz1 import questions
    elif choice == "2":
        from quizzes.quiz2 import questions
    elif choice == "3":
        from quizzes.quiz3 import questions
    elif choice == "4":
        from quizzes.quiz4 import questions
    elif choice == "5":
        from quizzes.quiz5 import questions
    elif choice == "6":
        from quizzes.quiz6 import questions
    elif choice == "7":
        from quizzes.quiz7 import questions
    elif choice == "8":
        from quizzes.quiz8 import questions
    else:
        print("❌ Opción inválida. Intente con un número del 1 al 8.")
        return

    run_quiz(questions)

if __name__ == "__main__":
    main()