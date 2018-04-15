function hidePopup() {
    // When the user press the esc key, close the modal
    document.addEventListener('keydown', function (event) {
        if (event.keyCode === 27) {
            location.href = '#';
        }
    });
}