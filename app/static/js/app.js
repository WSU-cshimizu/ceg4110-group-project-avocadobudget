const budgetData = [
    {category: 'Rental', percentage: 10, amount: '$100'},
    {category: 'Regular expense', percentage: 20, amount: '$200'},
    {category: 'Miscellaneous', percentage: 25, amount: '$300'},
    {category: 'Grocery', percentage: 30, amount: '$1150'},
    {category: 'Education', percentage: 5, amount: '$100'},
    {category: 'Medical', percentage: 20, amount: '$500'}
];

let editingIndex = null;

// Function to populate the budget table
function populateTable() {
    const tableBody = document.getElementById('budget-table-body');
    tableBody.innerHTML = ''; // Clear existing rows

    budgetData.forEach((budget, index) => {
        const row = `
            <tr>
                <td>${budget.category}</td>
                <td>${budget.percentage}%</td>
                <td>${budget.amount}</td>
                <td><button class="edit-btn" data-index="${index}">Edit</button></td>
            </tr>
        `;
        tableBody.innerHTML += row;
    });

    document.querySelectorAll('.edit-btn').forEach(button => {
        button.addEventListener('click', function () {
            editingIndex = this.getAttribute('data-index');
            const budget = budgetData[editingIndex];
            document.getElementById('edit-category-amount').value = budget.amount.replace('$', '');
            document.getElementById('edit-category-modal').style.display = 'flex';
        });
    });
}

// Function to handle opening and closing modal
const modal = document.getElementById('new-category-modal');
const editModal = document.getElementById('edit-category-modal');
const openModalBtn = document.getElementById('open-modal-btn');
const cancelBtn = document.getElementById('cancel-btn');
const editCancelBtn = document.getElementById('edit-cancel-btn');

// Open new category modal
openModalBtn.addEventListener('click', () => {
    modal.style.display = 'flex';
});

// Close new category modal
cancelBtn.addEventListener('click', () => {
    modal.style.display = 'none';
});

// Close edit category modal
editCancelBtn.addEventListener('click', () => {
    editModal.style.display = 'none';
});

// Submit new category form
document.getElementById('new-category-form').addEventListener('submit', (event) => {
    event.preventDefault();
    const categoryName = document.getElementById('category-name').value;
    const categoryAmount = document.getElementById('category-amount').value;

    if (categoryName && categoryAmount) {
        budgetData.push({
            category: categoryName,
            percentage: 0, // Calculate based on your logic
            amount: `$${categoryAmount}`
        });
        //populateTable();
        modal.style.display = 'none';
    }
});

// Submit edit category form
document.getElementById('edit-category-form').addEventListener('submit', (event) => {
    event.preventDefault();
    const newAmount = document.getElementById('edit-category-amount').value;
    if (editingIndex !== null && newAmount) {
        budgetData[editingIndex].amount = `$${newAmount}`;
        //populateTable();
        editModal.style.display = 'none';
    }
});

// Initial population of the table
//populateTable();
