// Récupérer les éléments du riskForlm et results
const form = document.getElementById('riskForm');
const resultsDiv = document.getElementById('results');

form.addEventListener('submit', async (e) => {
    e.preventDefault();

    // Récupérer les valeurs du formulaire
    const formData = new FormData(form);
    const data = {};
    formData.forEach((value, key) => 
        {
            if (key === 'interest_rate') 
            {
                // Convertir le pourcentage en décimal
                data[key] = parseFloat(value) / 100.0;
            } 
            
            else 
            {
                // Convertir les autres valeurs en float
                data[key] = parseFloat(value);
            }
        });

    try {
        // Envoyer les données au backend
        const response = await fetch('http://127.0.0.1:5000/score', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        });

        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }

        const prediction = await response.json();

        // Afficher les résultats
        resultsDiv.textContent = `Prediction Results:\n\n`;
        // Afficher la probabilité de défaut en pourcentage avec deux décimales
        resultsDiv.textContent += `Probability of Default: ${(prediction.probability_of_default * 100).toFixed(2)}\n`;
        resultsDiv.textContent += `Is Anomaly: ${prediction.is_anomaly}\n`;
        } 

        catch (error) 
        {
            console.error('Error:', error);
            resultsDiv.textContent = 'An error occurred while fetching the prediction.';
        }

});