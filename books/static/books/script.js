// Confirm before deleting a book
document.addEventListener('DOMContentLoaded', function () {
    const deleteLinks = document.querySelectorAll('a[href^="/delete/"]');
    deleteLinks.forEach(link => {
        link.addEventListener('click', function (event) {
            if (!confirm("Are you sure you want to delete this book?")) {
                event.preventDefault();
            }
        });
    });
});
