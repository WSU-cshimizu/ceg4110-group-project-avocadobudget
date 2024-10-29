// Sample expenses to start with
const expenses = [
    { id: '#123456', date: '2022-05-22', method: 'Debit card', amount: '5110', description: 'Rent', category: 'Rental' },
    { id: '#123457', date: '2022-06-01', method: 'Cash', amount: '220', description: 'Groceries', category: 'Regular Expense' },
    { id: '#123458', date: '2022-07-10', method: 'Credit card', amount: '320', description: 'Subscription', category: 'Miscellaneous' },
    { id: '#123459', date: '2022-06-15', method: 'Debit card', amount: '150', description: 'Utilities', category: 'Bills' },
    { id: '#123460', date: '2022-07-05', method: 'Bank transfer', amount: '600', description: 'Dining Out', category: 'Entertainment' },
    { id: '#123461', date: '2022-08-20', method: 'Credit card', amount: '75', description: 'Gym Membership', category: 'Health & Fitness' },
   
];

// Variables for the modal and form
const expenseTable = document.getElementById('expense-table');
const modal = document.getElementById('expense-modal');
const modalTitle = document.getElementById('modal-title');
const expenseForm = document.getElementById('expense-form');

// Form fields
const descriptionInput = document.getElementById('expdesc');
const categoryInput = document.getElementById('expcat');
const amountInput = document.getElementById('expamt');
const paymentMethodInput = document.getElementById('payment-method');
const dateInput = document.getElementById('expdate');

// Buttons
const newExpenseBtn = document.getElementById('new-expense-btn');
const cancelBtn = document.getElementById('cancel-btn');
const submitBtn = document.getElementById('submit-btn');

// Track editing state
let isEditing = false;
let editingExpenseId = null;

// Render initial expenses in the table
function renderExpenses(filteredExpenses = expenses) {
    expenseTable.innerHTML = ''; // Clear existing rows

    filteredExpenses.forEach(expense => {
        const row = document.createElement('tr');
        row.innerHTML = `
            <td>${expense.id}</td>
            <td>${expense.date}</td>
            <td>${expense.method}</td>
            <td>${expense.amount}</td>
            <td>${expense.description}</td>
            <td>${expense.category}</td>
            <td><button class="edit-btn" data-id="${expense.id}">Edit</button></td>
            <td><button class="delete-btn" data-id="${expense.id}">Delete</button></td>
        `;
        expenseTable.appendChild(row);
    });

    document.querySelectorAll('.edit-btn').forEach(button => {
        button.addEventListener('click', handleEdit);
    });

    document.querySelectorAll('.delete-btn').forEach(button => {
        button.addEventListener('click', handleDelete);
    });
}

// Open the modal for adding a new expense
newExpenseBtn.addEventListener('click', () => {
    isEditing = false;
    clearForm();
    modalTitle.textContent = 'Add New Expense';
    submitBtn.textContent = 'Add Expense';
    modal.style.display = 'flex';
});

// Handle form submission
expenseForm.addEventListener('submit', (event) => {
    event.preventDefault();
    const newExpense = {
        id: isEditing ? editingExpenseId : `#${Math.floor(Math.random() * 1000000)}`,
        date: dateInput.value,
        method: paymentMethodInput.value,
        amount: amountInput.value,
        description: descriptionInput.value,
        category: categoryInput.value
    };

    if (isEditing) {
        const expenseIndex = expenses.findIndex(expense => expense.id === editingExpenseId);
        expenses[expenseIndex] = newExpense;
    } else {
        expenses.push(newExpense);
    }

    //renderExpenses();
    closeModal();
});

// Open the modal for editing
function handleEdit(event) {
    isEditing = true;
    editingExpenseId = event.target.getAttribute('data-id');

    const expense = expenses.find(exp => exp.id === editingExpenseId);

    descriptionInput.value = expense.description;
    categoryInput.value = expense.category;
    amountInput.value = expense.amount;
    paymentMethodInput.value = expense.method;
    dateInput.value = expense.date;

    modalTitle.textContent = 'Edit Expense';
    submitBtn.textContent = 'Update Expense';
    modal.style.display = 'flex';
}

// Handle deletion
// function handleDelete(event) {
//     const expenseId = event.target.getAttribute('data-id');
//     const expenseIndex = expenses.findIndex(expense => expense.id === expenseId);

//     expenses.splice(expenseIndex, 1);
//     renderExpenses();
// }

// Close modal and clear form
cancelBtn.addEventListener('click', closeModal);

function closeModal() {
    modal.style.display = 'none';
    clearForm();
}

function clearForm() {
    descriptionInput.value = '';
    categoryInput.value = '';
    amountInput.value = '';
    paymentMethodInput.value = '';
    dateInput.value = '';
}

// Real-time description search
// document.getElementById("search-description").addEventListener("input", () => {
//     const searchTerm = document.getElementById("search-description").value.toLowerCase();
//     const filteredExpenses = expenses.filter(expense =>
//         expense.description.toLowerCase().includes(searchTerm)
//     );
//     renderExpenses(filteredExpenses);
// });

// // Initial render
// renderExpenses();





