$(document).ready(function() {


    function getCode() {
        $.ajax({
            url: `http://127.0.0.1:5000/shorten`,
            type: 'POST',
            success: function(response) {
                
                const tbody = $('.inventory-card table tbody');
                tbody.empty(); // Clear existing table rows
                const data = response.inventory;

                data.forEach(item => {
                    const row = `<tr>
                        <td>${item.blood_type}</td>
                        <td>${item.available_units}</td>
                    </tr>`;
                    tbody.append(row);
                });
                // console.log(data);
            },
            error: function(xhr, status, error) {
                console.error(`Error accessing ${authority} inventory:`, status, error);
                // Optional: Implement retry or user notification here
            }
        });
    }


});