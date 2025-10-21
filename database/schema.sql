-- Database: `credit_risk_db`
USE credit_risk_db;

--  Table structure for table `loans`
CREATE TABLE loans (
    id INT AUTO_INCREMENT PRIMARY KEY,
    loan_amount INT,
    interest_rate DECIMAL(10, 4),
    term_months INT,
    start_date DATE,
    end_date DATE,
    borrower_age INT,
    borrower_income INT,
    credit_score INT,
    defaulted BOOLEAN,
    is_simulated_anomaly BOOLEAN
);