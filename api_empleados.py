import requests

def get_employees_data(url):
    headers = requests.utils.default_headers()
    headers.update({
        'User-Agent': 'My User Agent 1.0',
    })

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return response.json()['data']
    else:
        return None

def calculate_statistics(data):
    total_employees = len(data)

    total_salary = sum(float(employee['employee_salary']) for employee in data)
    average_salary = total_salary / total_employees

    total_age = sum(int(employee['employee_age']) for employee in data)
    average_age = total_age / total_employees

   # salaries = [float(employee['employee_salary']) for employee in data]
    #min_salary = min(salaries)
    #max_salary = max(salaries)
    salarios = [float(employee['employee_salary']) for employee in data]

    # Ordenar los salarios en orden ascendente
    salarios_ordenados = sorted(salarios)

    salario_minimo = salarios_ordenados[0]
    salario_maximo = salarios_ordenados[-1]

    ages = [int(employee['employee_age']) for employee in data]
    min_age = min(ages)
    max_age = max(ages)

    return {
        'total_employees': total_employees,
        'average_salary': average_salary,
        'average_age': average_age,
        'min_salary': salario_minimo,
        'max_salary': salario_maximo,
        'min_age': min_age,
        'max_age': max_age,
    }

def print_results(statistics):
    print(f"Número de empleados: {statistics['total_employees']}")
    print(f"Promedio de salario: {statistics['average_salary']}")
    print(f"Promedio de edad: {statistics['average_age']}")
    print(f"Salario mínimo: {statistics['min_salary']}")
    print(f"Salario máximo: {statistics['max_salary']}")
    print(f"Edad menor: {statistics['min_age']}")
    print(f"Edad mayor: {statistics['max_age']}")

if __name__ == '__main__':
    url = 'https://dummy.restapiexample.com/api/v1/employees'
    employees_data = get_employees_data(url)

    if employees_data is not None:
        statistics = calculate_statistics(employees_data)
        print_results(statistics)
    else:
        print("Error al obtener los datos de empleados.")