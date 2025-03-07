document.addEventListener('DOMContentLoaded', () => {
    const arrayContainer = document.getElementById('array-container');
    const stepsContainer = document.getElementById('steps');
    const startSortingBtn = document.getElementById('start-sorting');
    const algorithmSelect = document.getElementById('algorithm');
    const arrayInput = document.getElementById('array-input');

    async function startSorting() {
        const inputArray = arrayInput.value;
        const array = inputArray.split(',').map(Number);  // Convert input to an array of numbers

        // Basic validation for array input
        if (array.some(isNaN)) {
            alert("Please enter a valid array of numbers.");
            return;
        }

        const algorithm = algorithmSelect.value;
        const response = await fetch('/sort', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ array, algorithm })
        });

        const steps = await response.json();

        // Clear previous steps
        stepsContainer.innerHTML = '';

        // Visualize the sorting process
        for (let i = 0; i < steps.length; i++) {
            const step = steps[i];
            arrayContainer.innerHTML = '';  // Clear the previous bars
            
            // Display current step in the steps container
            const stepDiv = document.createElement('div');
            stepDiv.textContent = `Step ${i + 1}: ${step.join(', ')}`;
            stepsContainer.appendChild(stepDiv);

            // Render the bars for the current step
            step.forEach(value => {
                const bar = document.createElement('div');
                bar.classList.add('bar');
                bar.style.height = `${(value * 100) / Math.max(...step)}%`;  // Normalize height

                // Create a label for each bar
                const label = document.createElement('div');
                label.classList.add('bar-label');
                label.textContent = value;
                bar.appendChild(label);

                arrayContainer.appendChild(bar);
            });

            // Slow down the visualization to make it visible to the user
            await new Promise(resolve => setTimeout(resolve, 200)); // 500ms delay
        }
    }

    startSortingBtn.addEventListener('click', startSorting);
});
