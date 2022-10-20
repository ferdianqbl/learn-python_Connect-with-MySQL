import mysql.connector


def sqlConnect():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="employees_db",
        auth_plugin="mysql_native_password"
    )


def dbCursor():
    database = sqlConnect()
    db_cursor = database.cursor()
    return db_cursor


def createDatabase():
    dbCursor().execute("CREATE TABLE IF NOT EXISTS employees (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), role VARCHAR(255), salary INT)")

    dbCursor().execute("SELECT * FROM employees")


def addEmployee():
    name = input("Enter employee name: ")
    role = input("Enter employee role: ")
    salary = input("Enter employee salary: ")

    dbCursor().execute("INSERT INTO employees (name, role, salary) VALUES (%s, %s, %s)",
                       (name, role, salary))

    sqlConnect().commit()

    print(dbCursor().rowcount, "record inserted.")
