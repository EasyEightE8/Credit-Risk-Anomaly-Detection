import pandas as pd
import numpy as np
from faker import Faker
import os 
from datetime import datetime, timedelta

N_ROWS = 75000 # Number of rows to generate
DEFAULT_RATE_BASE = 0.10 # 10% default interest rate
N_ANOMALIES = int(N_ROWS * 0.05) # 5% anomalies
fake = Faker('fr_FR')
OUTPUT_FILE = 'database/simulated_loans.csv'

def generate_loan_data(n_rows=N_ROWS, default_rate=DEFAULT_RATE_BASE, n_anomalies=N_ANOMALIES):
    np.random.seed(42)  # For reproducibility
    data = []
    # Génération des données de prêt
    for _ in range(n_rows):
        loan_amount = np.random.randint(1000, 75000)
        interest_rate = round(np.random.uniform(0.03, 0.15), 4)
        term_months = np.random.choice([12, 24, 36, 48, 60])
        start_date = fake.date_between(start_date='-5y', end_date='today')
        end_date = start_date + timedelta(days=int(term_months * 30))
        borrower_age = np.random.randint(18, 70)
        borrower_income = np.random.randint(20000, 150000)
        credit_score = np.random.randint(300, 850)
        
        # Adjust default probability based on credit score and loan-to-income ratio
        proba_de_defaut_ajustee = default_rate
        if credit_score < 600:
            proba_de_defaut_ajustee += 0.20
        if borrower_income < 30000:
            proba_de_defaut_ajustee += 0.15
        if loan_amount / borrower_income > 0.5:
            proba_de_defaut_ajustee += 0.10
        # Limiter la probabilité de défaut à un maximum de 90%
        proba_de_defaut_ajustee = min(proba_de_defaut_ajustee, 0.90)
        # Déterminer si le prêt est en défaut
        defaulted = np.random.rand() < proba_de_defaut_ajustee

        # Ajouter la ligne de données
        data.append({
            'loan_amount': loan_amount,
            'interest_rate': interest_rate,
            'term_months': term_months,
            'start_date': start_date,
            'end_date': end_date,
            'borrower_age': borrower_age,
            'borrower_income': borrower_income,
            'credit_score': credit_score,
            'defaulted': int(defaulted)
            'is_simulated_anomaly': 0
        })

    df = pd.DataFrame(data)
    # Introduce anomalies
    for _ in range(n_anomalies):
        idx = np.random.randint(0, n_rows)
        anomaly_type = np.random.choice(['negative_loan', 'high_interest', 'invalid_dates', 'extreme_income'])
        # Marquer cette ligne comme une anomalie simulée
        df.at[idx, 'is_simulated_anomaly'] = 1

        if anomaly_type == 'negative_loan':
            df.at[idx, 'loan_amount'] = -abs(df.at[idx, 'loan_amount'])
        elif anomaly_type == 'high_interest':
            df.at[idx, 'interest_rate'] = round(np.random.uniform(0.5, 1.0), 4)  # Unrealistically high interest rate
        elif anomaly_type == 'invalid_dates':
            df.at[idx, 'end_date'] = df.at[idx, 'start_date'] - timedelta(days=30)  # End date before start date
        elif anomaly_type == 'extreme_income':
            df.at[idx, 'borrower_income'] = np.random.randint(1000000, 5000000)  # Unrealistically high income
    return df

if __name__ == "__main__":
    df_loans = generate_loan_data(N_ROWS, DEFAULT_RATE_BASE, N_ANOMALIES)
    os.makedirs(os.path.dirname(OUTPUT_FILE), exist_ok=True)
    df_loans.to_csv(OUTPUT_FILE, index=False)
    print(f"Taux de défaut moyen: {df_loans['defaulted'].mean():.2%}")
    print(df_loans.head())