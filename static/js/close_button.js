window.onload = function () {
    let close_btn = document.querySelector('#close-button');
    let messages_wrapper = document.querySelector('#messages-wrapper');

    close_btn.addEventListener('click', function () {
        messages_wrapper.remove()
    })

}