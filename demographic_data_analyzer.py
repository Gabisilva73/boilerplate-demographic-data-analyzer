import pandas as pd

def calculate_demographic_data(print_data=True):
    # Ler os dados do arquivo CSV
    df = pd.read_csv('adult.data.csv')  # Certifique-se de usar o nome correto do arquivo CSV

    # Quantidade de pessoas de cada raça
    race_count = df['race'].value_counts()

    # Idade média dos homens
    average_age_men = round(df[df['sex'] == 'Male']['age'].mean(), 1)

    # Porcentagem de pessoas com diploma de Bacharelado
    percentage_bachelors = round((df['education'] == 'Bachelors').mean() * 100, 1)

    # Pessoas com e sem educação avançada (Bacharelado, Mestrado ou Doutorado)
    higher_education = df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])
    lower_education = ~higher_education

    # Porcentagem de pessoas com educação avançada que ganham mais de 50K
    higher_education_rich = round((df[higher_education & (df['salary'] == '>50K')].shape[0] / df[higher_education].shape[0]) * 100, 1)

    # Porcentagem de pessoas sem educação avançada que ganham mais de 50K
    lower_education_rich = round((df[lower_education & (df['salary'] == '>50K')].shape[0] / df[lower_education].shape[0]) * 100, 1)

    # Número mínimo de horas trabalhadas por semana
    min_work_hours = df['hours-per-week'].min()

    # Porcentagem das pessoas que trabalham o número mínimo de horas por semana e ganham mais de 50K
    num_min_workers = df[df['hours-per-week'] == min_work_hours]
    rich_percentage = round((num_min_workers[num_min_workers['salary'] == '>50K'].shape[0] / num_min_workers.shape[0]) * 100, 1)

    # País com a maior porcentagem de pessoas que ganham mais de 50K
    country_earnings = df[df['salary'] == '>50K']['native-country'].value_counts()
    country_totals = df['native-country'].value_counts()
    highest_earning_country = (country_earnings / country_totals).idxmax()
    highest_earning_country_percentage = round((country_earnings / country_totals).max() * 100, 1)

    # Ocupação mais popular para quem ganha mais de 50K na Índia
    top_IN_occupation = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]['occupation'].value_counts().idxmax()

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
